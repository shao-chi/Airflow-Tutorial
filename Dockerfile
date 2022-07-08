FROM python:3.9

WORKDIR /airflow_tutorial

ADD . /airflow_tutorial

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary
