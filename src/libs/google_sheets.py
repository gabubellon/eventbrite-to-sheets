import socket

from google.oauth2 import service_account
from googleapiclient.discovery import build
from loguru import logger

from .settings import (GOOGLE_SERVICE_ACCOUNT, SHEET_HEADER, SHEET_ID,
                          SHEET_RANGE)

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "key.json"


def write_on_sheets(list_to_write):
    socket.setdefaulttimeout(600)  # set timeout to 10 minutes

    logger.info("Creating Google Connection...")

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=credentials)

    logger.info(f"Cleanning Sheets..")
    service.spreadsheets().values().clear(
        spreadsheetId=SHEET_ID, range=SHEET_RANGE, body={}
    ).execute()

    list_to_write.insert(0, SHEET_HEADER)

    logger.info(f"Update Sheets..")
    service.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        valueInputOption="RAW",
        range=SHEET_RANGE,
        body=dict(majorDimension="ROWS", values=list_to_write),
    ).execute()

    logger.info(f"Sheets Updated.")
