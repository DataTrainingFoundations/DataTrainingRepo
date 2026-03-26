from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.operators.bash import BashOperator
from datetime import datetime


def load_orders_to_snowflake():
    hook = SnowflakeHook(snowflake_conn_id2="my_snowflake_conn")

    sql_statements = [
        "CREATE DATABASE IF NOT EXISTS MY_DB",
        "CREATE SCHEMA IF NOT EXISTS MY_DB.RAW",
        """
        CREATE TABLE IF NOT EXISTS MY_DB2.RAW.ORDERS(
            order_id INT,
            customer_id INT,
            order_date DATE,
            amount INT
        )
        """,
        """
        INSERT INTO MY_DB2.RAW.ORDERS(order_id, customer_id, order_date, amount)
        VALUES
        (1, 101, '2026-03-15', 120),
        (2, 102, '2026-03-15', 50),
        (3, 101, '2026-03-16', 75),
        (4, 103, '2026-03-16', 200),
        (5, 102, '2026-03-17', 30)
        """
    ]

    hook.run(sql_statements)


with DAG(
    dag_id="snowflake_dbt_pipeline_2",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    # Task 1: Load raw data into Snowflake
    load_orders = PythonOperator(
        task_id="load_orders",
        python_callable=load_orders_to_snowflake
    )

    # Task 2: Run dbt models
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd ~/pySparkFun/dbt_project && dbt run --profiles-dir /home/will/pySparkFun/dbt_project"
    )

    # Task 3: Run dbt tests
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd ~/pySparkFun/dbt_project && dbt test --profiles-dir /home/will/pySparkFun/dbt_project'
    )

    load_orders >> dbt_run >> dbt_test
