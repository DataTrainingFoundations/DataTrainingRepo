# Schema Evolution in PySpark 

## Overview

**Schema evolution** refers to the ability of a dataset's **structure
(schema)** to change over time while still allowing the data to be read
and processed.

In distributed data systems such as **Apache Spark**, data is often
written in **multiple batches over time**. If the structure of the data
changes (for example a new column appears), schema evolution allows
Spark to still read all of the data together.

In **PySpark**, schema evolution commonly occurs when using file formats
like:

-   Parquet
-   ORC
-   JSON
-   Avro

The most common schema evolution feature in Spark is **schema merging**,
where Spark combines different schemas from multiple files.

------------------------------------------------------------------------

# What is a Schema?

A **schema** defines the structure of a dataset:

-   column names
-   data types
-   nested structures

Example schema:

    id: integer
    name: string
    age: integer

If later data adds another column:

    id: integer
    name: string
    age: integer
    country: string

The schema has **evolved**.

------------------------------------------------------------------------

# Why Schema Evolution Happens

Schema evolution is common in real-world pipelines because:

1.  Source systems change
2.  New data fields are added
3.  Logging systems evolve
4.  APIs return new attributes
5.  Data engineers enrich datasets over time

Example timeline:

  Time     Schema
  -------- ------------------------
  Day 1    id, name
  Day 5    id, name, age
  Day 10   id, name, age, country

Without schema evolution, reading all data together would fail.

------------------------------------------------------------------------

# Schema Evolution with Parquet in PySpark

The most common place to see schema evolution is when reading **Parquet
files**.

Parquet stores **schema metadata inside each file**, which allows Spark
to merge schemas across files.

------------------------------------------------------------------------

# Example 1 --- Initial Dataset

Create a Spark session.

``` python
from pyspark.sql import SparkSession

spark = SparkSession.builder     .appName("schema_evolution_example")     .getOrCreate()
```

Create an initial dataset.

``` python
data1 = [
    (1, "Alice"),
    (2, "Bob")
]

df1 = spark.createDataFrame(data1, ["id", "name"])
df1.show()
```

Output:

    +---+-----+
    |id |name |
    +---+-----+
    |1  |Alice|
    |2  |Bob  |
    +---+-----+

Write the data to Parquet.

``` python
df1.write.mode("overwrite").parquet("data/people")
```

Schema stored in the files:

    id: long
    name: string

------------------------------------------------------------------------

# Example 2 --- New Data With Additional Column

Later, a new column appears.

``` python
data2 = [
    (3, "Charlie", 25),
    (4, "Diana", 30)
]

df2 = spark.createDataFrame(data2, ["id", "name", "age"])
df2.show()
```

Output:

    +---+-------+---+
    |id |name   |age|
    +---+-------+---+
    |3  |Charlie|25 |
    |4  |Diana  |30 |
    +---+-------+---+

Append the new data.

``` python
df2.write.mode("append").parquet("data/people")
```

Now the directory contains files with **two different schemas**.

------------------------------------------------------------------------

# Example 3 --- Reading With Schema Merging

To allow schema evolution, enable **schema merging**.

``` python
df = spark.read.option("mergeSchema", "true").parquet("data/people")

df.show()
```

Result:

    +---+-------+----+
    |id |name   |age |
    +---+-------+----+
    |1  |Alice  |null|
    |2  |Bob    |null|
    |3  |Charlie|25  |
    |4  |Diana  |30  |
    +---+-------+----+

Spark automatically merged the schemas.

Old rows simply contain **null values** for the new column.

------------------------------------------------------------------------

# Example 4 --- Viewing the Merged Schema

You can inspect the merged schema.

``` python
df.printSchema()
```

Output:

    root
     |-- id: long
     |-- name: string
     |-- age: long

------------------------------------------------------------------------

# How Schema Merging Works

Spark performs the following steps:

1.  Reads schema metadata from each file
2.  Combines the schemas
3.  Creates a unified schema
4.  Fills missing fields with **null**

Example:

File 1 schema:

    id
    name

File 2 schema:

    id
    name
    age

Merged schema:

    id
    name
    age

------------------------------------------------------------------------

# Example 5 --- Schema Evolution with JSON

Schema evolution can also happen with **semi-structured data like
JSON**.

Example JSON records:

Record 1:

``` json
{"id":1, "name":"Alice"}
```

Record 2:

``` json
{"id":2, "name":"Bob", "age":25}
```

Load JSON in PySpark.

``` python
df = spark.read.json("data/json_records")
df.show()
```

Output:

    +---+-----+----+
    |id |name |age |
    +---+-----+----+
    |1  |Alice|null|
    |2  |Bob  |25  |
    +---+-----+----+

Spark inferred a **merged schema automatically**.

------------------------------------------------------------------------

# Supported Schema Evolution Changes

Common schema evolution changes include:

  Change             Behavior
  ------------------ -----------------------
  Add column         Supported
  Remove column      Old data keeps column
  Add nested field   Supported
  Change datatype    Can cause errors
  Rename column      Treated as new column

------------------------------------------------------------------------

# Schema Evolution vs Schema Inference

### Schema Inference

Spark **automatically detects the schema** from data.

``` python
df = spark.read.json("data/file.json")
```

------------------------------------------------------------------------

### Schema Evolution

Spark **handles schema changes across multiple datasets**.

Example:

    file1: id, name
    file2: id, name, age

Spark merges schemas when reading.

------------------------------------------------------------------------

# Schema Evolution vs Schema Enforcement

### Schema Enforcement

Rejects mismatched data.

Example table schema:

    id INT
    name STRING

If data contains:

    id INT
    name STRING
    age INT

The write may fail.

------------------------------------------------------------------------

### Schema Evolution

Allows the schema to change.

    Old data: id, name
    New data: id, name, age

Spark merges them.

------------------------------------------------------------------------

# Performance Considerations

Schema merging has a **performance cost** because Spark must:

1.  Read metadata from many files
2.  Merge schemas
3.  Build a unified schema

Large datasets with thousands of files can experience slower reads.

To reduce overhead:

-   Use consistent schemas when possible
-   Avoid frequent schema changes
-   Define schemas manually when reading

``` python
spark.read.schema(my_schema).parquet("data/")
```

------------------------------------------------------------------------

# Best Practices for Schema Evolution

### 1. Prefer Adding Columns

Adding columns is the safest schema evolution change.

### 2. Avoid Changing Data Types

Problematic change:

    age INT

to

    age STRING

### 3. Avoid Renaming Columns

Renaming often results in duplicate columns.

### 4. Keep Backward Compatibility

Example:

    Old: id, name
    New: id, name, email

------------------------------------------------------------------------

# Real-World Example

Suppose an application logs user events.

Initial schema:

    user_id
    event_type
    timestamp

Later version adds device information:

    user_id
    event_type
    timestamp
    device_type

Using schema evolution allows Spark to read **all historical logs**
together.

------------------------------------------------------------------------

# Summary

Schema evolution in PySpark allows datasets to **change structure over
time while still remaining readable**.

Key points:

-   Schema evolution handles **changing dataset structures**
-   Most common with **Parquet, JSON, ORC**
-   Spark can **merge schemas across files**
-   Missing values appear as **null**
-   Schema merging is enabled using **mergeSchema**

Example:

``` python
df = spark.read.option("mergeSchema","true").parquet("data/")
```
