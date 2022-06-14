import gspread
from google.oauth2.service_account import Credentials
import time
import os


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

DIVIDER = '-' * 50


def clear_console():
    """
    This will clear the console
    """
    os.system('clear')


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
    Provides an explanation for how to use the application and what to expect
    """
    time.sleep(2)
    print("To use this application, you first need to register.")
    print("After registration you'll be asked to log in.")
    print("Then you can choose to search or add a tool.")
    print("when you are already registered, just log in!")
    print('')
    time.sleep(1)


def menu():
    """
    Presents two options, to register or to log in
    """
    time.sleep(1)
    print("Please select one of the options and press enter: ")
    menu_options = "1) Register\n2) Log in\n"
    menu_selected = input(menu_options)
    print('')

    # This will validate the answer and check if 1 or 2 is choosen
    while menu_selected not in ('1', '2'):
        print("Please choose option '1' or '2':")
        menu_selected = input(menu_options)
        print('')

    if menu_selected == "1":
        print(f"You choose: {menu_selected}")
        print("Loading...")
        time.sleep(2)
        clear_console()
        registration()
        
    elif menu_selected == "2":
        print(f"You choose: {menu_selected}")
        print("Loading...")
        time.sleep(2)
        clear_console()
        log_in()
        

def registration():
    """
    Registers a resident by asking for data input
    like first name and last name.
    """
    while 'n':
        time.sleep(1)
        fname = input("Please enter your first name:\n")
        print(f"Hi {fname}!")
        time.sleep(1)
        lname = input("What is your last name?\n")
        print("Registering...")
        print('')
        time.sleep(1)
        print(f"we now have you registered as: {fname} {lname}")
        time.sleep(1)
        correct = input("Is that correct? 'y' for yes or 'n' for no:\n")

        while correct not in ('n', 'y'):
            print('')
            print(f"'y' or 'n' is requirred, you provided {correct}.")
            time.sleep(1)
            correct = input("'y' for yes or 'n' for no:\n")
            
        if correct == 'n':
            print('')
            print("Let's try that again!") 
            
        elif correct == 'y':
            print('')
            print("Great! We're almost there...")
            break  

        
def create_psswd():
    """
    Create a unique password.
    """
    time.sleep(1)
    print("To be able to log in, you need to create a unique password.")
    time.sleep(1)
    while True:
        print("Your password should have at least 6 characters.")
        print("It also should contain at least 1 digit.")
        try: 
            password = input("please enter your unique password:\n")
          


def log_in():
    """
    This will activate the log in sequence 
    """
    print("Log in Function under construction...")


def main():
    """
    This is the main function, that will run the application
    """
    welcome()
    explanation()
    menu() 


main()
