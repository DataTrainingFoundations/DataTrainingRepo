# 1. Import necessary modules
from pyspark.sql import SparkSession

# 2. Create SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

sc=spark.sparkContext

files = sc.wholeTextFiles("./*.txt")

data = sc.parallelize([1, 2, 2, 3, 3, 3, 4])
unique = data.distinct()
print(unique.collect())  # [1, 2, 3, 4]

print(files.collect())

# Read log file, filter errors, extract timestamps, which days did errors occur??
log_rdd = sc.textFile("./data/test.log")

error_times = log_rdd \
    .filter(lambda line: "ERROR" in line) \
    .map(lambda line: line.split()[0]) \
    .distinct() \
    .collect()

print(error_times)

##############################################

# Sample log data
logs = log_rdd


# Example 1: Filter and map
print("=== Error Logs (timestamp only) ===")
error_times = logs \
    .filter(lambda line: "ERROR" in line) \
    .map(lambda line: line.split()[0:2])

for time in error_times.collect():
    print(f"  {time}")

# Example 2: FlatMap to extract words
print("\n=== Unique Log Levels ===")
log_levels = logs \
    .map(lambda line: line.split()[2]) \
    .distinct()

print(f"  {log_levels.collect()}")

# Example 3: Complex chain
print("\n=== Word Frequency in Error Messages ===")
error_words = (logs 
    .filter(lambda line: "ERROR" in line) 
    .flatMap(lambda line: line.split()[3:])
    .map(lambda word: (word.lower(), 1))
    #.reduceByKey(lambda a, b: f"({a},{b})")
    .reduceByKey(lambda a, b: a+b)
    .sortBy(lambda x: x[1], ascending=False))
print(error_words.collect())
for word, count in error_words.collect():
    print(f"  {word}: {count}")

# Example 4: Set operations
info_lines = logs.filter(lambda l: "INFO" in l)
warn_error_lines = logs.filter(lambda l: "WARN" in l or "ERROR" in l)

print(f"\n=== Line Counts ===")
print(f"  INFO lines: {info_lines.count()}")
print(f"  WARN/ERROR lines: {warn_error_lines.count()}")
print(f"  All lines: {logs.count()}")
print(f"  Combined (union): {info_lines.union(warn_error_lines).count()}")

sc.stop()

