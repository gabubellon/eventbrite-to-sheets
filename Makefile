build:
	docker-compose build eventbrite_api

up:
	docker-compose up eventbrite_api
	
local:
	uvicorn app.main:app --reload --workers=1 --host=0.0.0.0 --port=8080