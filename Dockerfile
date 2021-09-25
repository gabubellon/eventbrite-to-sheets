FROM python:3.9-slim-buster

WORKDIR ./api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app