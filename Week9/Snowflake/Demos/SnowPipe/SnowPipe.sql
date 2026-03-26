--https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration


---> set Role Context
USE ROLE ACCOUNTADMIN;

---> set Warehouse Context
USE WAREHOUSE COMPUTE_WH;

---> set the Database
USE DATABASE DEV_DB;


----------------------------
--create s3 bucket
--create iam-> role (first create policy 
--use 2nd option aws account for the trusted entity type


------------------
--do this in s3 to work: (for pipe to work with auto instead of refreshing)
--Open the bucket

--Go to Properties

--Find Event notifications

--Create new notification

--USE SHOWPIPES for queue arn

--------------------------------------------------

-- CREATE SCHEMA IF NOT EXISTS DEV_DB.public;


--Snowflake uses Storage Integration to access S3 securely:

-- Create storage integration
CREATE OR REPLACE STORAGE INTEGRATION s3_int_will1
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::08016124657:role/willsnowrolemar11'
-- STORAGE_ALLOWED_LOCATIONS = ('*');
STORAGE_ALLOWED_LOCATIONS = ('s3://my-snowpipe-bucket-will1/');

DESC INTEGRATION s3_int_will1

CREATE OR REPLACE STAGE my_s3_stage_will1
URL='s3://my-snowpipe-bucket-will1/data'
STORAGE_INTEGRATION = s3_int_will1;

CREATE OR REPLACE TABLE  DEV_DB.public.raw_events (
    event_id INTEGER,
    event_timestamp TIMESTAMP_NTZ,
    event_type STRING,
    user_id INTEGER
);

CREATE OR REPLACE PIPE DEV_DB.public.my_pipe
AUTO_INGEST = TRUE
AS
COPY INTO DEV_DB.public.raw_events
FROM (
    SELECT  $1:event_id::INTEGER,
        $1:timestamp::TIMESTAMP_NTZ,
        $1:event_type::STRING,
        $1:user_id::INTEGER
    FROM @my_s3_stage_will1
)
FILE_FORMAT = (TYPE = JSON);

--SELECT SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO();
DESC PIPE DEV_DB.public.my_pipe;

SHOW PIPES;

SELECT "name", "notification_channel"
FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()));

ALTER PIPE DEV_DB.public.my_pipe REFRESH;

-- Query your table:

SELECT * FROM DEV_DB.public.raw_events;