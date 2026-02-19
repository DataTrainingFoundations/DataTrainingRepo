import boto3
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from io import StringIO

s3 = boto3.client("s3")

def lambda_handler(event, context):

    bucket = "retail-etl-feb20-2"
    key = "processed/orders_flat.csv"

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response["Body"].read().decode("utf-8")

    df = pd.read_csv(StringIO(content))

    engine = create_engine(
        "mysql+mysqlconnector://admin:password@rds-endpoint/mydb"
    )

    df.to_sql(
        name="fact_sales",
        con=engine,
        if_exists="append",
        index=False
    )

    return {"statusCode": 200}