# Snowflake & dbt – Interview Questions & Study Guide

---

## Snowflake (25 Questions)

### Core Concepts

1. What is Snowflake and what problem does it solve?
2. What makes Snowflake different from traditional data warehouses?
3. What is the architecture of Snowflake (Storage, Compute, Cloud Services)?
4. What is a virtual warehouse?
5. What happens when you suspend or resume a warehouse?
6. What is auto-scaling and auto-suspend?
7. What is Snowflake Time Travel?

### Storage & Data Handling

8. What is a micro-partition?
9. How does Snowflake handle partitioning automatically?
10. What is clustering in Snowflake?
11. When would you use a clustering key?
12. What is data pruning?
13. What file formats does Snowflake support for loading data?
14. What is the difference between internal and external stages?

### Data Loading & Pipelines

15. What is Snowpipe?
16. What is the difference between COPY INTO and Snowpipe?
17. What are stages in Snowflake?
18. What is an external stage (e.g., S3, Azure Blob)?
19. How does Snowflake handle semi-structured data (JSON, Avro, Parquet)?
20. What is VARIANT data type?

### Streams, Tasks & Performance

21. What is a Snowflake Stream?
22. What is a Snowflake Task?
23. How do Streams and Tasks work together?
24. How do you monitor query performance in Snowflake?
25. What is result caching and how does it improve performance?

---

## dbt (25 Questions)

### Core Concepts

1. What is dbt and what problem does it solve?
2. How does dbt differ from traditional ETL tools?
3. What does ELT mean in the context of dbt?
4. What is a dbt project?
5. What happens when you run `dbt run`?
6. What is the role of `profiles.yml`?
7. What is the role of `dbt_project.yml`?

### Models & Transformations

8. What is a dbt model?
9. What is the difference between view and table materializations?
10. What is an incremental model?
11. When would you use incremental models?
12. What does `ref()` do in dbt?
13. Why is `ref()` important for dependency management?
14. What is a staging model vs a mart model?

### Testing & Documentation

15. What are dbt tests?
16. What is the difference between generic and singular tests?
17. How do you test for null values in a column?
18. What is a schema.yml file?
19. What is dbt documentation generation (`dbt docs generate`)?
20. What is a source in dbt?

### Advanced Concepts

21. What are macros in dbt?
22. What is Jinja templating in dbt?
23. What are seeds in dbt?
24. What are snapshots in dbt?
25. How does dbt handle environment separation (dev vs prod)?

---

## Quick Definitions

Be prepared to define these terms in one or two sentences:

### Snowflake

- Virtual Warehouse  
- Micro-partition  
- Snowpipe  
- Stream  
- Task  
- Time Travel  
- VARIANT  

### dbt

- Model  
- ref()  
- Materialization  
- Incremental Model  
- Macro  
- Seed  
- Snapshot  
- Source  

---

## Key Topics to Study

### Snowflake

- Architecture (Separation of Compute & Storage)
- Query optimization and caching
- Data loading strategies (batch vs streaming)
- Streams & Tasks (CDC pipelines)
- Semi-structured data handling (JSON)
- Cost optimization (warehouse sizing, auto-suspend)

### dbt

- ELT vs ETL concepts
- Modular data modeling (staging → intermediate → marts)
- Dependency management with `ref()`
- Testing strategy (data quality)
- Incremental processing
- Jinja templating & macros
- Documentation and lineage

---

## Bonus Practical Questions

- How would you design an end-to-end pipeline using Snowflake and dbt?
- How would you handle late-arriving data in dbt?
- How would you optimize a slow Snowflake query?
- How would you implement CDC using Snowflake Streams and Tasks?
- How would you structure a dbt project for a large organization?