FROM python:3.9-slim-buster

WORKDIR /usr/src/eventbrite-to-sheets

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD [ "uvicorn", "app.main:app", "--reload", "--workers=1", "--host=0.0.0.0", "--port=8080 " ]

  

