import gspread
from google.oauth2.service_account import Credentials
from time import sleep

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tool_data_list')
members = SHEET.worksheet('members')
data = members.get_all_values()
DIVIDER = '-' * 30


def welcome():
    print('')
    print(DIVIDER)
    print('')
    print(('Welcome to Tools for borrow').upper())
    print('')
    print(('The place for you to borrow tools from your neighbours').upper())
    print('')
    print(DIVIDER)
    print('')

def main_menu():
    pass

welcome()