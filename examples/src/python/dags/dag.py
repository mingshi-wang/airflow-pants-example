from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

class MyBashOperator(BashOperator):
    pass

dag = DAG(
    dag_id='my_dag',
    default_args={
        'owner': 'pipeline',
        'depends_on_past': False,
        'start_date': datetime(2019, 6, 1),
        'email': ['pipeline@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
)

task = MyBashOperator(
    task_id='my_task',
    bash_command='date',
    dag=dag
)
