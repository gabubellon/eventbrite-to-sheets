import json

import requests
from loguru import logger

from settings import EVENTBRITE_API_URL, EVENTBRITE_EVENT_ID, EVENTBRITE_TOKEN


def get_event_attendees():

    url = EVENTBRITE_API_URL + f'events/{EVENTBRITE_EVENT_ID}/attendees/?token={EVENTBRITE_TOKEN}'
    response = requests.get(url)
    continuation = json.loads(response.text).get("pagination").get("continuation")
    page_number = json.loads(response.text).get("pagination").get("page_number")
    page_count = json.loads(response.text).get("pagination").get("page_count")
    has_more_items = json.loads(response.text).get("pagination").get("has_more_items")
    attendees = json.loads(response.text).get("attendees")

    logger.info(f"Reading attendees page {page_number} of {page_count}...")

    while True:
        if has_more_items:
            response = requests.get(url + f"&continuation={continuation}")
            continuation = (
                json.loads(response.text).get("pagination").get("continuation")
            )
            page_number = json.loads(response.text).get("pagination").get("page_number")
            has_more_items = (
                json.loads(response.text).get("pagination").get("has_more_items")
            )
            attendees += json.loads(response.text).get("attendees")
            logger.info(f"Reading attendees page {page_number} of {page_count}")
        else:
            break
    
    return attendees
