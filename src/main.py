import json
import random
from datetime import datetime
from typing import Optional

import pandas as pd
import toml
from fastapi import FastAPI, Request
from loguru import logger

from src.libs import eventbrite, google_sheets
from src.libs.settings import API_HASH

app = FastAPI()

ATTENDS_DF=None
ATTENDS_LIST=None

def main():
    logger.info("Starting get attends from event")
    attends = eventbrite.get_event_attendees()
    attendes_array = []

    key_array = load_keys()
    for items in attends:
        attendes_array.append(
            [
                dict_nested_get(items, keys)
                for keys in [item.split("___") for item in key_array]
            ]
        )
    google_sheets.write_on_sheets(attendes_array)
    logger.info("All Attendes imported")


def load_keys():
    return toml.load("./eventbrite_fields.toml").get("attends")

def load_keys_api():
    return toml.load("./eventbrite_fields.toml").get("api_columns")


def dict_nested_get(dic, keys):
    for key in keys:
        dic = dic.get(key)
    return dic

@app.get("/{API_HASH}")
def read_root():
    return {"Hello": "World"}

@app.post("/{API_HASH}/eventbrite/")
async def post(request: Request):
    req_info = await request.json()
    # with open(f'./files/{datetime.now().strftime("%Y%m%d_%s")}_{random.randint(1,99)}_event.json',"w") as file:
    #     file.write(json.dumps(req_info))
    action= req_info.get("config").get("action")
    url = req_info.get("api_url")

    if action == "attendee.updated":
        global ATTENDS_LIST
        ATTENDS_LIST+= eventbrite.get_event_attendee(url)
        parse(ATTENDS_LIST)
        return {
            "status" : "SUCCESS"
    }

    return {
        "status" : "FAIL"
    }

@app.get("/{API_HASH}/attend/")
async def get_attend(field,value):

    filter = f"{field}=='{value}'"
    logger.info(filter)
    filterd = ATTENDS_DF.query(filter).copy()

    if not filterd.empty:
        return {
            "status" : "SUCCESS",
            "data" : filterd.to_json()
        }
    return {
            "status" : "SUCCESS",
            "data" : "Not Found"
        }
    
@app.on_event("startup")             
def app_startup():
    global ATTENDS_LIST
    ATTENDS_LIST = eventbrite.get_event_attendees()
    parse(ATTENDS_LIST)

def parse(parse_list):
    attendes_array = []
    key_array = load_keys_api()
    for items in ATTENDS_LIST:
        attendes_array.append(
            [
                dict_nested_get(items, keys)
                for keys in [item.split("___") for item in key_array]
            ]
        )

    global ATTENDS_DF
    ATTENDS_DF = pd.DataFrame([dict(zip(key_array, item)) for item in attendes_array]).drop_duplicates()

 
if __name__ == "__main__":
    main()
