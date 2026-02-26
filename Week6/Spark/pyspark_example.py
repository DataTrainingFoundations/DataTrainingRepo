from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("pyspark_example") \
    .getOrCreate()

sc = spark.sparkContext

sc.setLogLevel("WARN")

rdd1 = sc.parallelize([1, 2, 3, 4, 5])
print(rdd1.collect())

rdd2 = rdd1.map(lambda x: (x, x*10))
input("asdf")

print(rdd2.collect())

spark.stop()
