# Import required modules
import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import logging
from dotenv import load_dotenv

load_dotenv()

# Configuring the logging module to output debug information
logging.basicConfig(level=logging.INFO)

# Setting up constants for Google Sheets API access
# Auth scope for Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The range of cells to update in sheet notation
counter = 2
RANGE_NAME = f"{os.getenv('SHEET_LIST_NAME')}!A{counter}:E{counter}"


def authenticate() -> None:
    """
    Authenticates the user and sets up the Sheets API service.
    """
    try:
        # Load credentials from the service account file and create a Sheets API service
        credentials = Credentials.from_authorized_user_file(
            os.getenv('TOKEN_PATH'), SCOPES)
        service = build("sheets", "v4", credentials=credentials)
        return service
    except Exception as e:
        logging.error(f"Failed to authenticate: {e}")
        return None  # Ensure the function returns a value even in case of error


def json_to_sheets_data(data):
    sheet_data = list()
    for tag in data:
        sheet_data.append(str(data[tag]))

    return sheet_data


def export_data_to_sheets(service, json_data):
    """
    Updates specific cells in the spreadsheet with new data.

    :param service: A Sheets API service instance.
    """

    data = str(json_to_sheets_data(json_data))

    # Update the range of cells with the given values
    response = service.spreadsheets().values().update(
        spreadsheetId=os.getenv('SPREADSHEET_ID'),  # The ID of the spreadsheet to update
        valueInputOption='RAW',  # The values will be parsed exactly as they are input
        range=RANGE_NAME,  # The range of cells to update
        body=dict(
            majorDimension='ROWS',  # The first dimension of the values array corresponds to rows
            values=[data]  # The data to input
        )
    ).execute()
    logging.info(response)
    logging.info("Sheet successfully Updated!")
