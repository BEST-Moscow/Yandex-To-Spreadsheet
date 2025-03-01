import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import logging
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))

# Configuring the logging module to output debug information
logging.basicConfig(level=logging.INFO)

# Setting up constants for Google Sheets API access
# Auth scope for Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def authenticate() -> None:
    """
    Authenticates the user and sets up the Sheets API service.
    """
    try:
        # Load credentials from the service account file and create a Sheets API service
        credentials = Credentials.from_authorized_user_file(
            f"{os.getcwd()}/tokens/api-token.json", SCOPES)
            # f"{os.getcwd()}/tokens/api-token.json", SCOPES)
            # f"./scripts/googleApi/tokens/api-token.json", SCOPES)

        service = build("sheets", "v4", credentials=credentials)
        return service
    except Exception as e:
        logging.error(f"Failed to authenticate: {e}")
        return None  # Ensure the function returns a value even in case of error


def json_to_sheets_data(data):
    """
    Change the json data to the format that Google Api uses

    :param data: Received data from API in json format
    :return: Data in current format to use for spreadsheet
    """

    sheet_data = list()
    for tag in data:
        if data[tag] != "":
            sheet_data.append(str(data[tag]))
        else:
            sheet_data.append("-")

    return sheet_data


def export_data_to_sheets(service, json_data, id, numOfList):
    """
    Updates specific cells in the spreadsheet with new data

    :param service: A Sheets API service instance
    :param json_data: Received data from API in json format
    """

    # Range and sheet on which the data will be placed
    match numOfList:
        case '1':    
            RANGE_NAME = f"{os.getenv('SHEET_LIST_NAME')}!{os.getenv('FIRST_LETTER_OF_COL')}{id[0]}:{os.getenv('LAST_LETTER_OF_COL')}{id[0]}"
        case '2':
            RANGE_NAME = f"{os.getenv('SHEET_LIST_NAME_2')}!{os.getenv('FIRST_LETTER_OF_COL')}{id[1]}:{os.getenv('LAST_LETTER_OF_COL')}{id[1]}"
        case '3':
            RANGE_NAME = f"{os.getenv('SHEET_LIST_NAME_3')}!{os.getenv('FIRST_LETTER_OF_COL')}{id[2]}:{os.getenv('LAST_LETTER_OF_COL')}{id[2]}"

    data = json_to_sheets_data(json_data)

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

    match numOfList:
        case '1':
            id[0] += 1
        case '2':
            id[1] += 1
        case '3':
            id[2] += 1

    # Update the id of the line where next data will be inserted
    with open(f"{os.getcwd()}/id.txt", "w") as file:
        file.write(str(id[0]))

    with open(f"{os.getcwd()}/id_2.txt", "w") as file:
        file.write(str(id[1]))
        
    with open(f"{os.getcwd()}/id_3.txt", "w") as file:
        file.write(str(id[2]))