from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config import SAMPLE_SPREADSHEET_ID

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "key.json"


def write_on_sheets(list_to_write):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=credentials)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="attendes!A2:ZZ10000")
        .execute()
    )
    values = result.get("values", [])

    service.spreadsheets().values().clear(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range="attendes!A2:Z", body={}
    ).execute()

    service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        valueInputOption="RAW",
        range="attendes!A2:Z",
        body=dict(majorDimension="ROWS", values=list_to_write),
    ).execute()
