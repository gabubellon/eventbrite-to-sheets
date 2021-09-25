build:
	docker-compose build eventbrite_api

up:
	docker-compose up eventbrite_api
	
server:
	uvicorn src.main:app --reload --workers=1 --host=0.0.0.0 --port=80