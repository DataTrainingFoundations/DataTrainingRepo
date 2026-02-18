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

    Examples
  - Spark transformations
  - SQL aggregations
  - Joining datasets
  - Applying business rules

 5. Data Analysis / Consumption
 Data is used for decision-making
  
    Examples
  - Dashboards (Power Bi, Tableau)
  - Machine Learning Models
  - Reports
  - APIs serving processed data

 6. Data ARchival
 Move infrequently used data to cheaper storage.

 7. Data Retention & Deletion
 Data is retained per policy and eventually removed.

### Summary of Data Lifecycle
 Creation -> Ingestion -> Storage -> Processing -> Consumption -> Archival -> Deletion


## OLTP vs OLAP

## WHat is OLTP?
- Online Transaction Processing
    - Real-time transactions
    - Banking apps
    - E-commerce checkout
    - order entry systems
    - all implemented with SQL, and transactions
    - data is typically normalized

## What is OLAP?
- Online Analytical Processing
    - Complex analytical queries 
    - implemented with Data warehousing
    - BI dashboards
    - Reporting Systems
    - data is typically denormalized for optimal analysis

## Lifecycle Comparison 

|Stage          | OLTP                | OLAP                  |
|---------------|---------------------|-----------------------|
|Creation       |Primary source of transactions| Rare         |
|Ingestion      |App Inserts/updates  | Receives data from OLTP|
|Storage        |Normalized, row-based| denormalized, columnar |
|Processing     |Small transaction logic |Heavy aggregation|
|Consumption    |Operational Lookups  |Dashboards, ML         |
|Archival       |Limited Retetion     | Long-term historical  |
|Deletion       |Operational Cleanup  | Compliance-based      |
