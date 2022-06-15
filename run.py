import gspread
from google.oauth2.service_account import Credentials
import time
import os
import re


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
        time.sleep(1)
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
        # This will make sure to have no digits in the name
        while fname.isalpha() is False:
            print(f"Letters are required, you provided: {fname}")
            print('')
            fname = input("Please enter your first name again:\n")
        
        update_fname = name_correct(fname)
        print(f"Hi {update_fname}!")
        print('')
        time.sleep(1)

        lname = input("What is your last name?\n")
        # This will make sure to have no digits in the name
        while lname.isalpha() is False:
            print(f"Letters are required, you provided: {lname}")
            print('')
            lname = input("Please enter your last name again:\n")

        update_lname = name_correct(lname)
        print("Registering...")
        print('')
        time.sleep(1)

        print(f"we now have you registered as: {update_fname} {update_lname}")
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
            reg_input = f'{update_fname} ' + f'{update_lname}'
            input_list = reg_input.split(" ")
            update_member_worksheet(input_list)
            print('')
            print("Great! We're almost there...\n")
            time.sleep(3)
            clear_console()
            break
    create_psswd()


def name_correct(data):
    """
    This will make sure spaces are considered in the name
    and the names are capitalized before going into the spreadsheet
    """
    name_correct = (data).capitalize().replace(' ', '_')
    return name_correct


def update_member_worksheet(data):
    """
    This will update the members worksheet
    in the google spreadsheet, and add a new row
    to the list
    """
    print("Updating members list...\n")
    members_worksheet = SHEET.worksheet("members")
    members_worksheet.append_row(data)
    time.sleep(1)
    print("Member registration completed!")


def create_psswd():
    """
    Create a unique password.
    """
    time.sleep(1)
    print("To be able to log in, you need to create a unique password.")
    print('')
    time.sleep(1)
    print("Here are some rules...")
    print('')
    print("Your password should have at least 6 characters")
    print("At least 1 uppercase")
    print("At least 1 lowercase")
    print("At least 1 digit")
    print("And no spaces")
    print('')
    time.sleep(2)
    while True: 
        password = input("please enter your unique password:\n")
        if (password_check(password)):
            print("Password is valid")
            print("Updating password...\n")
            convert_psswd_to_string(password)
            save_psswd(convert_psswd_to_string)
            time.sleep(1)
            print("Password registration completed!")
            time.sleep(1)
            print('')
            print("You are now ready to log in!")
            break
   

def password_check(password):
    """
    Checks if password is valid
    """
    val = True
      
    if len(password) < 6:
        print('length should be at least 6')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
    
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
    
    if not any(char.isdigit() for char in password):
        print('Password should have at least one digit')
        val = False
    
    if val:
        return val


def save_psswd(password):
    """
    This will save the password to the spreadsheet column of password
    """
    members_worksheet = SHEET.worksheet('members')    
    psswd_column = members_worksheet.col_values(3)
    psswd_column.append(password)


def convert_psswd_to_string(password):
    """
    This will convert the password to a list to be added to the spreadsheet
    """
    list_psswd = (password).split(" ")
    return list_psswd


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
