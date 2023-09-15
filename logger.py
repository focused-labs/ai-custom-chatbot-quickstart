from __future__ import print_function

import base64
import os
import pickle
from datetime import datetime

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()


def authenticate():
    creds = None

    token_base64 = os.getenv("GOOGLE_CREDS_TOKEN")
    if token_base64:
        token_data = base64.b64decode(token_base64)

        creds = pickle.loads(token_data)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../service_account_credentials.json', ['https://www.googleapis.com/auth/drive.file',
                                                        'https://www.googleapis.com/auth/spreadsheets'])
            creds = flow.run_local_server(port=0)
            token_data = pickle.dumps(creds)

            token_base64 = base64.b64encode(token_data).decode()
            print("GOOGLE_CREDS_TOKEN in Base64:", token_base64)

    return creds


def save_question(question, answer, sheet_id=os.getenv("GOOGLE_API_SPREADSHEET_ID"),
                  sheet_range=os.getenv("GOOGLE_API_RANGE_NAME"), session_id=""):
    try:
        creds = authenticate()
        sources = "\n".join([i['URL'] for i in answer["sources"]]) if len(answer["sources"]) > 0 else ""
        append_values(creds, sheet_id,
                      sheet_range, "USER_ENTERED",
                      [
                          [
                              str(datetime.utcnow()),
                              str(session_id),
                              question,
                              answer["result"],
                              sources
                          ]
                      ])
    except Exception as e:
        print(f"Error returned from google authentication: {e}")


def save_error(question, message, sheet_id=os.getenv("GOOGLE_API_SPREADSHEET_ID"),
               sheet_range=os.getenv("GOOGLE_API_RANGE_NAME"), session_id=""):
    try:
        creds = authenticate()
        append_values(creds, sheet_id, sheet_range,
                      "USER_ENTERED",
                      [
                          [
                              str(datetime.utcnow()),
                              str(session_id),
                              question,
                              "",
                              "",
                              message
                          ]
                      ])
    except Exception as e:
        print(f"Error returned from google authentication: {e}")


def create_sheet_in_folder(sheet_name, folder_id, sheet_range=None, sheet_data=None):
    creds = authenticate()

    drive_service = build('drive', 'v3', credentials=creds, cache_discovery=False)

    file_metadata = {
        'name': sheet_name,
        'mimeType': 'application/vnd.google-apps.spreadsheet',
        'parents': [folder_id]
    }

    file = drive_service.files().create(body=file_metadata, fields='id', supportsAllDrives=True).execute()

    if sheet_data is not None:
        append_values(creds, file.get('id'), sheet_range, "USER_ENTERED", sheet_data)

    print('Created new spreadsheet: https://docs.google.com/spreadsheets/d/%s' % file.get('id'))
    return file.get('id')


def append_values(creds, sheet_id, range_name, value_input_option, values):
    try:
        sheet_service = build('sheets', 'v4', credentials=creds, cache_discovery=False)

        body = {
            'values': values
        }
        result = sheet_service.spreadsheets().values().append(
            spreadsheetId=sheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        return result

    except HttpError as error:
        print(f"An error occurred when trying to append values to google sheet {sheet_id}: {error}")
        return error
