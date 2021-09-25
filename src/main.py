import json
import random
from datetime import datetime
from typing import Optional

import toml
from fastapi import FastAPI, Request
from loguru import logger

from src.libs import eventbrite, google_sheets
from src.libs.settings import API_HASH

app = FastAPI()

def main():
    logger.info("Starting get attends from event")
    attends = eventbrite.get_event_attendees()
    attendes_array = []

    key_array = load_keys()
    for items in attends:
        attendes_array.append(
            [
                dict_nested_get(items, keys)
                for keys in [item.split(":") for item in key_array]
            ]
        )
    google_sheets.write_on_sheets(attendes_array)
    logger.info("All Attendes imported")


def load_keys():
    return toml.load("./eventbrite_fields.toml").get("attends")


def dict_nested_get(dic, keys):
    for key in keys:
        dic = dic.get(key)
    return dic

@app.get("/{API_HASH}")
def read_root():
    return {"Hello": "World"}

@app.post("/eventbrite/{API_HASH}")
async def post(request: Request):
    req_info = await request.json()
    with open(f'./files/{datetime.now().strftime("%Y%m%d_%s")}_{random.randint(1,99)}_event.json',"w") as file:
        file.write(json.dumps(req_info))

    return {
        "status" : "SUCCESS",
        "data" : req_info
    }

@app.get("/{API_HASH}/items/{item_id}")
def search_attend(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    main()
