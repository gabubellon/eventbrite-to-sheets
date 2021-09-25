FROM python:3.9-slim-buster

WORKDIR ./eventbrite-to-sheets

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app

CMD [ "uvicorn", "app.main:app", "--reload", "--workers=1", "--host=0.0.0.0", "--port=8080 " ]

  

