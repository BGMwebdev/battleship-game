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

DIVIDER = '-' * 50


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
    print("when you come back next time, just log in!")
    print('')
    time.sleep(1)

def registration():
    """
    Registers a resident by asking for data input
    like first name and last name.
    """
    while 'n':
        time.sleep(1)
        fname = input("Please enter your first name: ")
        print(f"Hi {fname}!")
        time.sleep(1)
        lname = input("What is your last name? ")
        print("Registering...")
        time.sleep(1)
        print(f"we now have you registered as: {fname} {lname}")
        time.sleep(1)
        correct = input("Is that correct? 'y' for yes or 'n' for no: ")
        while correct != 'n' and correct != 'y':
            print(f"'y' or 'n' is requirred, you provided {correct}.")
            time.sleep(1)
            y_or_n = input("'y' for yes or 'n' for no: ")
            if y_or_n == 'n':
                print("Let's try that again!") 
                break
            elif y_or_n == 'y':
                print("Great! We're almost there...")
                break  
        if correct == 'n':
            print("Let's try that again!")
        elif correct == 'y':
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
            password = input("please enter your unique password: ")
            if password == len(>=6):
        except ValueError as e:
            print("Both values have to be integers.")
    except Exception:
        print('Another error has occurred')
        except:
            print("Your input doesn't suffice! Let's try that again!")
        else:
            print("Your password is valid!")
            break
        time.sleep(1)



def main():
    welcome()
    explanation()
    registration()
    create_psswd()


main()