build:
	docker-compose build eventbrite_api

up:
	docker-compose up eventbrite_api 

up_s:
	docker-compose up -d eventbrite_api

reload:
	docker-compose up --build --remove-orphans -d eventbrite_api 

down:
	docker-compose down

stop:
	docker-compose stop eventbrite_api

server:
	uvicorn src.main:app --reload --workers=1 --host=0.0.0.0 --port=80