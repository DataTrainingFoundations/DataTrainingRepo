from pyspark import SparkContext

sc = SparkContext("local[*]", "ActionsDemo")

# Create sample data
numbers = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
words = sc.parallelize(["apple", "banana", "apple", "cherry", "banana", "apple"])

# Demonstrate various actions
print("=== Counting Operations ===")
print(f"count(): {numbers.count()}")
print(f"countByValue(): {dict(words.countByValue())}")

print("\n=== Retrieval Operations ===")
print(f"collect(): {numbers.collect()}")
print(f"first(): {numbers.first()}")
print(f"take(3): {numbers.take(3)}")
print(f"takeSample(False, 3): {numbers.takeSample(False, 3, seed=42)}")

print("\n=== Aggregation Operations ===")
print(f"reduce (sum): {numbers.reduce(lambda a, b: a + b)}")
print(f"reduce (max): {numbers.reduce(lambda a, b: a if a > b else b)}")
print(f"fold (sum with zero): {numbers.fold(0, lambda a, b: a + b)}")

# Aggregate: calculate sum and count for average
sum_count = numbers.aggregate(
    (0, 0),
    lambda acc, val: (acc[0] + val, acc[1] + 1),
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])
)
print(f"aggregate (sum, count): {sum_count}")
print(f"Average: {sum_count[0] / sum_count[1]}")

print("\n=== Other Useful Actions ===")
print(f"top(3) - largest values: {numbers.top(3)}")
print(f"takeOrdered(3) - smallest values: {numbers.takeOrdered(3)}")
print(f"isEmpty(): {numbers.isEmpty()}")

numbers.saveAsTextFile("testNumbers")

def f(x): print(x)
numbers.foreach(f)

sc.stop()