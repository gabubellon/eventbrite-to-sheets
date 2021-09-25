FROM python:3.9-slim-buster
COPY ./app /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt