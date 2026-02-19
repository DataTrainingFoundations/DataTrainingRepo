# Unit: BigQuery

* **What is OLTP?**
  * Keywords, concepts, or topics that should be in the response:
    * OnLine Transaction Processing.
    * RDBMS (Relational Database Management Systems).  
    * Contain homogeneous data, usually normalized till 3NF.
    * Databases fill up quickly, data needs to be sent somewhere else (Data Warehouses)
    * They contain current, transactional data.
    * Examples: Oracle, MySQL, Postgres, DB2, SQL Server, IBM Informix"

* **What is OLAP?**
  * Keywords, concepts, or topics that should be in the response:
    * OnLine Analytical Processing
    * A form of decision support statement (DSS).
    * Generates a pre-prepared report based on data from DWH
    * Report can be written summary, or visuals can be sent like charts, dashboard, etc.
    * Examples: Sap Business Objects, IBM Cognos, MicroStrategy, QlikView, Tableau

* **What is a Data Warehouse?**
  * Keywords, concepts, or topics that should be in the response:
    * Stores historical data from OLTP databases periodically
    * Stores for Reports, Queries, Analysis, Business decisions, Analytics
    * Data in DWH is stored within a slowly changing dimension (SCD) [ETL should cleanse and summarize data before coming in here).
    * Examples: Teradata (NCR), Exadata (Oracle), Vertica, Netezza, Greenplum

* **What is the standard structure of tables in a Data Warehouse?**
  * Keywords, concepts, or topics that should be in the response:
    * Star Schema. Should have a center Fact Table which contains Key Performance Indicators (KPI) and foreign keys to Dimension tables (specific summarized data holders).
    * This helps reporting tools to perform reports in a fast manner without complex queries.

* **What is ETL?**
  * Keywords, concepts, or topics that should be in the response:
    * Extract-Transform-Load where data from the OLTP databases are extracted, transformed into either a summary of the data or the summary and an inclusion of more detailed information regarding the data, then loaded into the DWH.
    * Examples: Informatica, DataStage, SSIS, Abnitio, Oracle Data Integrator (ODI)

* **What is a Staging Database?**
  * Keywords, concepts, or topics that should be in the response:
    * Before entering DWH, data is quality checked in the “Staging Area”, otherwise known as Operational Data Store (ODS)
    * Quality checking also known as “Data Cleansing” Includes removing trailing spaces, checking proper value of “gender” (M or F, nothing else), filtering out unnecessary data (“Mr.” from “Mr. Ram”)

* **What is a Data Mart?**
  * Keywords, concepts, or topics that should be in the response:
    * Data Warehouse cannot with hold the entirity of historical data. The standard maximum should be 20 years. After 20 years, data can be split into smaller databases called DataMarts, which hold 5 years ~ 10 years data. These periodically receive select portions of the DWH that reflect business data.

* **What kind of data do we have available?**
  * Keywords, concepts, or topics that should be in the response:
    * `Structured Data`
      * Defined Format (like RDBMS)
    * `Semi-structured Data`
      * XML, Email, Excel Spreadsheet has an apparent pattern, enabling analysis
    * `Quasi-structured Data`
      * Erratic format that can be formatted with tools
    * Clickstream Data
    * `Unstructured Data`
      * No inherent structure
      * Text Documents, PDFs, image, videos

* **Define  BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery is a big data analytics web service that runs in the cloud and is designed to process very massive read-only data collections. It is a fully managed, serverless data warehouse that enables petabyte-scale data processing. BigQuery's serverless architecture allows you to perform SQL queries to resolve your business's most pressing issues. Using BigQuery's distributed analytical engine, you may query terabytes in seconds and petabytes in minutes.

* **Explain the architecture of BigQuery.**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery architecture consists of the majority of 4 parts. They are
      * `Dremel`  
        * It makes creating execution trees from SQL queries much easier.
      * `Colossus`
        * It enables columnar storage and comes equipped with a compression mechanism, both of which are beneficial for data storage.
      * `Jupiter`
        * It is helpful because it improves the CPUs and storage connection.
      * `Borg`
        * It contributes to the regulation of error tolerance for the processing power of Dremel jobs.

* **What are the benefits of BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery benefits include:
      * BigQuery's Storage API makes it possible to read Spark and Beam workloads, which is a big assist for integration.
      * BigQuery reduces the need to rewrite the code by supporting the standard SQL Dialect.
              Data can be replicated using BigQuery, and a seven-day history of changes can be kept to aid restoration and comparison.

* **How data can be loaded into BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery Data Transfer Service is the tool that should be utilized for the most successful loading of data into BigQuery. we will be able to swiftly and efficiently import data into BigQuery from various sources, including other services offered by the Google Cloud Platform.BigQuery supports multiple input formats when receiving data.  
    * BigQuery's web-based user interface is another option for transferring data files. In addition to importing data from a local file or a Google Cloud Storage bucket, the BigQuery command-line tool can do the same for a Google Cloud Datastore bucket. BigQuery's application programming interface (API) then lets you import records from numerous sources.

* **What is BigQuery Storage?**
  * Keywords, concepts, or topics that should be in the response:
    * Data can be represented in BigQuery Storage using rows, columns, and tables, and the columnar Storage format, which is optimized for analytical queries, can be used to store the data. BigQuery Storage also assists with storing the data. It supplies comprehensive assistance for database transaction semantics (ACID). It is possible to replicate it across many sites to provide high availability.


* **How to access BigQuery once it is configured?**
  * Keywords, concepts, or topics that should be in the response:
    * Once BigQuery has been configured, it can be accessed in several ways.
    * Most users access BigQuery via the Google Cloud Console, a web-based administration and data analysis interface.
    * We can use the BigQuery command-line tool, which lets you communicate with BigQuery via the command line and issue queries.
    * BigQuery may be integrated with various third-party tools that offer additional features and capabilities.

* **What are views in BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * We can use the command line interface (CLI), the BigQuery online UI, or the API to accomplish this. Before developing a view, we will need first to make a dataset and can generate a view after that dataset has been created.

* **Differentiate BigQuery and SQL?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery is a cloud-based architecture that offers remarkable performance due to its ability to auto-scale up and down depending on the amount of data load and rapidly perform data analysis.  
    * SQL Server employs a client-server architecture and, unless the user scales it manually, maintains a constant level of performance throughout the system.

* **Explain the working of BigQuery columnar database?**
  * Keywords, concepts, or topics that should be in the response:
    * A database that organizes its data into columns instead of rows is known as a columnar database. BigQuery is a columnar database that contains data in columns rather than rows, like traditional relational databases do and because of this, it is an excellent choice for storing massive volumes of data and conducting queries on that data.

* **What are the features of  BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * The BigQuery features  includes:
    * `BigQuery Omni`
      * It's a multi-cloud analytics solution that's fully managed, so we can use it to perform analyses across AWS and Azure, for example.
    * `BigQuery ML`
      * It makes it possible for all data analysts to construct and operationalize machine learning models on structured or semi-structured data at planet size directly inside BigQuery, using simple SQL and doing so in a fraction of the time previously required.
    * `BigQuery GIS`
      * It is utilized to connect the serverless architecture of BigQuery with the native support for geospatial analysis, which enables you to enhance your analytics processes with location intelligence.
    * `BigQuery BI Engine`
      * It is used in the analyzing service created in BigQuery, enabling users to interactively examine huge and complicated datasets with a query response time of less than one second and high concurrency.

* **How do you fix the most common SQL errors in BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * We have to check that the Query follows the proper syntax using the Query Validator. If you try to run a query that already has errors, the attempt will fail, and the error will be logged in the Job details. The query validator will show a tick in the green box whenever there are no problems with the Query. Click the Run button to execute the Query and see the results after the checkmark appears in the green box.

* **Explain what makes legacy SQL different from standard SQL?**
  * Keywords, concepts, or topics that should be in the response:
    * Using standard SQL to query data in BigQuery is the most up-to-date and recommended way. The SQL:2011 standard, on which it is based, provides numerous enhancements over older versions of the language. Performance enhancements, more assistance for SQL standard features, and enhanced compatibility with other SQL-based systems are only some of how this has been enhanced.  
    * Legacy SQL is a way of querying data in BigQuery that predates the SQL:2003 standard. While traditional SQL is still supported for compatibility reasons, it is strongly recommended that you use more modern forms of the language whenever possible.

* **What kinds of reports can be generated using BigQuery data?**
  * Keywords, concepts, or topics that should be in the response:
    * We can generate the following reports using BigQuery:
      * Inventory reports
      * Marketing reports
      * Sales reports
      * Product reports
      * Customer reports
      * Financial reports

* **How can I get into the BigQuery Cloud Data Warehouse?**
  * Keywords, concepts, or topics that should be in the response:
    * The following are methods for connecting to the BigQuery Cloud Data Warehouse:
      * ODBC Drivers
      * Web User Interface
      * JDBC Drivers
      * Python Libraries
      * BQ Command-line Client

* **What is a Big Query time decorator?**
  * Keywords, concepts, or topics that should be in the response:
    * Time decorators in Big Query enables access to historical data. For instance, if you accidentally deleted a table an hour ago, you may still retrieve the data from the table using a time decorator.

* **How much information can BigQuery deal with?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery was explicitly developed to manage massive data collections. It can store up to 10 petabytes of data and can analyze up to 100 terabytes of data every single day.

* **How to permit sharing data and queries with the public in BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * We can publicize your searches and data on Google BigQuery. We can implement this by launching a project, discussing it with specific people, or making it available to the general public.

* **Is BigQuery PaaS or SAAS?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery is a fully managed serverless data warehouse that supports scalable analysis of data sets up to several petabytes in size. A cloud computing environment that supports ANSI SQL queries.

* **Is BigQuery an OLAP or OLTP?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery is a solution for OLAP, which stands for online analytical processing.  
    * BigQuery is best suited for large workloads, such as regular OLAP reporting and archiving activities. It is because query latency is significant in BigQuery. BigQuery's architecture discourages OLTP-style queries.

* **Is BigQuery an ETL tool?**
  * Keywords, concepts, or topics that should be in the response:
    * Yes, BigQuery is the best ETL software solutions for businesses that want to manage their data from various sources and get the most out of their data insights. These businesses aim to gain as much as they can from their data.

* **Why is BigQuery faster than SQL?**
  * Keywords, concepts, or topics that should be in the response:
    * The query engine can process petabyte-scale data using standard SQL queries in seconds, and terabyte-scale data takes only minutes. BigQuery delivers tremendous efficiency with no requirement for index creation, infrastructure maintenance, or rebuilding. Because of its speed and scalability, BigQuery is well-suited for processing massive datasets.

* **Why does BigQuery use SQL?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery supports the Google Standard SQL dialect. If you are unfamiliar with BigQuery, you should start with Google Standard SQL because it has the most comprehensive features. For instance, features such as DDL and DML statements are only supported when using Google Standard SQL.

* **Why BigQuery needs a schema?**
  * Keywords, concepts, or topics that should be in the response:
    * When creating an empty table or loading data into an existing one, BigQuery allows you to choose the table's schema. On the other hand, you can utilize schema auto-detection to find out what file formats can be used to store your data.

* **What type of storage is BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery's data storage is a fully managed service. No need to set aside storage space or reserve a certain amount of storage capacity. When you upload data to BigQuery, the service immediately begins allocating storage space. Only the space you actually use will be charged to you.

* **BigQuery structured or unstructured data?Discuss?**
  * Keywords, concepts, or topics that should be in the response:
    * BigQuery is intended for typical SQL queries on structured and semi-structured data. It is extremely cost-effective and highly optimized for query performance. BigQuery is a fully managed cloud service; therefore, there is no operational overhead.

* **An analytics company handles data processing for different clients. Clients use their own suite of analytics tools. Some clients have allowed direct query access via Google Big Query. You want to ensure that clients cannot see each other’s data. What steps can you perform inside Big Query to ensure the data security of clients?**
  * Keywords, concepts, or topics that should be in the response:
    * To ensure that clients could not see each other’s data, the following steps could be taken:
    * For each client, load data into a different dataset.
    * Restrict a client’s dataset such that only approved users can access their dataset
    * For further security, use the relevant identity and access management (IAM) roles for each client’s users.

## Scenario Questions

* **You have a large dataset in Google BigQuery, and you need to share summarized insights with your team. Instead of sharing the entire dataset, you want to create a dashboard that provides an overview of key metrics. How would you approach creating a dashboard with summarized data from BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * `Define Key Metrics`: Identify the key metrics or insights you want to showcase in the dashboard. These could include aggregations, trends, or comparisons that provide meaningful information to your team.
    * `Write SQL Queries`: Write SQL queries that aggregate and summarize the data to obtain the key metrics. For example, you might calculate total sales, average order value, or the number of new customers.
        `SELECT EXTRACT(MONTH FROM order_date) AS month, COUNT(DISTINCT customer_id) AS new_customers, SUM(order_amount) AS total_sales FROM my_dataset.my_table WHERE EXTRACT(YEAR FROM order_date) = 2023 GROUP BY month`
    * `Save Query Results or Views`: Save the results of your SQL queries to new tables or create views for easier reference. This can be useful if you want to reuse these summarized datasets in multiple dashboards.
        `CREATE TABLE my_dataset.dashboard_metrics AS SELECT EXTRACT(MONTH FROM order_date) AS month,COUNT(DISTINCT customer_id) AS new_customers, SUM(order_amount) AS total_sales FROM my_dataset.my_table WHERE EXTRACT(YEAR FROM order_date) = 2023 GROUP BY month`
    * `Choose a Dashboard Tool`: Select a dashboarding tool that integrates well with BigQuery. Google Data Studio is a common choice, but other tools like Tableau, Looker, or Power BI also work well. Connect the dashboard tool to your BigQuery project.
    * `Create Visualizations`: Use the dashboard tool to create visualizations based on the summarized data. You can create charts, graphs, tables, and other visual elements to represent the key metrics effectively.
    * `Configure Data Refresh`: Configure the dashboard tool to periodically refresh the data from BigQuery. This ensures that the dashboard reflects the latest information without manual intervention.
    * `Share Dashboard`: Share the dashboard with your team members by providing them with the necessary access permissions or sharing links. Consider setting up scheduled email updates or publishing the dashboard to a shared space.
    * `Monitor and Iterate`: Monitor the usage of the dashboard and gather feedback from your team. Iterate on the dashboard design and content based on user feedback and changing business requirements.

### Challenge Questions

* **What is Sharding?**
  * Keywords, concepts, or topics that should be in the response:
    * Sharding is the process of breaking data into smaller pieces so that it can be handled and managed more quickly and easily. When working with BigQuery, sharding, which is the process of dividing the data across multiple processors, can be used to speed things up overall.

* **Why we have to use Google Cloud Storage as a secondary storage layer when loading data into BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * Google Cloud Storage is utilized as an intermediary storage layer to import data into BigQuery because of the reasonable pricing of the cloud data storage that it provides. we can significantly reduce the high expenses associated with cloud storage if you use Google Cloud Storage rather than one of the many other cloud storage providers.

* **How many slots does BigQuery have?**
  * Keywords, concepts, or topics that should be in the response:
    * It Depends on the size and complexity of each query, BigQuery determines how many slots are needed. At each level of the query, separate units of work are carried out by BigQuery slots. For a certain step of a query, BigQuery can ask for an unlimited number of slots. For example, If BigQuery finds that the best parallelization factor for a stage is 10, it asks 10 slots to process that stage.

* **A client provides your company with a daily dump of data that flows into Google Cloud Storage as CSV files. How would you build a pipeline that will analyze the data stored in Google Cloud Storage in the Google Big Query when the data may contain rows which are formatted incorrectly or corrupted?**
  * Keywords, concepts, or topics that should be in the response:
    * To build a pipeline for the above scenario follow the below steps:
      * Import the data from Google Cloud Storage to the Big Query by running Google Cloud Dataflow.
      * Push the corrupted rows to another dead-letter table for analysis.

* **You work as an analyst in an e-commerce company. You use Google Big Query to correlate the customer data with the average prices of the 40 most common products sold, including laptops, mobile phones, television, etc. After every 25 minutes, the average prices of these goods are updated. What steps you should follow to ensure that this average price data stays up to date so that you can easily combine it with other data in Big Query as cheaply as possible?**
  * Keywords, concepts, or topics that should be in the response:
    * Follow the below steps to ensure that this average price data stays up to date so that you can easily combine it with other data in Big Query as cheaply as possible:
      * Create a regional Google Cloud Storage Bucket to store and update the average price data
      * Then, use the Cloud Storage Bucket as a federated data source in Big Query.

* **Your data team is building a new real-time data warehouse for a client. The client wants to use Google Big Query for performing streaming inserts. You get a unique ID and an event timestamp whenever data gets inserted in the row but it is not guaranteed that data will only be sent in once. Which clauses and functions you will use to write a query which ensures that duplicates are not included while interactively querying data?**
  * Keywords, concepts, or topics that should be in the response:
    * To ensure that duplicates are not included, use the ROW_NUMBER window function with PARTITION BY based on unique ID WHERE row equals to1.

## Scenario Questions

[Back to top](#unit-bigquery)

* **You are working on a project where you have a large dataset in Google Cloud Storage, and you need to perform complex analytical queries on this data. The dataset is too large to process locally, and you want to leverage the scalability of Google BigQuery. How would you approach loading the data into BigQuery and running analytical queries?**
  * Keywords, concepts, or topics that should be in the response:
    * `Load Data into BigQuery`: Upload the dataset from Google Cloud Storage to BigQuery. You can use the bq command-line tool, the web UI, or the BigQuery API for this task. The bq load command allows you to load data from Cloud Storage into a BigQuery table.
        bq load --source_format=CSV my_dataset.my_table gs://path/to/data.csv
    * `Schema Definition`: Ensure that you define the schema of your table accurately, specifying the data types for each column. This helps BigQuery optimize query performance.
    * `Partitioning and Clustering`: The partitioning and clustering your table to improve query performance. Partitioning is useful for date-based or numeric columns, while clustering can help organize data based on a specific column, reducing the amount of data scanned during queries.
        `CREATE TABLE my_dataset.my_table PARTITION BY DATE(_PARTITIONTIME)`
        `CREATE TABLE my_dataset.my_table CLUSTER BY column_name`
    * `Use Standard SQL`: Write your analytical queries using Standard SQL. BigQuery supports both Legacy SQL and Standard SQL, but Standard SQL offers more features and is recommended for new projects.
    * `Leverage BigQuery's SQL Capabilities`: Take advantage of BigQuery's powerful SQL capabilities, including window functions, analytical functions, and support for nested and repeated fields. These features can simplify and enhance your analytical queries.
    * `Optimize Query Performance`: Optimize your queries for performance by using appropriate JOIN strategies, choosing the right data types, and avoiding unnecessary subqueries. Utilize the "Query History" feature in the BigQuery Console to review and optimize query execution times.
    * `Save Query Results`: If you need to save the results of a query, you can create a new table or export the results to Google Cloud Storage. This is useful for sharing or further analysis.
        `CREATE TABLE my_dataset.query_results AS SELECT * FROM my_dataset.my_table WHERE condition;`

* **Your company collects large amounts of streaming data, and you need to perform real-time analytics on this data using Google BigQuery. How would you set up and manage real-time streaming data processing in BigQuery?**
  * Keywords, concepts, or topics that should be in the response:
    * `Configure Data Streaming`: Ensure that your streaming data source is configured to send data to BigQuery in real-time. Google Cloud provides services like Cloud Pub/Sub for handling streaming data. Configure the streaming source to publish data to a Cloud Pub/Sub topic.
    * `Create a BigQuery Dataset and Table`: In the BigQuery Console, create a dataset to store your streaming data. Within the dataset, create a table that will receive the real-time streaming data. Enable the streaming option for the table.
    * `Define Schema`: Define the schema of your streaming table, specifying the data types for each field. The schema should match the structure of the incoming streaming data.
    * `Set Up Cloud Pub/Sub Subscription`: Create a subscription for the Cloud Pub/Sub topic that receives the streaming data. This subscription acts as a bridge between Cloud Pub/Sub and BigQuery, delivering the data in real-time.
    * `Write Streaming Inserts`: Modify your streaming data source to send data to the Cloud Pub/Sub topic. Ensure that the data is in JSON format and matches the schema defined in BigQuery. The data will be streamed in real-time from Cloud Pub/Sub to BigQuery.
    * `Monitor Streaming Inserts`: Use BigQuery's real-time monitoring tools to check the status of streaming inserts. You can monitor the number of rows streamed, the lag between the data arriving in Cloud Pub/Sub and being available in BigQuery, and other metrics.
    * `Write Real-Time Analytical Queries`: Write SQL queries in BigQuery to perform real-time analytical processing on the streaming data. For example, you can calculate rolling averages, detect anomalies, or aggregate data on-the-fly.
    * `Visualize Real-Time Data`: Use a dashboarding tool like Google Data Studio, Tableau, or another visualization tool to create real-time dashboards based on the streaming data. Connect the dashboard tool to BigQuery to visualize insights as they happen.

* **You are working on a collaborative project, and multiple team members need access to a subset of data stored in Google BigQuery. How would you manage access control and permissions to ensure that team members have the necessary access without compromising security?**
  * Keywords, concepts, or topics that should be in the response:
    * `Understand Data Access Requirements`: Collaborate with team members to understand their specific data access requirements. Identify the tables or datasets they need access to and the level of access required (e.g., read-only or read-write).
    * `Organize Data in Datasets`: Organize your data in BigQuery datasets based on logical groupings. For example, you might have datasets for different functional areas or projects.
    * `Grant Dataset-level Permissions`: Grant appropriate dataset-level permissions to team members based on their roles. Assign roles such as READER, WRITER, or OWNER at the dataset level to control access.
        `GRANT ROLE roles/bigquery.dataViewer TO user@example.com;`
    * `Use IAM Roles`: Leverage Identity and Access Management (IAM) roles to manage access at the project level. Assign roles such as BigQuery Data Viewer or BigQuery Data Editor to control access across multiple datasets.
        `GRANT roles/bigquery.dataViewer TO user@example.com;`
    * `Grant Table-level Permissions`: Grant table-level permissions to team members for specific tables within a dataset. This allows for more granular control over data access.
        `GRANT ROLE roles/bigquery.dataViewer TO user@example.com ON my_dataset.my_table;`
    * Use Google Groups for Access Management: Consider creating Google Groups to manage access more efficiently. You can add team members to groups and grant permissions to the entire group, simplifying access management.
        `GRANT ROLE roles/bigquery.dataViewer TO group:your-group@googlegroups.com;`
    * `Regularly Review and Update Permissions`: Periodically review and update permissions based on changes in team composition or project requirements. Ensure that team members have the necessary access and revoke access when it is no longer needed.
    * `Audit Access Logs`: Enable and review BigQuery's audit logs to monitor data access. Audit logs provide information about who accessed the data and what actions were performed, helping to identify and address security concerns.
    * `Train Team Members on Access Control`: Provide training to team members on how to manage and request access. Encourage the use of authorized channels for access requests and updates.

* **You are working on a project that involves analyzing large amounts of historical data stored in Google Cloud Storage. The data is in a CSV format, and you want to leverage Google BigQuery for efficient analysis. How would you go about loading this historical data into BigQuery and optimizing it for analytical queries?**
  * Keywords, concepts, or topics that should be in the response:
    * `Create a BigQuery Dataset`: In the BigQuery Console, create a new dataset to organize the tables related to your project. This provides a logical grouping for your data.
    * `Upload CSV Data to Cloud Storage`: Upload the historical CSV data files to Google Cloud Storage. You can use the Cloud Console, gsutil command-line tool, or the Cloud Storage API for this task.
        `gsutil cp local_data.csv gs://your_bucket/path/to/data.csv`
    * `Load Data into BigQuery`: Use the BigQuery Console or the bq command-line tool to create a new table in BigQuery and load the data from Cloud Storage. Specify the schema and options such as CSV delimiter and header.
        `bq load --autodetect --source_format=CSV my_dataset.my_table gs://your_bucket/path/to/data.csv`
        Alternatively, you can manually define the schema if autodetection is not desired.
    * `Partition and Cluster Tables`: If applicable, consider partitioning your table based on a date or numeric column. This can significantly improve query performance by limiting the amount of data that needs to be scanned.
        `CREATE TABLE my_dataset.my_table PARTITION BY DATE(date_column)`
        `CREATE TABLE my_dataset.my_table CLUSTER BY column_name`
    * `Optimize Query Performance`: Write SQL queries that take advantage of BigQuery's capabilities, such as using partitioned columns in WHERE clauses, minimizing the use of wildcard characters, and leveraging appropriate JOIN strategies.
    * `Schedule Data Refresh`: If the historical data is regularly updated, schedule periodic refreshes of the data in BigQuery. You can automate this process using Cloud Composer, Cloud Scheduler, or other scheduling tools.
    * `Monitor and Optimize Costs`: Monitor your query costs and take advantage of tools like the BigQuery Pricing Calculator. Consider using reservations or flex slots for cost optimization based on your workload.

### IMPORTANCE: Stretch

* **What are BigQuery's Window Functions?**
  * Keywords, concepts, or topics that should be in the response:
    * Functions that aggregate to a single value for a set of rows are called Window functions.They're helpful for computing values over a set of rows and returning just that result.
    * It has three different kinds of functions, such as:
    * `Navigation function`
      * The navigation function returns a value based on a specific location.
    * `Numbering function`
      * Numbering functions are used to give each row a number that is based on where it is in the window.
    * Analytic function: Analytic functions are used to do the math on a set of values.

* **If certain users should only see sales data for their assigned region and only be able to access non-sensitive columns, how would you enforce that in BigQuery?**

  * Implement row-level security policies using CREATE ROW ACCESS POLICY and column-level access control using policy tags or RESTRICTED labels with IAM conditions.
    * look for mentioning aligning policies with business roles, applying multiple policies to a single table, and auditing access to sensitive data.

## Scenario Questions

[Back to top](#unit-bigquery)

* **Imagine you're working with customer churn data and want to predict who might leave next month. How would BigQuery ML help you do that directly within BigQuery?**

  * BigQuery ML lets you train models like logistic regression or boosted trees using simple SQL syntax and store the model as a BigQuery resource.
    * could go further, mentioning the use of CREATE MODEL, ML.TRAIN, ML.PREDICT, and even evaluating models using ML.EVALUATE.

* **You have store locations and customer coordinates. How would you determine the closest store for each customer using BigQuery?**

  * Use BigQuery GIS functions, particularly using ST_Distance, ST_GeogPoint, and potentially ST_ClosestPoint for proximity calculations.
    * thorough answer might describe using spatial joins, understanding the coordinate system (GEOGRAPHY type), and filtering with ST_WITHIN or bounding boxes for efficiency.



