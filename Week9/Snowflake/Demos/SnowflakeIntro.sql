-- ============================================
-- SECURITY / ACCESS CONTROL
-- ============================================

SHOW ROLES;                -- List all roles in the account
SHOW GRANTS;               -- Show all grants (who has access to what)

USE ROLE ACCOUNTADMIN;     -- Switch to highest privilege role (full control)

SHOW GRANTS TO ROLE ACCOUNTADMIN; -- See what this role can access/do


-- ============================================
-- ⚙️ WAREHOUSE (COMPUTE)
-- ============================================

SHOW WAREHOUSES;           -- List compute warehouses

CREATE OR REPLACE WAREHOUSE my_wh
  WAREHOUSE_SIZE = 'XSMALL';  -- Create small compute warehouse (cost-efficient)

USE WAREHOUSE MY_WH;       -- Set active warehouse (used for queries)

ALTER WAREHOUSE MY_WH SUSPEND;  
-- Pause warehouse to save money (no compute charges while suspended)

USE WAREHOUSE COMPUTE_WH;  -- Switch to default warehouse


-- ============================================
-- DATABASE & SCHEMA SETUP
-- ============================================

-- Create a development database
CREATE DATABASE IF NOT EXISTS DEV_DB
    COMMENT = 'Development Database for training with Snowflake';

SHOW DATABASES;            -- List all databases

USE DATABASE DEV_DB;       -- Set current database

-- Create schema (like a folder inside DB)
CREATE SCHEMA IF NOT EXISTS DEV_DB.SANDBOX;
USE SCHEMA DEV_DB.SANDBOX; -- Set working schema


-- ============================================
-- TABLE CREATION
-- ============================================

CREATE OR REPLACE TABLE DEV_DB.SANDBOX.ORDERS (
    order_id STRING PRIMARY KEY,         -- Unique order ID
    customer_id STRING NOT NULL,         -- Required customer ID
    order_date DATE NOT NULL,            -- Required order date
    order_status STRING,                 -- Optional status
    amount DECIMAL (12,2),               -- Monetary value
    processed_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
    -- Auto-populated timestamp when row inserted
)
COMMENT = 'Cleaned orders - typed/validated - ready for analysis';

DESCRIBE TABLE ORDERS;     -- Show table structure

SELECT * FROM DEV_DB.SANDBOX.ORDERS; -- View data


-- ============================================
-- TABLE TYPES (TEMP vs TRANSIENT)
-- ============================================

CREATE OR REPLACE TEMPORARY TABLE my_temp_table (
id INT,
name STRING
);
-- Temporary table → only exists for session, auto-deleted

CREATE OR REPLACE TRANSIENT TABLE my_transient_table (
id INT,
name STRING
);
-- Transient table → no fail-safe (cheaper, less recovery)


-- ============================================
-- PERMANENT TABLE + TIME TRAVEL
-- ============================================

CREATE OR REPLACE TABLE ORDERS_PERMANENT(
    order_id STRING,
    customer_id STRING,
    amount DECIMAL(10,2),
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
)
COMMENT = 'Permanent TABLE, 90 days time travel and 7 days fail safe';

SHOW TABLES;

-- Reduce time travel retention (default is higher depending on edition)
ALTER TABLE ORDERS_PERMANENT SET DATA_RETENTION_TIME_IN_DAYS=7;

-- Transient tables typically have 0 retention
ALTER TABLE my_transient_table SET DATA_RETENTION_TIME_IN_DAYS=0;


-- ============================================
-- STREAM (CHANGE DATA CAPTURE)
-- ============================================

CREATE OR REPLACE STREAM orders_stream
ON TABLE ORDERS_PERMANENT
APPEND_ONLY=FALSE              -- Track INSERT, UPDATE, DELETE
SHOW_INITIAL_ROWS=TRUE;        -- Treat existing rows as INSERTS initially

-- Stream = tracks changes since last consumption (not full history)


-- ============================================
-- CDC HISTORY TABLE
-- ============================================

CREATE OR REPLACE TABLE orders_cdc_history AS
SELECT 
    METADATA$ACTION AS action,       -- INSERT or DELETE
    METADATA$ISUPDATE AS is_update,  -- TRUE if part of update
    *
FROM orders_stream
WHERE 1=0;  
-- 1=0 ensures NO data is inserted, only schema is created


-- ============================================
-- INITIAL STREAM CONSUMPTION
-- ============================================

INSERT INTO orders_cdc_history
SELECT METADATA$ACTION, METADATA$ISUPDATE, *
FROM orders_stream;
-- Consumes stream → moves changes into history table


-- ============================================
-- INSERT SAMPLE DATA
-- ============================================

INSERT INTO ORDERS_PERMANENT VALUES 
    ('O001', 'C100',100.00,CURRENT_TIMESTAMP()),
    ('O002', 'C100',100.00,CURRENT_TIMESTAMP()),
    ('O003', 'C100',100.00,CURRENT_TIMESTAMP());

-- Check stream (should show INSERT events)
SELECT METADATA$ACTION, METADATA$ISUPDATE, * FROM orders_stream;

-- Persist changes into CDC table
INSERT INTO orders_cdc_history
SELECT METADATA$ACTION, METADATA$ISUPDATE, *
FROM orders_stream;


-- ============================================
-- UPDATE + DELETE OPERATIONS
-- ============================================

UPDATE ORDERS_PERMANENT 
SET amount=999 
WHERE order_id='O001';

DELETE FROM ORDERS_PERMANENT 
WHERE order_id='O003';

-- Stream now contains:
-- UPDATE → DELETE + INSERT pair
-- DELETE → DELETE record

SELECT METADATA$ACTION, METADATA$ISUPDATE, * FROM orders_stream;

-- Persist those changes
INSERT INTO orders_cdc_history
SELECT METADATA$ACTION, METADATA$ISUPDATE, *
FROM orders_stream;


-- ============================================
-- DATA VALIDATION
-- ============================================

SELECT * FROM ORDERS_PERMANENT;   -- Current state
SELECT * FROM orders_stream;      -- Remaining unconsumed changes
SELECT * FROM orders_cdc_history;-- Full CDC history


-- ============================================
-- TIME TRAVEL
-- ============================================

-- Query table as it existed ~260 seconds ago
SELECT * FROM ORDERS_PERMANENT AT (OFFSET => -260);

SELECT * FROM orders_stream;

SHOW STREAMS;                    -- List streams
DESCRIBE STREAM orders_stream;  -- Show stream details


-- ============================================
-- FILE FORMATS (FOR INGESTION)
-- ============================================

SELECT CURRENT_ROLE();

SHOW FILE FORMATS; 

CREATE OR REPLACE FILE FORMAT CSV_FORMAT
    TYPE='CSV'
    FIELD_DELIMITER = ','
    SKIP_HEADER=1
    NULL_IF = ('NULL','null','','N/A')
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    TRIM_SPACE=TRUE
    ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE
    COMMENT = 'STANDARD CSV format with header';

CREATE OR REPLACE FILE FORMAT JSON_FORMAT
    TYPE='JSON'
    STRIP_OUTER_ARRAY = TRUE
    COMMENT = 'JSON format for event data';


-- ============================================
-- STAGE (FILE STORAGE)
-- ============================================

-- Stage = location where files live before loading
-- Internal stage = managed by Snowflake (backed by cloud storage like S3)

CREATE OR REPLACE STAGE INTERNAL_LOAD_STAGE
    FILE_FORMAT = CSV_FORMAT
    COMMENT = 'Internal stage for loading CSV files';

LIST @INTERNAL_LOAD_STAGE; -- View files in stage


-- ============================================
-- DATA INGESTION (COPY INTO)
-- ============================================

-- Temporary staging table (raw data, no strict typing yet)
CREATE OR REPLACE TEMPORARY TABLE STAGING_ORDERS (
    order_id STRING,
    customer_id STRING,
    order_date STRING,
    amount STRING,
    status STRING
);

COPY INTO STAGING_ORDERS
FROM @INTERNAL_LOAD_STAGE
FILE_FORMAT = (FORMAT_NAME = CSV_FORMAT)
ON_ERROR = 'CONTINUE'   -- Skip bad rows
PURGE = FALSE;          -- Keep files after load (set TRUE in production)

SELECT * FROM STAGING_ORDERS LIMIT 100;