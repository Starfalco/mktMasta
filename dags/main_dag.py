from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import sys
sys.path.append("/opt/airflow/dags/modules/")
from extracts_tasks import prices_task, earnings_estimate_task, earnings_history_task, info_task

args = {
    'owner': 'Nawar',
    'start_date': days_ago(1), # make start date in the past
    'retries': 2,
    'retry_delay': timedelta(minutes=3)
}

dag = DAG(
    dag_id='main_py',
    default_args=args,
    schedule_interval='@daily' # make this workflow happen every day
)

with dag:
    t1 = PythonOperator(
        task_id='prices_task',
        python_callable=prices_task,
        execution_timeout=timedelta(minutes=6),
        dag=dag
    )
    t2 = PythonOperator(
        task_id='earnings_estimate_task',
        python_callable=earnings_estimate_task,
        execution_timeout=timedelta(minutes=6),
        dag=dag
    )
    t3 = PythonOperator(
        task_id='earnings_history_task',
        python_callable=earnings_history_task,
        execution_timeout=timedelta(minutes=6),
        dag=dag
    )
    t4 = PythonOperator(
        task_id='info_task',
        python_callable=info_task,
        execution_timeout=timedelta(minutes=12),
        dag=dag
    )

    t1 >> t2 >> t3 >> t4
