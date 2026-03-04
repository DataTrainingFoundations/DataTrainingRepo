# my_job.py
from pyspark.sql import SparkSession
import argparse

def main(input_path, output_path):
    # Create SparkSession
    spark = (SparkSession.builder
        .appName("MyFirstJob")
        #.master("local[*]") 
        .config("spark.master","local[*]")
        .getOrCreate()
    )
    
    # Get SparkContext
    sc = spark.sparkContext
    
    # Create RDD and perform operations
    data = sc.parallelize(range(1, 1000001))
    
    # Transformations (lazy)
    squared = data.map(lambda x: x ** 2)
    filtered = squared.filter(lambda x: x % 2 == 0)
    
    # Action triggers job
    result = filtered.reduce(lambda a, b: a + b)
    
    print(f"Result: {result}")

    spark = SparkSession.builder.appName("ConfigurableJob").getOrCreate()
    df = spark.read.parquet(input_path)
    # ... processing ...
    df.write.parquet(output_path,mode="append")

    spark.stop()
    
    # Clean up
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    
    main(args.input, args.output)




