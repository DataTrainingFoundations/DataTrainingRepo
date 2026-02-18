## Data Lifecycle Stages

### Core Stages
 1. Data is generated or captured.
 Examples
 - User submits a web form
 - IoT sensor records temperature
 - Application logs events
 - Database transactions occur
 - producers send JSON messages to Kafka

 2. Data Ingestion
  Data is brought into a system for storage processing
 Examples
 - Kafka topics receive events
 - ETL pipeline load data in a warehouse
 - APIs pull data from external services

 3. Data Storage
   Data is persisted Somewhere
  Examples
  - Relational DB (PostgreSQL, MySQL)
  - Data warehouse (Snowflake, BigQuery)
  - Data Lake (S3, ADLS)

 4. Data Processing / Transformation
  Raw Data is cleaned, enriched, or transformed
  - Spark transformations
  - SQL aggregations
  - Joining datasets
  - Applying business rules

 5. 


