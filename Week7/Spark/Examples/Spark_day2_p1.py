# 1. Import necessary modules
from pyspark.sql import SparkSession

# 2. Create SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

# 3. Load data
df = spark.read.csv("data.csv", header=True)


df.createOrReplaceTempView("my_table")
result = spark.sql("SELECT * FROM my_table WHERE age > 30")

result.show()

############################################################################

# Create DataFrame
data = [
    (1, "Alice", "Engineering", 75000),
    (2, "Bob", "Marketing", 65000),
    (3, "Charlie", "Engineering", 80000),
    (4, "Diana", "Sales", 55000),
    (5, "Eve", "Marketing", 70000)
]

df = spark.createDataFrame(data, ["id", "name", "department", "salary"])

# Register as temporary view
df.createOrReplaceTempView("employees")

# Run SQL queries
print("All employees:")
spark.sql("SELECT * FROM employees").show()

print("Engineers only:")
spark.sql("""
    SELECT name, salary 
    FROM employees 
    WHERE department = 'Engineering'
""").show()

print("Average salary by department:")
spark.sql("""
    SELECT department, 
           AVG(salary) as avg_salary,
           COUNT(*) as count
    FROM employees
    GROUP BY department
    ORDER BY avg_salary DESC
""").show()



############################# advanced queries

spark = SparkSession.builder.appName("Advanced SQL").getOrCreate()

# Sample data
employees = spark.createDataFrame([
    (1, "Alice", 1, 75000),
    (2, "Bob", 2, 65000),
    (3, "Charlie", 1, 80000),
    (4, "Diana", 3, 55000)
], ["id", "name", "dept_id", "salary"])

departments = spark.createDataFrame([
    (1, "Engineering"),
    (2, "Marketing"),
    (3, "Sales")
], ["dept_id", "dept_name"])

employees.createOrReplaceTempView("employees")
departments.createOrReplaceTempView("departments")

# JOIN
print("JOIN:")
spark.sql("""
    SELECT e.name, d.dept_name, e.salary
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
""").show()

# Subquery
print("Subquery (employees earning above average):")
spark.sql("""
    SELECT name, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
""").show()

# Window function
print("Window function (rank by salary):")
spark.sql("""
    SELECT name, dept_id, salary,
           RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rank
    FROM employees
""").show()

# Common Table Expression (CTE)
print("CTE:")
spark.sql("""
    WITH dept_stats AS (
        SELECT dept_id, 
               AVG(salary) as avg_salary,
               MAX(salary) as max_salary
        FROM employees
        GROUP BY dept_id
    )
    SELECT e.name, e.salary, ds.avg_salary
    FROM employees e
    JOIN dept_stats ds ON e.dept_id = ds.dept_id
    WHERE e.salary > ds.avg_salary
""").show()



########################
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

spark = SparkSession.builder.appName("Mixed Approach").getOrCreate()

data = [
    ("Alice", 34, 75000),
    ("Bob", 45, 65000),
    ("Charlie", 29, 80000)
]

df = spark.createDataFrame(data, ["name", "age", "salary"])
df.createOrReplaceTempView("people")

# Start with SQL for complex aggregation
sql_result = spark.sql("""
    SELECT 
        name,
        salary,
        salary - (SELECT AVG(salary) FROM people) as vs_avg
    FROM people
""")

# Continue with DataFrame API for transformations
final_result = (sql_result 
    .withColumn("name_upper", upper(col("name"))) 
    .filter(col("vs_avg") > 0))

print("Combined approach:")
final_result.show()

# Or vice versa: DataFrame to SQL
df_transformed = df.withColumn("bonus", col("salary") * 0.1)
df_transformed.createOrReplaceTempView("people_with_bonus")

spark.sql("""
    SELECT name, salary, bonus, salary + bonus as total
    FROM people_with_bonus
    ORDER BY total DESC
""").show()


###########global views###################################
data = [("Alice", 30), ("Bob", 25)]
df = spark.createDataFrame(data, ["name", "age"])

# Create global temp view (accessible across sessions)
df.createOrReplaceGlobalTempView("global_people")

# Must use global_temp database prefix
spark.sql("SELECT * FROM global_temp.global_people").show()

# Local temp view (current session only)
df.createOrReplaceTempView("local_people")
spark.sql("SELECT * FROM local_people").show()

# List all tables/views
print("Views in catalog:")
for table in spark.catalog.listTables():
    print(f"  {table.name} (database: {table.database}, isTemporary: {table.isTemporary})")

data = [("Alice", 30), ("Bob", 25)]
df = spark.createDataFrame(data, ["name", "age"])

# Create view
df.createOrReplaceTempView("my_view")

# Check if view exists
print("Tables/Views:", [t.name for t in spark.catalog.listTables()])

# Drop view
spark.catalog.dropTempView("my_view")
print("After drop:", [t.name for t in spark.catalog.listTables()])

# Clear all cached tables
spark.catalog.clearCache()

# List columns in a view
df.createOrReplaceTempView("my_view")
print("Columns:", spark.catalog.listColumns("my_view"))

spark.stop()