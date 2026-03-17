# Apache Spark Join Strategies (Concise Notes)

## Overview

In **Apache Spark**, joins can be executed using several strategies chosen by the **Catalyst Optimizer**. The strategy depends on:

- Table sizes
- Join condition
- Available memory
- Configuration settings
- Join hints

Main join strategies:

1. Broadcast Hash Join
2. Broadcast Nested Loop Join
3. Sort Merge Join
4. Shuffle Hash Join

---

# 1. Broadcast Join (Concept)

A **Broadcast Join** means Spark sends a **small table to every executor** so the large table does not need to shuffle across the cluster.

Advantages:

- Avoids shuffle
- Very fast for small dimension tables

Spark automatically uses broadcast when the table size is below `spark.sql.autoBroadcastJoinThreshold` (default ≈ 10MB).

---

# 2. Broadcast Hash Join (BHJ)

This is the **most common broadcast join implementation**.

### How it works

1. Small table is broadcast to every executor
2. Each executor builds a **hash table**
3. Large table rows probe the hash table

### PySpark Example

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder.appName("broadcast_join").getOrCreate()

orders = spark.createDataFrame([
    (1, 101),
    (2, 102),
    (3, 103)
], ["order_id", "customer_id"])

customers = spark.createDataFrame([
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie")
], ["customer_id", "name"])

joined = orders.join(broadcast(customers), "customer_id")
joined.show()
joined.explain(True)
```

---

# 3. Shuffle Join (Concept)

A **shuffle join** means Spark must **redistribute data across executors by the join key**.

Example:

```python
df1 = spark.range(0, 1000).withColumnRenamed("id", "key")
df2 = spark.range(0, 1000).withColumnRenamed("id", "key")

joined = df1.join(df2, "key")
joined.explain(True)
```

The `Exchange` step in the plan indicates a **shuffle**.

---

# 4. Sort Merge Join (SMJ)

A **Sort Merge Join** is the **most common strategy when both tables are large**.

### How it works

1. Shuffle both datasets by join key
2. Sort partitions by join key
3. Merge sorted rows

### PySpark Example

```python
large1 = spark.range(0, 1000000).withColumnRenamed("id", "key")
large2 = spark.range(0, 1000000).withColumnRenamed("id", "key")

joined = large1.join(large2, "key")
joined.explain(True)
```

---

# 5. Shuffle Hash Join

Another shuffle-based join:

### PySpark Example

```python
from pyspark.sql import functions as F

medium1 = spark.range(0, 10000).withColumnRenamed("id", "key")
medium2 = spark.range(0, 10000).withColumnRenamed("id", "key")

joined = medium1.join(medium2, "key")
joined.explain(True)
```

Shuffle hash joins occur when both tables are medium-sized and Spark cannot broadcast.

---

# 6. Broadcast Nested Loop Join (BNLJ)

A **Broadcast Nested Loop Join** broadcasts one dataset and performs a **nested loop comparison**.

### PySpark Example

```python
df_small = spark.createDataFrame([(1,), (2,), (3,)], ["value"])
df_large = spark.createDataFrame([(2,), (4,)], ["value"])

# Non-equi join condition
joined = df_large.join(df_small, df_large.value > df_small.value)
joined.explain(True)
```

Used when:
- Join condition is non-equality (`<`, `>`, `<=`, `>=`, `OR`)
- Cross joins
- Complex OR conditions

---

# 7. Cross Join Example

```python
df1 = spark.createDataFrame([(1,), (2,)], ["a"])
df2 = spark.createDataFrame([(3,), (4,)], ["b"])

cross = df1.crossJoin(df2)
cross.show()
cross.explain(True)
```

Spark may use **BroadcastNestedLoopJoin** internally.

---

# 8. Join Strategy Comparison

| Join Strategy | Shuffle | Broadcast | Best Use Case |
|---|---|---|---|
| Broadcast Hash Join | No | Yes | Small table + large table |
| Sort Merge Join | Yes | No | Both tables large |
| Shuffle Hash Join | Yes | No | Medium tables |
| Broadcast Nested Loop Join | No | Yes | Non-equi joins, cross joins |
| Cross Join | Sometimes | Sometimes | Cartesian product |

---

# 9. Influencing Spark Join Strategy

### Broadcast Hint

```python
joined = df1.join(broadcast(df2), "id")
```

### SQL Hint
Spark SQL supports **join hints**, the **hint** goes before the table name in the FROM clause using the /*+ BROADCAST(table) */ comment syntax.

```python
joined = spark.sql("""
SELECT *
FROM fact
JOIN /*+ BROADCAST(dim) */ dim
ON fact.id = dim.id
""")
```
---

# 10. Inspecting the Physical Plan

```python
joined.explain(True)
```

Operators to look for:
- `BroadcastHashJoin`
- `SortMergeJoin`
- `ShuffleHashJoin`
- `BroadcastNestedLoopJoin`

---

# 11. Practical Rules of Thumb

| Scenario | Recommended Strategy |
|---|---|
| Small table + large table | Broadcast Hash Join |
| Both tables large | Sort Merge Join |
| Medium tables | Shuffle Hash Join |
| Non-equi joins | Broadcast Nested Loop Join |

---

# 12. Key Takeaways

- **Broadcast Join** is a concept.
- **Broadcast Hash Join** is the typical broadcast implementation.
- **Sort Merge Join** is the most common shuffle join.
- **Shuffle Join** means data redistribution across the cluster.
- **Broadcast Nested Loop Join** is a fallback for complex joins.

Understanding these strategies is critical for **Spark performance tuning and data engineering interviews**.

---
# Spark Broadcast Join Example (SQL + PySpark)

## 1. Setup SparkSession and Sample Data

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("broadcast_join_example").getOrCreate()

# Sample fact table
fact_df = spark.createDataFrame([
    (1, 101),
    (2, 102),
    (3, 103),
    (4, 104)
], ["order_id", "customer_id"])

# Sample dimension table
dim_df = spark.createDataFrame([
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie"),
    (104, "David")
], ["customer_id", "name"])

# Register as temporary views for SQL
fact_df.createOrReplaceTempView("fact")
dim_df.createOrReplaceTempView("dim")
```

---

## 2. Broadcast Join Using Spark SQL Hint

```python
joined_sql = spark.sql("""
SELECT *
FROM fact
JOIN /*+ BROADCAST(dim) */ dim
ON fact.customer_id = dim.customer_id
""")

joined_sql.show()
```

**Execution Plan:**

```python
joined_sql.explain(True)
```

Look for `BroadcastHashJoin` to confirm Spark is broadcasting the `dim` table.

---

## 3. Broadcast Join Using PySpark DataFrame API

```python
from pyspark.sql.functions import broadcast

joined_df = fact_df.join(broadcast(dim_df), "customer_id")
joined_df.show()
joined_df.explain(True)
```

- The DataFrame API automatically broadcasts the smaller table.
- Equivalent to SQL hint method.

---

## 4. Notes

- SQL hint syntax: `/*+ BROADCAST(table) */` goes **before the table name** in the join.
- Spark may ignore the hint if the table is too large.
- Adjust broadcast threshold using:

```python
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 20*1024*1024)  # 20MB
```

- This ensures efficient **Broadcast Hash Join** when one table is small.

---

## Key Takeaways

- Use **Broadcast Hash Join** when one table is small.
- Spark SQL hints and DataFrame API `broadcast()` are equivalent.
- Check `explain(True)` to confirm join strategy.
- Broadcast joins reduce shuffle and improve performance.

