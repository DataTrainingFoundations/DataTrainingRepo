# Data Engineering Interview Questions (with Answers)

## Testing & Data Pipelines

### 1. What is the testing pyramid and how does it apply to data engineering?
**Answer:**  
The testing pyramid consists of unit tests, integration tests, and end-to-end tests. In data engineering, it ensures fast feedback and reliable pipelines.

### 2. Why are unit tests important in data pipelines?
**Answer:**  
They validate transformations in isolation and catch logic errors early.

### 3. Give examples of what should be unit tested in data workflows.
**Answer:**  
Python transformation functions, SQL logic, validation rules, and configs.

### 4. What is the difference between integration and end-to-end tests?
**Answer:**  
Integration tests validate component interactions; end-to-end tests validate full pipelines.

### 5. What are schema tests and why are they important?
**Answer:**  
They validate structure like columns and data types to prevent downstream issues.

### 6. What are data quality tests?
**Answer:**  
They check correctness such as nulls, uniqueness, and valid ranges.

### 7. What are freshness tests?
**Answer:**  
They ensure data is up-to-date and meets SLAs.

### 8. What tools are commonly used for data testing?
**Answer:**  
pytest, dbt, Great Expectations, Soda.

### 9. What is the purpose of Great Expectations?
**Answer:**  
To define and validate expectations about data quality.

### 10. Why is end-to-end testing used sparingly?
**Answer:**  
Because it is slow and complex.

## dbt & Data Testing

### 11. What is the difference between dbt schema tests and singular tests?
**Answer:**  
Schema tests are predefined; singular tests are custom SQL queries.

### 12. What are the four built-in dbt schema tests?
**Answer:**  
unique, not_null, accepted_values, relationships.

### 13. How does dbt determine if a test fails?
**Answer:**  
If the test query returns rows, it fails.

### 14. What is a relationships test in dbt?
**Answer:**  
It validates referential integrity.

### 15. Why are dbt tests critical in CI/CD pipelines?
**Answer:**  
They prevent bad data from reaching production.

### 16. What steps are typically included in a dbt CI pipeline?
**Answer:**  
Checkout, install, compile, test, docs.

### 17. What environments are typically used in dbt projects?
**Answer:**  
Dev, CI, staging, production.

## Data Quality

### 18. What are the six dimensions of data quality?
**Answer:**  
Accuracy, completeness, timeliness, consistency, validity, uniqueness.

### 19. Why is data quality important even if pipelines run successfully?
**Answer:**  
Because incorrect data leads to bad decisions.

### 20. Give an example of a data quality issue.
**Answer:**  
Missing purchase data leading to incorrect churn assumptions.

## Data Lineage

### 21. What is data lineage?
**Answer:**  
Tracking data from source to consumption.

### 22. Why is data lineage important?
**Answer:**  
For debugging, compliance, and impact analysis.

### 23. What are different levels of lineage granularity?
**Answer:**  
System, table, column, row.

### 24. How does dbt help with lineage?
**Answer:**  
By generating dependency graphs using ref().

### 25. How does Snowflake track lineage?
**Answer:**  
Through query history and logs.

## Data Governance

### 26. What are the four pillars of data governance?
**Answer:**  
Ownership, security, cataloging, quality.

### 27. What is the difference between a data owner, steward, and custodian?
**Answer:**  
Owner = accountability, Steward = quality, Custodian = technical.

### 28. Why is data governance important?
**Answer:**  
Ensures trust and compliance.

### 29. What is a data catalog?
**Answer:**  
A repository of metadata for discovery.

### 30. How do you measure effective data governance?
**Answer:**  
Using quality scores, metadata completeness, and compliance metrics.

---

# Data Scenario Questions

### Scenario 1: Missing Data in Reports
**Question:**  
A dashboard shows a sudden drop in sales. What steps would you take?

**Answer:**  
Check data freshness, pipeline failures, source data completeness, and transformation logic.

---

### Scenario 2: Duplicate Records
**Question:**  
You notice duplicate customer records. How do you handle this?

**Answer:**  
Identify root cause, apply deduplication logic, enforce uniqueness constraints, and add tests.

---

### Scenario 3: Broken Downstream Table
**Question:**  
A downstream table is failing after a schema change upstream. What do you do?

**Answer:**  
Use lineage to trace dependencies, update schema or transformations, and add schema tests.

---

### Scenario 4: Data Not Updating
**Question:**  
A table hasn’t updated in 24 hours. What’s your approach?

**Answer:**  
Check pipeline scheduling, ingestion processes, logs, and freshness tests.
