# complete_job.py
from pyspark.sql import SparkSession
import time

def main():
    # Initialize Spark
    spark = (SparkSession.builder 
        #.appName("ComprehensiveJobExample") 
        .config("spark.ui.showConsoleProgress", "true") 
        .getOrCreate())
    
    sc = spark.sparkContext
    
    print("=" * 50)
    print(f"Application ID: {sc.applicationId}")
    print(f"Spark Version: {spark.version}")
    print(f"Master: {sc.master}")
    print(f"Default Parallelism: {sc.defaultParallelism}")
    print("=" * 50)
    
    # Job 1: Basic computation
    print("\n[Job 1] Starting basic computation...")
    start = time.time()
    
    numbers = sc.parallelize(range(1, 100001), numSlices=8)
    count = numbers.count()
    
    print(f"[Job 1] Counted {count} elements in {time.time() - start:.2f}s")
    
    # Job 2: Multi-stage computation
    print("\n[Job 2] Starting multi-stage computation...")
    start = time.time()
    
    words = sc.parallelize([
        "Spark is fast",
        "Spark is distributed",
        "Spark processes big data",
        "Big data is everywhere"
    ])
    
    word_counts = words \
        .flatMap(lambda line: line.lower().split()) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .sortBy(lambda x: x[1], ascending=False)
    
    top_words = word_counts.take(5)
    print(f"[Job 2] Top 5 words: {top_words}")
    print(f"[Job 2] Completed in {time.time() - start:.2f}s")
    
    # Job 3: Aggregation
    print("\n[Job 3] Starting aggregation...")
    start = time.time()
    
    sales = sc.parallelize([
        ("Electronics", 1200),
        ("Clothing", 450),
        ("Electronics", 800),
        ("Food", 200),
        ("Clothing", 350),
        ("Electronics", 950),
        ("Food", 180)
    ])
    
    category_totals = sales \
        .reduceByKey(lambda a, b: a + b) \
        .collect()
    
    print(f"[Job 3] Category totals: {dict(category_totals)}")
    print(f"[Job 3] Completed in {time.time() - start:.2f}s")
    
    print("\n" + "=" * 50)
    print("All jobs completed successfully!")
    print(f"View Spark UI at: http://localhost:4040")
    print("=" * 50)
    
    # Allow time to view Spark UI
    input("Press Enter to exit and stop Spark...")
    

    spark.stop()

if __name__ == "__main__":
    main()