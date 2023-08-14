import requests
import time
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def get_data(**kwargs):

    tickers = kwargs['tickers']

    for ticker in tickers:

        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=YOUR_API_KEY"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print(f"Market data for {ticker}:\n{json.dumps(data, indent=4)}")
        else:
            print(f"Failed to retrieve market data for {ticker}")



default_dag_args = {
    'start_date': datetime(2022, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
}

with DAG("market_data_alphavantage_dag", schedule_interval='@daily', catchup=False,
         default_args=default_dag_args) as dag_python:

    task_0 = PythonOperator(
        task_id="get_market_data",
        python_callable=get_data,
        op_kwargs={'tickers': ['AAPL', 'GOOGL', 'MSFT', 'AMZN']}  # Add your list of tickers here
    )
