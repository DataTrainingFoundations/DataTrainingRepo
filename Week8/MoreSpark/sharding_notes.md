# Data Sharding in PySpark and BigQuery

Author: Generated Notes

------------------------------------------------------------------------

# 1. What is Data Sharding?

Data sharding is a technique where a large dataset is split horizontally
into smaller subsets called **shards**.\
Each shard contains part of the dataset and can be stored or processed
on different machines.

Purpose: - Handle very large datasets - Improve query performance -
Enable horizontal scaling

Example:

Original Table

  user_id   name
  --------- -------
  1         Alice
  2         Bob
  3         Carol
  4         Dave
  5         Eve

Sharded:

Shard 1 \| user_id \| name \| \|-------\|------\| \|1\|Alice\|
\|2\|Bob\|

Shard 2 \| user_id \| name \| \|-------\|------\| \|3\|Carol\|
\|4\|Dave\| \|5\|Eve\|

------------------------------------------------------------------------
# 2. Sharding Concepts in PySpark

PySpark does not explicitly use the term *shard*.\
Instead, it uses **partitions**, which behave similarly.

Spark partitions distribute data across cluster nodes.

Example:

``` python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sharding_example").getOrCreate()

data = list(range(100))

rdd = spark.sparkContext.parallelize(data, 4)

print(rdd.getNumPartitions())
```

Output

    4

Each partition acts like a **shard of the dataset**.

------------------------------------------------------------------------

# 3. Simulating Sharding in PySpark

We can simulate sharding by distributing rows based on a hash key.

Example dataset:

``` python
from pyspark.sql import Row

data = [
    Row(user_id=1, country="US"),
    Row(user_id=2, country="US"),
    Row(user_id=3, country="UK"),
    Row(user_id=4, country="FR"),
    Row(user_id=5, country="US")
]

df = spark.createDataFrame(data)
```

Create a shard key:

``` python
from pyspark.sql.functions import col

sharded_df = df.repartition(3, col("user_id"))
```

Spark distributes rows across partitions based on the shard key.

Check partitions:

``` python
print(sharded_df.rdd.getNumPartitions())
```

------------------------------------------------------------------------

# 4. Sharding and Data Skew in PySpark

Data skew occurs when **one partition contains far more data than
others**.

Example skewed dataset:

  country   users
  --------- ---------
  US        1000000
  FR        500
  UK        800

If partitioning by country:

    Partition 1 -> US (huge)
    Partition 2 -> FR
    Partition 3 -> UK

Problem:

-   One worker does most of the work
-   Cluster resources wasted

This is similar to **bad sharding**.

Solution approaches:

1.  Hash-based repartitioning

``` python
df = df.repartition(10)
```

2.  Salting keys

``` python
from pyspark.sql.functions import rand

df = df.withColumn("salt", (rand()*10).cast("int"))
```

3.  Broadcast joins

``` python
from pyspark.sql.functions import broadcast

df_large.join(broadcast(df_small), "id")
```

------------------------------------------------------------------------

# 5. How BigQuery Handles Sharding

BigQuery typically uses **partitioned tables and clustered tables**
instead of manual sharding.

Older systems used sharded tables:

    events_2023
    events_2024
    events_2025

Modern BigQuery approach:

Partitioned table

``` sql
CREATE TABLE events (
    event_id INT64,
    event_date DATE
)
PARTITION BY event_date;
```

BigQuery automatically distributes data across storage nodes.

Internally BigQuery uses:

-   Columnar storage
-   Distributed storage blocks
-   Parallel query execution

Conceptually similar to sharding but fully managed.

------------------------------------------------------------------------

# 6. How Snowflake Handles Data Distribution

Snowflake does not expose shards.

Instead it uses:

**Micro-partitions**.

Each table is automatically split into:

    50MB - 500MB compressed micro-partitions

Example logical structure

    Table
      ├ Micro-partition 1
      ├ Micro-partition 2
      ├ Micro-partition 3

Snowflake automatically distributes these across cloud storage.

Advantages:

-   Automatic pruning
-   Parallel query processing
-   No manual sharding required

------------------------------------------------------------------------

# 7. PySpark vs BigQuery vs Snowflake Distribution

  System      Distribution Unit
  ----------- -----------------------------
  PySpark     Partitions
  BigQuery    Storage blocks / partitions
  Snowflake   Micro-partitions

All achieve:

-   Parallel computation
-   Horizontal scalability
-   Faster queries

------------------------------------------------------------------------

# 8. Practical Data Engineering Example

Suppose an e-commerce dataset with billions of rows.

Columns

    order_id
    customer_id
    product_id
    timestamp
    price

Possible shard key

    customer_id

Spark example:

``` python
orders = spark.read.parquet("orders")

orders = orders.repartition(100, "customer_id")
```

BigQuery equivalent:

``` sql
CREATE TABLE orders
PARTITION BY DATE(timestamp)
CLUSTER BY customer_id;
```

Snowflake:

Simply load data; micro-partitions automatically created.

------------------------------------------------------------------------

# 9. Key Takeaways

1.  Sharding splits data across machines for scalability.
2.  PySpark uses **partitions** which behave like shards.
3.  Data skew is caused by uneven shard distribution.
4.  BigQuery and Snowflake manage sharding automatically.
5.  Proper shard keys are critical for performance.
