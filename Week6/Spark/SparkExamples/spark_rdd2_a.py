# 1. Import necessary modules
from pyspark.sql import SparkSession

# 2. Create SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

# Initialize SparkContext
sc= spark.sparkContext

# From a text file
rdd1 = sc.textFile("file.txt")

# From multiple files using wildcards
rdd2 = sc.textFile("./data/*.log")

print(rdd1.collect())

print(rdd2.collect())

###########################################


# Create an RDD from a list
numbers = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numSlices=4)

# Check partition count
print(f"Number of partitions: {numbers.getNumPartitions()}")

# View data in each partition
def show_partition(index, iterator):
    return [(index, list(iterator))]

partitioned_data = numbers.mapPartitionsWithIndex(show_partition).collect()
print("Data by partition:")
for part_id, data in partitioned_data:
    print(f"  Partition {part_id}: {data}")

# Demonstrate immutability
evens = numbers.filter(lambda x: x % 2 == 0)
print(f"\nOriginal RDD count: {numbers.count()}")
print(f"Filtered RDD count: {evens.count()}")

evens2 = numbers.filter(lambda x: x % 2 == 0)

evens2.collect()

# Show lineage
print(f"\nLineage (Debug String):")
print(evens2.toDebugString())

sc.stop()

spark.stop()

# From multiple files using wildcards
#rdd = sc.textFile("path/to/logs/*.log")