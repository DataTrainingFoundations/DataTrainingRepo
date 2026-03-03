from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# 2. Create SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

#df = spark.read.csv("data2.csv", header=True, inferSchema=True)


schema_nameagecity = StructType([StructField("name",StringType(),True),
                     StructField("age",IntegerType(),True),
                     StructField("city",StringType(),True)])

df = spark.read.csv("data2.csv", header=True, schema=schema_nameagecity)

df.show()

############################################
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("Working on DataFrames") \
    .getOrCreate()

# ---------------------
# Reading CSV Files
# ---------------------

# Simple read with header
df_csv = spark.read.csv("employees.csv", header=True, inferSchema=True)

# With explicit options
df_csv_opts = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", ",") \
    .option("nullValue", "NA") \
    .csv("employees.csv")

# With predefined schema (recommended for production)
employee_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("salary", DoubleType(), True)
])

df_csv_schema = spark.read \
    .option("header", "true") \
    .schema(employee_schema) \
    .csv("employees.csv")

# ---------------------
# Reading JSON Files
# ---------------------

# Single-line JSON (default)
df_json = spark.read.json("events.json")

# Multi-line JSON (entire file is one JSON object)
df_json_multi = spark.read \
    .option("multiLine", "true") \
    .json("config.json")

# ---------------------
# Reading Parquet Files
# ---------------------

# Reading multiple csv files
df_csv_1 = spark.read.csv("data/year=2023/month=01/sales.csv", inferSchema=True)
df_csv_2 = spark.read.csv("data/year=2023/month=01/sales.csv", inferSchema=True)


df_csv_1.show()
df_csv_2.show()

df_csv_1.summary()

print(df_csv_1.rdd.getNumPartitions())

df_csv_3=df_csv_1.repartition(2)

print(df_csv_3.rdd.getNumPartitions())

print('printing parquet')
df_csv_3.write.mode("overwrite").parquet("data/year=2023/month=01/sales.parquet")
#df_csv_1.coalesce(1).write.mode("overwrite").parquet("data/year=2023/month=01/sales.parquet")
df_parquet_1= spark.read.parquet("data/year=2023/month=01/sales.parquet",inferSchema=True)
df_parquet_1.show()

#####################################
from pyspark.sql.functions import col, upper, when, current_timestamp

spark = SparkSession.builder.appName("ETL Example").getOrCreate()

# EXTRACT: Read raw data
raw_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("sales.csv")

print("Raw data:")
raw_df.show(5)
print("Row count:", raw_df.count())

# TRANSFORM: Clean and enrich data
transformed_df = raw_df \
    .filter(col("amount").isNotNull()) \
    .filter(col("amount") > 0) \
    .withColumn("region", upper(col("region"))) \
    .withColumn("amount_category",
        when(col("amount") < 100, "SMALL")
        .when(col("amount") < 1000, "MEDIUM")
        .otherwise("LARGE")) \
    .withColumn("processed_at", current_timestamp())

print("\nTransformed data:")
transformed_df.show(5)

# LOAD: Write processed data
transformed_df.write \
    .partitionBy("region") \
    .mode("overwrite") \
    .parquet("processed_data/sales")

print("\nData written to processed_data/sales")

spark.stop()

