import datetime
from datetime import date
from datetime import time
from datetime import timedelta

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from src.catGif import saveCatGif
from src.topMusic import saveTopSongText
from src.weather import saveWeatherText
from src.slackSend import slackNotification

start_date = datetime.datetime.combine(date.today(), time())
start_date = start_date + timedelta(hours=8)
default_args = {
    'owner': 'jojo',
    'start_date': start_date,
    'schedule_interval': '* * * 8 0',
    'tag': 'slack'
}


with DAG(dag_id='slack_notification_daily',
         default_args=default_args) as dag:
    get_cat_gif = PythonOperator(
        task_id='get_cat_gif',
        python_callable=saveCatGif,
    )

    get_top_song = PythonOperator(
        task_id='get_top_song',
        python_callable=saveTopSongText,
    )

    get_weather = PythonOperator(
        task_id='get_weather',
        python_callable=saveWeatherText,
    )

    send_notification = PythonOperator(
        task_id='send_notification',
        python_callable=slackNotification,
    )

    [get_cat_gif, get_top_song, get_weather] >> send_notification
