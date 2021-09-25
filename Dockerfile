FROM python:3.9-slim-buster

WORKDIR /usr/src/eventbrite-to-sheets

COPY requirements.txt ./
COPY eventbrite_fields.toml ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/eventbrite-to-sheets"

CMD [ "uvicorn", "src.main:app", "--reload", "--workers=1", "--host=0.0.0.0", "--port=80 " ]

  

