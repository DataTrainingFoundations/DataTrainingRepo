
# PySpark RDD Activity Solutions (Interview‑Level Reference)

---

# 1) Common Elements Between Two Lists

## Code
```python
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 3, 5, 7, 9]

rdd1 = sc.parallelize(list1)
rdd2 = sc.parallelize(list2)

common_rdd = rdd1.intersection(rdd2)

print(common_rdd.collect())
```

## Output
```
[1, 3, 5]
```

## DAG Explanation

Stage 1:
parallelize → create RDD partitions

Stage 2:
intersection → shuffle required

Stage 3:
collect → action triggers execution

Shuffle occurs because Spark must compare values across partitions.

---

# 2) Sort Coordinates by Distance

## Code
```python
import math

coords_rdd = sc.parallelize(coords)

sorted_rdd = (
    coords_rdd
    .map(lambda c: (
        math.sqrt((c[0]-target[0])**2 + (c[1]-target[1])**2),
        c
    ))
    .sortByKey()
    .map(lambda x: x[1])
)

print(sorted_rdd.collect())
```

## DAG Explanation

Stage 1:
parallelize

Stage 2:
map → narrow transformation

Stage 3:
sortByKey → wide transformation → shuffle

Stage 4:
collect → action

sortByKey triggers shuffle.

---

# 3) reduceByKey Version (Recommended)

## Code
```python
reduce_rdd = (
    sc.textFile("pokemon.csv")
    .filter(lambda row: row != header)
    .map(lambda r: r.split(","))
    .map(lambda c: (int(c[11]), (int(c[6]), 1)))
    .reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1]))
    .mapValues(lambda x: (x[1], x[0]/x[1]))
)
```

## DAG Explanation

Stage 1:
textFile → map → map

Stage 2:
reduceByKey → shuffle with combiner optimization

Stage 3:
mapValues → collect

## Partition-Level Explanation

Each partition performs LOCAL aggregation first:

Partition example:

Partition 1:
(1,(49,1)), (1,(62,1))

Local combine:
(1,(111,2))

Then shuffle happens sending only aggregated results.

This reduces network traffic significantly.

---

# 4) combineByKey Version (Most Flexible)

## Code
```python
combine_rdd = (
    sc.textFile("pokemon.csv")
    .filter(lambda row: row != header)
    .map(lambda r: r.split(","))
    .map(lambda c: (int(c[11]), int(c[6])))
    .combineByKey(
        lambda value: (value,1),
        lambda acc,value: (acc[0]+value, acc[1]+1),
        lambda acc1,acc2: (acc1[0]+acc2[0], acc1[1]+acc2[1])
    )
    .mapValues(lambda x: (x[1], x[0]/x[1]))
)
```

## DAG Explanation

Stage 1:
map transformations

Stage 2:
combineByKey → shuffle

Stage 3:
mapValues

## Partition-Level Explanation

combineByKey performs:

Partition local combine → shuffle → global combine

Most efficient and flexible aggregation.

---

# 5) aggregateByKey Version

## Code
```python
agg_rdd = (
    sc.textFile("pokemon.csv")
    .filter(lambda row: row != header)
    .map(lambda r: r.split(","))
    .map(lambda c: (int(c[11]), int(c[6])))
    .aggregateByKey(
        (0,0),
        lambda acc,value: (acc[0]+value, acc[1]+1),
        lambda acc1,acc2: (acc1[0]+acc2[0], acc1[1]+acc2[1])
    )
    .mapValues(lambda x: (x[1], x[0]/x[1]))
)
```

## DAG Explanation

Same structure as combineByKey:

map → aggregateByKey (shuffle) → mapValues → collect

---

# 6) groupByKey Version (WORST — Avoid in Interviews ⚠️)

## Code
```python
group_rdd = (
    sc.textFile("pokemon.csv")
    .filter(lambda row: row != header)
    .map(lambda r: r.split(","))
    .map(lambda c: (int(c[11]), int(c[6])))
    .groupByKey()
    .mapValues(lambda values: (
        len(list(values)),
        sum(values)/len(list(values))
    ))
)
```

## Why groupByKey is worse ⚠️

groupByKey does NOT perform local aggregation.

Example:

Partition 1:
(1,49)
(1,62)

Partition 2:
(1,82)

Shuffle sends ALL values across network:

(1,[49,62,82])

Problems:

• Massive network traffic  
• High memory usage  
• Slow performance  
• Risk of OOM  

reduceByKey instead sends:

Partition 1 → (1,111,2)

Much smaller.

---

# Performance Ranking (Interview Answer)

Best → Worst

combineByKey = aggregateByKey
reduceByKey
groupByKey

---

# Partition‑Level Summary

Before shuffle:

Partition 1:
(1,49)
(1,62)

Partition 2:
(1,82)

reduceByKey:

Partition 1 → (1,111,2)
Partition 2 → (1,82,1)

Shuffle sends small data.

groupByKey:

Partition 1 → sends all values
Partition 2 → sends all values

Much heavier.

---

# Interview One‑Line Summary

reduceByKey, combineByKey, and aggregateByKey perform map‑side aggregation reducing shuffle, while groupByKey sends all data across the network causing performance and memory issues.

### More Detailed Analysis Below
# Visual Legend

```
[Narrow Transformation]  = No shuffle
[Wide Transformation]    = Shuffle occurs
(Px)                     = Partition number
→                        = Execution flow
⇄                        = Shuffle
```

---

# 1) intersection()

## Code
```python
common_rdd = rdd1.intersection(rdd2)
common_rdd.collect()
```

## DAG Diagram

```
RDD1 partitions        RDD2 partitions
(P0) [1,2]             (P0) [1,3]
(P1) [3,4]             (P1) [5,7]
(P2) [5,6]             (P2) [9]

        ↓
    intersection
   [WIDE — SHUFFLE]
        ⇄

Shuffle groups identical keys together

        ↓

Result partitions
(P0) [1]
(P1) [3]
(P2) [5]

        ↓
     collect()
```

Shuffle required to compare values across partitions.

---

# 2) sortByKey()

## Code
```python
coords_rdd.map(...).sortByKey().collect()
```

## DAG Diagram

```
Original RDD
(P0) coords
(P1) coords
(P2) coords

        ↓
 map (distance)
[NARROW]

(P0) (dist,coord)
(P1) (dist,coord)

        ↓
 sortByKey
[WIDE — SHUFFLE]
        ⇄

Spark redistributes keys in sorted order

        ↓

Sorted partitions
(P0) smallest
(P1) medium
(P2) largest

        ↓
 collect
```

---

# 3) reduceByKey()

## DAG Diagram

```
Initial RDD

(P0)
(1,49)
(1,62)

(P1)
(1,82)
(2,100)

        ↓

Local aggregation happens FIRST

(P0)
(1,(111,2))

(P1)
(1,(82,1))
(2,(100,1))

        ↓
reduceByKey shuffle
[WIDE — SHUFFLE]
        ⇄

(P0)
(1,(193,3))

(P1)
(2,(100,1))

        ↓
mapValues
[NARROW]

        ↓
collect
```

Key benefit:
Shuffle sends reduced data, not raw data.

---

# 4) combineByKey()

## DAG Diagram

```
Initial

(P0)
(1,49)
(1,62)

(P1)
(1,82)

        ↓

createCombiner (local)

(P0)
(1,(111,2))

(P1)
(1,(82,1))

        ↓

Shuffle
[WIDE]
        ⇄

mergeCombiners

(P0)
(1,(193,3))

        ↓
mapValues
```

Most flexible aggregation primitive.

---

# 5) aggregateByKey()

## DAG Diagram

```
Initial

(P0)
(1,49)
(1,62)

        ↓

seqOp (local aggregation)

(P0)
(1,(111,2))

        ↓

Shuffle
        ⇄

combOp (merge partitions)

(P0)
(1,(193,3))
```

Similar efficiency to combineByKey.

---

# 6) groupByKey (Worst)

## DAG Diagram

```
Initial

(P0)
(1,49)
(1,62)

(P1)
(1,82)

        ↓

Shuffle WITHOUT aggregation
        ⇄

(P0)
(1,[49,62,82])

        ↓

Compute average AFTER shuffle
```

Problem:
All raw values shuffled.

reduceByKey sends only:

(1,(111,2))

Much smaller.

---

# Partition-Level Comparison

## reduceByKey

```
Partition 1:
(1,49),(1,62)

Local combine:
(1,111,2)

Shuffle sends small data
```

## groupByKey

```
Partition 1:
(1,49),(1,62)

Shuffle sends ALL data
```

Network impact:
reduceByKey = efficient
groupByKey = inefficient

---

# Execution Stage Summary

reduceByKey:

Stage 1 map
Stage 2 reduceByKey (shuffle)
Stage 3 mapValues
Stage 4 collect

groupByKey:

Stage 1 map
Stage 2 groupByKey (shuffle heavy)
Stage 3 mapValues
Stage 4 collect

---

# Interview Summary Answer

Best:
combineByKey
aggregateByKey
reduceByKey

Worst:
groupByKey

Reason:
map‑side aggregation reduces shuffle size dramatically.
