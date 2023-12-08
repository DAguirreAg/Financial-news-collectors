from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

import requests

PORT = 8102

def call_api(url: str):
    response = requests.get(url)
    
    if not (200<=response.status_code<=299):
        raise Exception('Something went wrong.')

def _download_webpages():
    url = f"http://localhost:{PORT}/download_webpages"    
    call_api(url)
    
def _etl_bbc():
    url = f"http://localhost:{PORT}/etl_bbc"    
    call_api(url)

with DAG("financial_news_collectors_dag", # Dag id
    start_date=datetime(2023, 10 ,5), # start date, the 1st of January 2023 
    schedule='@hourly', # Cron expression, here @daily means once every day.
    catchup=False):

    # Tasks are implemented under the dag object
    download_webpages = PythonOperator(
        task_id="download_webpages",
        python_callable=_download_webpages
    )

    etl_bbc = PythonOperator(
        task_id="etl_bbc",
        python_callable=_etl_bbc
    )


    download_webpages >> etl_bbc