from airflow import DAG
from airflow.decorators import task
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from datetime import datetime, timedelta
import requests
import pandas as pd
import os

with DAG(
    dag_id="market_etl",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=True,
    max_active_runs=1,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(minutes=5)
    }
) as dag:


    # -----------------------------
    # EXTRACT
    # -----------------------------
    @task()
    def hit_yahoo_api(**context):

        stock_ticker = "AMZN"

        # Airflow execution date
        ds = context["ds"]

        dt_obj = datetime.strptime(ds, "%Y-%m-%d")

        # Convert to Unix timestamp
        period1 = int(dt_obj.timestamp())
        period2 = period1 + 86400

        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock_ticker}?symbol={stock_ticker}&period1={period1}&period2={period2}&interval=1d"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        print("URL:", url)
        print("Status:", response.status_code)

        response.raise_for_status()

        data = response.json()

        return data


    # -----------------------------
    # TRANSFORM
    # -----------------------------
    @task()
    def flatten_market_data(yahoo_response):

        result = yahoo_response["chart"]["result"][0]

        meta = result["meta"]

        indicators = result["indicators"]["quote"][0]

        flattened_record = {
            "symbol": meta.get("symbol"),
            "date": datetime.fromtimestamp(
                meta.get("regularMarketTime")
            ).strftime("%Y-%m-%d"),
            "open": indicators.get("open", [None])[0],
            "high": indicators.get("high", [None])[0],
            "low": indicators.get("low", [None])[0],
            "close": indicators.get("close", [None])[0],
            "volume": indicators.get("volume", [None])[0]
        }

        print("Flattened Record:", flattened_record)

        return flattened_record


    # -----------------------------
    # LOAD
    # -----------------------------
    @task()
    def load_market_data(flattened_record):

        db_path = "/home/will/airflowTestDB/market_data.db"

        db_dir = os.path.dirname(db_path)

        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        market_database_hook = SqliteHook("market_database_conn")

        conn = market_database_hook.get_conn()

        df = pd.DataFrame([flattened_record])

        df.to_sql(
            name="market_data",
            con=conn,
            if_exists="append",
            index=False
        )

        print("Loaded data to SQLite")


    # -----------------------------
    # DAG dependencies
    # -----------------------------

    raw_market_data = hit_yahoo_api()

    transformed_market_data = flatten_market_data(raw_market_data)

    load_market_data(transformed_market_data)


#rm /home/will/airflowTestDB/market_data.db
#Open the Airflow Web UI
#Go to Admin → Connections
#Click + Add Connection
#Fill in:
#Field	Value
#Connection Id	market_database_conn
#Connection Type	SQLite
#Host	/home/will/airflowTestDB/market_data.db
#Save.      