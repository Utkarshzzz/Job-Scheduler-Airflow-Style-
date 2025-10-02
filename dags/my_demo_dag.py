from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

def task_a():
    print("Task A: Starting job")

def task_b():

    if random.random() < 0.4:
        raise ValueError("Simulated failure in Task B")
    print("Task B: Succeeded")

def task_c():
    print("Task C: Final step")

default_args = {
    'owner': 'utkarsh',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

with DAG(
    dag_id='my_demo_dag',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id='task_a', python_callable=task_a)
    t2 = PythonOperator(task_id='task_b', python_callable=task_b)
    t3 = PythonOperator(task_id='task_c', python_callable=task_c)

    t1 >> t2 >> t3
