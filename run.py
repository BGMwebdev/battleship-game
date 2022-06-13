import gspread
from google.oauth2.service_account import Credentials
import time



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
    """
    Provides a welcome message when program starts running
    """
    print('')
    print(DIVIDER)
    print('')
    print(('Welcome to Tools for borrow').upper())
    print('')
    print(('The place for you to borrow tools from your neighbours').upper())
    print('')
    print(DIVIDER)
    print('')
    

def explanation():
    """
    Provides an explanation for how to use it and what to expect
    """
    time.sleep(2)
    print("To use this application, you first need to register.")
    print("After registration you'll be asked to log in.")
    print("Then you can choose to search or add a tool.")
    print("when you come back next time, just log in!")
    print('')

def registration():
    time.sleep(2)
    fname = input("Please enter your first name: ")
    print(f"Hi {fname}!")
    lname = input("What is your last name? ")
    print(f"we now have you registered as: {fname} {lname}")
    correct = input("Is that correct? y/n ")
    yes = ""
    no = ""
    if correct == y:
        print("Great! We're almost there...")
    elif correct == n:
        print("Let's try that again!")    
    print("To be able to log in, you need to create a unique password.")
    
    

def main():
    welcome()
    explanation()
    registration()

main()