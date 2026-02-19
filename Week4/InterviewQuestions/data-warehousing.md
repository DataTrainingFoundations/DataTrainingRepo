# Unit: Data Warehousing


* How does a Data Warehouse compare with a Data Lake?
  * **Data Warehouse**:
    * **Structured Data**: Data warehouses are optimized for storing structured and preprocessed data in a schema-on-write format. They typically use relational database management systems (RDBMS) and structured query language (SQL) for data storage, management, and analysis.
    * **Purpose**: Data warehouses are designed for supporting business intelligence (BI), reporting, and decision-making processes. They are ideal for structured, transactional data from operational systems, such as sales transactions, customer interactions, and financial records.
    * **Schema Design**: Data warehouses typically use dimensional modeling techniques, such as star schemas or snowflake schemas, to organize data for efficient querying and analysis.
    * **Processing**: Data in a data warehouse is often cleansed, transformed, and aggregated before being loaded into the warehouse. Queries in a data warehouse are typically optimized for analytical workloads and involve complex aggregations and joins.

  * **Data Lake**:
    * **Flexible Data Storage**: Data lakes are designed for storing raw, unstructured, semi-structured, and structured data in its native format. They use distributed file systems, such as Apache Hadoop or cloud object storage, to store large volumes of data economically.
    * **Purpose**: Data lakes are used for storing diverse types of data, including logs, sensor data, social media feeds, and documents. They are ideal for exploratory data analysis, data science, machine learning, and advanced analytics.
    * **Schema-on-Read**: Data lakes employ a schema-on-read approach, where data is stored first and its structure is applied when it's read. This allows for greater flexibility and agility in data exploration and analysis.
    * **Processing**: Data in a data lake is processed and transformed as needed during analysis. Tools like Apache Spark, Apache Flink, or cloud-based services are often used for processing data in a data lake. Queries may involve a mix of SQL, batch processing, stream processing, and machine learning algorithms.

  * **Comparison**:
    * **Data Structure**: Data warehouses primarily store structured data, while data lakes can store structured, unstructured, and semi-structured data.
    * **Schema Design**: Data warehouses use predefined schemas optimized for analytics, while data lakes have a flexible schema-on-read approach.
    * **Processing**: Data warehouses preprocess data before storage and optimize queries for analytics, while data lakes process data on-the-fly during analysis with a variety of tools and frameworks.
    * **Use Cases**: Data warehouses are suited for structured data and business intelligence, while data lakes are used for storing diverse data types and supporting exploratory analytics and data science.

* What is dimensional modelling?
  * A technique used in data warehousing to organize and structure data for efficient querying and analysis. It involves designing a data model that represents business processes, measures, and dimensions in a way that is intuitive and optimized for analytical purposes. Dimensional modeling is commonly associated with star schemas and snowflake schemas.
    * **Fact Table**: The central table in a dimensional model, which contains quantitative measures or metrics that represent business events or transactions. Examples of measures include sales revenue, units sold, or customer counts.
    * **Dimension Tables**: Tables that contain descriptive attributes that provide context to the measures in the fact table. Dimensions represent the who, what, when, where, and how aspects of the business. Examples of dimensions include customer, product, time, geography, and sales channel.
    * **Star Schema**: A dimensional modeling technique where dimension tables are directly connected to a single fact table. The relationships between the fact table and dimension tables form a star-like structure, with the fact table at the center and dimension tables radiating out from it.
    * **Snowflake Schema**: A dimensional modeling technique where dimension tables are normalized into multiple related tables. This results in a snowflake-like structure with additional levels of hierarchy in the dimension tables. Snowflake schemas reduce data redundancy but may require more complex query logic compared to star schemas.
  * Benefits of dimensional modeling include:
    * **Simplicity**: Dimensional models are intuitive and easy to understand for business users, as they closely align with how people think about and analyze data.
    * **Query Performance**: Dimensional models are optimized for analytical queries, enabling fast query performance even on large datasets.
    * **Flexibility**: Dimensional models can easily accommodate changes in business requirements and evolving analytical needs.

* What is the difference between OLTP and OLAP?
  * **OLTP (Online Transaction Processing)**:
    * OLTP systems are designed for transactional workloads that involve capturing, storing, and processing high volumes of transactional data in real-time.
    * They are optimized for handling short, atomic transactions, such as inserting, updating, or deleting individual records in a database.
    * OLTP databases typically have normalized data schemas to minimize redundancy and ensure data consistency.
    * Examples of OLTP applications include e-commerce websites, banking systems, airline reservations systems, and point-of-sale systems.
  * **OLAP (Online Analytical Processing)**:
    * OLAP systems are designed for analytical workloads that involve querying and analyzing large volumes of historical data to support decision-making and business intelligence.
    * They are optimized for complex queries, aggregations, and multidimensional analysis to uncover insights and trends in the data.
    * OLAP databases typically have denormalized or dimensional data schemas, such as star schemas or snowflake schemas, to optimize query performance.
    * Examples of OLAP applications include data warehousing, business reporting, executive dashboards, and data mining.

* Explain star or snowflake schemas. What is the use case for them?
  * Star and snowflake schemas are both types of dimensional modeling techniques used in data warehousing to organize data for efficient querying and analysis.
    * **Star Schema**:
      * In a star schema, data is organized into a central fact table surrounded by dimension tables.
      * The fact table contains numerical measures or metrics, such as sales revenue or quantities sold, and foreign key references to related dimension tables.
      * Dimension tables contain descriptive attributes that provide context to the measures in the fact table. For example, in a sales database, dimension tables might include information about products, customers, time periods, and locations.
      * The relationships between the fact table and dimension tables form a star-like structure, with the fact table at the center and dimension tables radiating out from it.
      * Star schemas are denormalized, meaning that each dimension table is fully denormalized, containing all relevant attributes, to optimize query performance and simplify data retrieval.
    * **Snowflake Schema**:
      * A snowflake schema is similar to a star schema but differs in how dimension tables are structured.
      * In a snowflake schema, dimension tables are normalized, meaning that they are broken down into multiple related tables, forming a snowflake-like structure.
      * For example, a dimension table for products might be broken down into separate tables for product categories, subcategories, and attributes.
      * While snowflake schemas reduce data redundancy and storage requirements compared to star schemas, they can result in more complex query logic and potentially slower query performance due to the need to join multiple tables.
    * **Use Cases**:
      * **Star Schema Use Case**: Star schemas are commonly used in data warehousing for business intelligence and reporting applications where query performance is critical. They are well-suited for ad-hoc querying and analysis of large volumes of historical data.
      * **Snowflake Schema Use Case**: Snowflake schemas are used when there is a need to conserve storage space and reduce data redundancy, such as in scenarios with limited storage capacity or where data normalization is preferred for data integrity reasons. However, snowflake schemas may require more effort to query and maintain due to their normalized structure.

* What are some data warehousing best practices?
  * **Define Clear Objectives**: Clearly define the objectives and goals of your data warehousing initiative. Understand what business problems you are trying to solve and how the data warehouse will support decision-making processes.
  * **Data Modeling**: Invest time in designing a robust data model that reflects the business requirements and ensures data integrity. Use dimensional modeling techniques such as star schema or snowflake schema for optimal query performance and ease of use.
  * **Data Quality Assurance**: Implement processes for data quality assurance to ensure that the data stored in the warehouse is accurate, complete, and consistent. This may involve data profiling, cleansing, validation, and monitoring.
  * **ETL/ELT Processes**: Develop efficient Extract, Transform, and Load (ETL) or Extract, Load, and Transform (ELT) processes to ingest data from source systems into the data warehouse. Consider factors such as data volume, frequency of updates, and performance requirements when designing these processes.
  * **Scalability and Performance**: Design the data warehouse architecture for scalability and performance to handle increasing data volumes and user concurrency. Consider factors such as hardware resources, indexing strategies, partitioning, and caching mechanisms.
  * **Security and Compliance**: Implement robust security measures to protect sensitive data stored in the data warehouse. Define access controls, encryption mechanisms, and auditing processes to ensure data security and compliance with regulatory requirements such as GDPR, HIPAA, or PCI DSS.
  * **Documentation and Metadata Management**: Maintain comprehensive documentation and metadata about the data warehouse objects, including data models, ETL processes, business rules, and data lineage. This helps in understanding and maintaining the data warehouse over time.
  * **Monitoring and Performance Tuning**: Implement monitoring tools and processes to track the performance and health of the data warehouse. Monitor key metrics such as query execution times, resource utilization, and data loads to identify bottlenecks and optimize performance.
  * **User Training and Support**: Provide training and support to users who will be accessing and analyzing data from the data warehouse. Ensure that users understand how to use the data warehouse tools and query languages effectively to derive insights and make informed decisions.
  * **Iterative Development and Continuous Improvement**: Treat data warehousing as an iterative process and continuously improve the data model, ETL processes, and analytical capabilities based on user feedback and changing business requirements.

* What is a slowly changing dimension (SCD)? What are some types?
  * Slowly Changing Dimensions (SCDs) are techniques used in data warehousing to manage changes to dimension data over time. Some examples:
    * Overwriting old data, no historical data maintained
    * Adding a new row with each change to the attribute / dimension
    * Using a separate table to track changes to a dimension

* How would you define conceptual, logical, and physical data models? What are the primary differences among them?
  * Conceptual: High-level view of the business entities and relationships. No technical detail.
  * Logical: Adds structure — includes entity types, attributes, and relationships but still platform-agnostic.
  * Physical: Includes tables, columns, data types, indexing — tailored to the specific database system.
  * Differences lie in abstraction level and technical detail.

* What are some data store or data warehouse vendors?
  * **Data Warehousing**:
    * Snowflake
    * Amazon Redshift
    * Google BigQuery
    * Microsoft Azure Synapse Analytics
  * **Key-Value Stores**:
    * Redis
    * Amazon DynamoDB
    * Apache Cassandra
    * Riak
  * **Column-Family Stores**:
    * Apache Cassandra
    * ScyllaDB
    * HBase
    * Amazon Keyspaces (for Apache Cassandra)
  * **Graph Databases**:
    * Neo4j
    * Amazon Neptune
    * TigerGraph
    * JanusGraph
  * **Time-Series Databases**:
    * InfluxDB
    * Prometheus
    * Amazon Timestream
    * TimescaleDB
  * **NewSQL Databases**:
    * CockroachDB
    * NuoDB
    * Google Spanner

* What are the key differences between cloud-based and on-premises data warehouses with regard to scalability, cost, and maintenance?
  * Scalability: Cloud offers on-demand, nearly infinite scalability; on-prem is limited by hardware.
  * Cost: Cloud is OPEX (pay-as-you-go), on-prem is CAPEX (upfront investment + maintenance).
  * Maintenance: Cloud providers manage updates and availability; on-prem requires in-house teams.

* What is the purpose of a staging area in an ETL pipeline, and how does it impact performance and data integrity?
  * Purpose: Temporary storage for raw data before transformation.
  * Impact: Enables error handling, data validation, deduplication, and better control over loads, improving data quality and recovery processes.

* What is the role of an Operational Data Store (ODS) in ETL, and how does it differ from a data warehouse?
  * ODS holds current, integrated data from multiple sources for operational reporting.
  * It is updated frequently and supports near real-time queries.
  * Unlike a DWH, ODS is not optimized for historical analysis but for day-to-day operations.

## Scenario Based Questions

* You are designing a dimensional model for customer data and need to handle changes over time. For each of the following scenarios, identify the most appropriate Slowly Changing Dimension (SCD) type to use and explain your reasoning:
- A: The business requires a complete history of changes to customer addresses for accurate historical reporting.
- B: Only the most recent customer status (e.g. active, inactive) is needed for reporting; historical changes are irrelevant.
- C:  There is a need to retain both the current and immediately previous values of a customer's loyalty level within the same record for comparison.

  * A. SCD Type 2 – This type is suitable because it preserves history by adding a new row for each change, often using surrogate keys, effective dates, or version numbers.
  * B. SCD Type 1 – Overwrites the existing value without maintaining history, which is appropriate when only the latest status is required.
  * C. SCD Type 3 – Maintains limited history by storing current and previous values in separate columns within the same record, ideal for comparing recent changes.  

### Challenge Questions 
* Describe all types (0-6) of slowly changing dimensions
  * Slowly Changing Dimensions (SCDs) are techniques used in data warehousing to manage changes to dimension data over time. There are several types of SCDs, commonly numbered from 0 to 6, each addressing different scenarios:
    1. **Type 0**: In this type, dimension attributes never change. It's suitable for constant values that never need to be updated.
        * Example: *Date of Birth*

    2. **Type 1**: Type 1 SCDs overwrite old data with new data. Historical information is not preserved, as the dimension is updated with the latest values. It's simple to implement but doesn't maintain historical data.
        * Example: *Current Location* (looking up a company's location - we would only care about the current value)

    3. **Type 2**: This type maintains a new row for each change to a dimension attribute. It keeps track of historical data by creating a new record with a new surrogate key for each change, along with a validity period. This allows for historical analysis but can result in a large dimension table.
        * Example: *Location* (use a 'version' column or 'start date'/'end date' columns)

    4. **Type 3**: In Type 3 SCDs, only some attributes are stored historically, typically just a few key attributes. It involves adding new columns to the dimension to store historical values for selected attributes. It's less common due to limited historical data storage.
        * Example: *Original_Location* and *Current_Location* (only tracks original and current state)

    5. **Type 4**: Type 4 SCDs involve creating separate dimension tables for historical and current data. The current dimension table is linked to the historical table, allowing for faster performance when querying current data.
        * Example: adding a separate *Company_Location* table which stores the location history

    6. **Type 5**: This type combines aspects of Type 1 and Type 2 SCDs. It maintains current data in the main dimension table while using a separate history table to store changes. It's complex to implement but provides both current and historical data.

    7. **Type 6**: Also known as "Hybrid SCD", Type 6 combines Type 1, Type 2, and sometimes Type 3 techniques. It maintains both current and historical data directly in the main dimension table while also storing some historical attributes separately. This approach aims to balance simplicity and historical tracking.

* What are measures in a data warehouse context? How are they different from dimensions?
  * Measures are numeric values to be aggregated or analyzed (e.g. revenue, quantity sold).
  * Dimensions are descriptive attributes used to slice and filter the data (e.g. region, time, product category).
