from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime


def dizer_ola():
    print("Olá Mestre, sua primeira DAG está funcionando!")


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    tarefa_ola = PythonOperator(
        task_id="dizer_ola",
        python_callable=dizer_ola
    )