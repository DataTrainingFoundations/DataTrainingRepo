SHOW roles;
SHOW GRANTS;

USE role ACCOUNTADMIN;

SHOW GRANTS TO ROLE ACCOUNTADMIN;

SHOW warehouses;

CREATE OR REPLACE WAREHOUSE my_wh
  WAREHOUSE_SIZE = 'XSMALL';


USE WAREHOUSE MY_WH;
ALTER WAREHOUSE MY_WH SUSPEND;

USE WAREHOUSE COMPUTE_WH;

-- Creating a dev database
CREATE DATABASE IF NOT EXISTS DEV_DB
    COMMENT = 'Development Database for training with Snowflake';

SHOW DATABASES;

USE DATABASE DEV_DB;

CREATE SCHEMA IF NOT EXISTS DEV_DB.SANDBOX;
USE SCHEMA DEV_DB.SANDBOX;

CREATE OR REPLACE TABLE DEV_DB.SANDBOX.ORDERS (
    order_id STRING PRIMARY KEY,
    customer_id STRING NOT NULL,
    order_date DATE NOT NULL,
    order_status STRING,
    amount DECIMAL (12,2),
    processed_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
)
COMMENT = 'Cleaned orders - typed/validated - ready for analysis';

DESCRIBE TABLE ORDERS;

SELECT * FROM DEV_DB.SANDBOX.ORDERS;

CREATE OR REPLACE TEMPORARY TABLE my_temp_table (
id INT,
name STRING
);

CREATE OR REPLACE TRANSIENT TABLE my_transient_table (
id INT,
name STRING
);
----------------------------------------------
CREATE OR REPLACE TABLE ORDERS_PERMANENT(
    order_id STRING,
    customer_id STRING,
    amount DECIMAL(10,2),
    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
)
COMMENT = 'Permanent TABLE, 90 days time travel and 7 days fail safe';

SHOW TABLES;

ALTER TABLE ORDERS_PERMANENT SET DATA_RETENTION_TIME_IN_DAYS=7;

ALTER TABLE my_transient_table SET DATA_RETENTION_TIME_IN_DAYS=0;



CREATE OR REPLACE STREAM orders_stream
ON TABLE ORDERS_PERMANENT
APPEND_ONLY=FALSE
SHOW_INITIAL_ROWS=TRUE; --starts the stream with existing rows as "inserted"
;

CREATE OR REPLACE TABLE orders_cdc_history AS
SELECT 
    METADATA$ACTION AS action,
    METADATA$ISUPDATE AS is_update,
    *
FROM orders_stream
WHERE 1=0;

INSERT INTO orders_cdc_history
SELECT METADATA$ACTION, METADATA$ISUPDATE, *
FROM orders_stream;

INSERT INTO ORDERS_PERMANENT VALUES 
    ('O001', 'C100',100.00,CURRENT_TIMESTAMP()),
    ('O002', 'C100',100.00,CURRENT_TIMESTAMP()),
    ('O003', 'C100',100.00,CURRENT_TIMESTAMP());

-- check stream
SELECT METADATA$ACTION, METADATA$ISUPDATE, * FROM orders_stream;

INSERT INTO orders_cdc_history
SELECT METADATA$ACTION, METADATA$ISUPDATE, *
FROM orders_stream;

-- update + delete
UPDATE ORDERS_PERMANENT SET amount=999 WHERE order_id='O001';
DELETE FROM ORDERS_PERMANENT WHERE order_id='O003';

-- check stream again
SELECT METADATA$ACTION, METADATA$ISUPDATE, * FROM orders_stream;

INSERT INTO orders_cdc_history
SELECT METADATA$ACTION, METADATA$ISUPDATE, *
FROM orders_stream;


SELECT * FROM ORDERS_PERMANENT;
SELECT * FROM orders_stream;
SELECT * FROM orders_cdc_history;



--time travel where offset is in seconds 
SELECT * FROM ORDERS_PERMANENT AT (OFFSET => -260);

SELECT * FROM orders_stream;

SHOW STREAMS;

DESCRIBE STREAM orders_stream;
--------------------------------------------------
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

-- IN Snowflake, a stage is where files live before they're loaded into our instance
-- Think of it like the S3 bucket we used when working with Spark EMR
-- Internal Stages are managed by snowflake, they're just S3 buckets (provided you chose AWS during account creation)
-- In production we'd probably use an external stage, that explicitly point to a managed S3 bucket

CREATE OR REPLACE STAGE INTERNAL_LOAD_STAGE
    FILE_FORMAT = CSV_FORMAT
    COMMENT = 'Internal stage for loading CSV files';

--list all files currently in the stage
LIST @INTERNAL_LOAD_STAGE;

--can use PUT IF IN CLI
--PUT file:///C:/Users/WilliamTerry/Desktop/TRNGDataJan2026/GitHubRepoForDataJan2026/Week9/Snowflake/Demos/sample_orders.csv INTERNAL_LOAD_STAGE; 

-- First , we create a temp staging table
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
ON_ERROR = 'CONTINUE'
PURGE =FALSE; -- Keep files after loading, don't throw them out of the stage
--Set purge to TRUE once you get your ingestion logic working

SELECT * FROM STAGING_ORDERS LIMIT 100;