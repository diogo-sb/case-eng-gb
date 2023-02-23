from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.operators.pubsub import PubSubPublishMessageOperator
from airflow.operators.dummy import DummyOperator
from airflow.models import Variable
from datetime import timedelta, datetime


PROJECT_ID = "cobalt-list-378615"
TOPIC_ID = "trigger_function"
MESSAGE = {'data':b'go'}
PROC_NAME = "proc_consolidado"


###################################
# 	CONFIG DAG
###################################
default_args = {
            'owner': 'Diogo Brito',
            'depends_on_past': False,
            'start_date': datetime(2023,2,21),
            'dataflow_default_options': {
                'project': PROJECT_ID,
            }
        }

dag = DAG(
    "dag_case_gb",
    default_args=default_args,
    schedule_interval="@once",
)


##############################
# Funcao para enviar msg para pubsub
#############################

publish_task = PubSubPublishMessageOperator(
        task_id="publish_task",
        project_id=PROJECT_ID,
        topic=TOPIC_ID,
        messages=[MESSAGE],
        dag = dag
    )

###########################
# Funcao cria procedure
##########################

prc_load_task = BigQueryExecuteQueryOperator(
        task_id="call_proc",
        sql=f"CALL `{PROJECT_ID}.procedure.{PROC_NAME}`()",
        use_legacy_sql=False,
        priority="BATCH",
        dag=dag,
        depends_on_past=False
)


validate_table_OK = DummyOperator(task_id='validate_table', dag=dag,trigger_rule='all_success')


###################################
# Ordem de execucao
###################################

publish_task >> validate_table_OK >> prc_load_task