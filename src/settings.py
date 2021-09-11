from decouple import Csv, config

EVENTBRITE_TOKEN = config("EVENTBRITE_TOKEN")
EVENTBRITE_EVENT_ID = config("EVENTBRITE_EVENT_ID")
EVENTBRITE_API_URL = config("EVENTBRITE_API_URL")


GOOGLE_SERVICE_ACCOUNT = config("GOOGLE_SERVICE_ACCOUNT")
SHEET_ID = config("SHEET_ID")
SHEET_RANGE = config("SHEET_RANGE")
SHEET_HEADER = config("SHEET_HEADER", cast=Csv())
