FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential

RUN pip3 install flask
RUN pip3 install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run