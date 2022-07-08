
airflow db init
airflow users create -e jojo@jojo.com -f jo -l jo -p jojo -u jojo -r Admin

airflow scheduler -D
airflow webserver -H 0.0.0.0 -p 8080