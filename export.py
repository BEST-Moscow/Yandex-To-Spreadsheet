# Import required modules
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import logging

# Configuring the logging module to output debug information
logging.basicConfig(level=logging.INFO)

# Setting up constants for Google Sheets API access
# Auth scope for Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# ID of the target spreadsheet
# Find the spreadsheet ID in the URL: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}
SPREADSHEET_ID = '1Wfb61dYbtWdfiFJelhky1mdxux3dpFMtPkr7pMbtyTc'
# Path to token JSON
TOKEN_PATH = 'api-token.json'
# The range of cells to update in sheet notation
SAMPLE_RANGE_NAME = 'Лист1!A3:E4'


def authenticate() -> None:
    """
    Authenticates the user and sets up the Sheets API service.
    """
    try:
        # Load credentials from the service account file and create a Sheets API service
        credentials = Credentials.from_authorized_user_file(
            TOKEN_PATH, SCOPES)
        service = build('sheets', 'v4', credentials=credentials)
        return service
    except Exception as e:
        logging.error(f"Failed to authenticate: {e}")
        return None  # Ensure the function returns a value even in case of error


def export_data_to_sheets(service):
    """
    Updates specific cells in the spreadsheet with new data.

    :param service: A Sheets API service instance.
    """
    # Update the range of cells with the given values
    response = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,  # The ID of the spreadsheet to update
        valueInputOption='RAW',  # The values will be parsed exactly as they are input
        range=SAMPLE_RANGE_NAME,  # The range of cells to update
        body=dict(
            majorDimension='ROWS',  # The first dimension of the values array corresponds to rows
            values=[['This', 'is', 'a', 'test...'], [
                'Congrats!', 'It', 'works!']]  # The data to input
        )
    ).execute()
    logging.info(response)
    logging.info('Sheet successfully Updated!')


if __name__ == "__main__":
    # Authenticate to the service and update the sheet
    service = authenticate()
    if service:  # Only attempt to update the sheet if authentication was successful
        export_data_to_sheets(service)
