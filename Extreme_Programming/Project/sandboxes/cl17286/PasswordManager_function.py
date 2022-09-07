import random
import string
import re

class functions:
    #RandomPassWordGen(mode, length): to get rid of while loop.
    #when called, call with user choice in brackets. No user input apart from characters and length.
    # https://pynative.com/python-generate-random-string/ Will probably need to put a reference here idk
    @staticmethod
    def RandomPassWordGen(passwordgenchoice):  #This should be taken from the UI
        wantsuggestion = True
        while wantsuggestion != False:
            passwordgenchoice = input("Would you like to be suggested a password y/n?")  # Asking user if they want password suggestion
            if passwordgenchoice == 'y' or passwordgenchoice == 'Y':
                userlength = input("Please enter how many characters you would like in the password (between 8 and 24):")
                length = int(userlength)  # Convert user input to integer
                wantsuggestion = False
                if length <= 24 and length >= 8:  # Making sure only a password of reasonable length is created
                    characters = string.ascii_letters + string.digits + string.punctuation  # Characters variable stores all characters
                    newpassword = ''.join(random.choice(characters) for i in range(length))  # Characters are selected at random and are joined
                    print("Strong Password: ", newpassword)  # New password is printed
                    return True
                else:
                    print("Please enter a number between 8 and 24")  # Unless a number outside the boundaries is entered.
            elif passwordgenchoice == 'n' or passwordgenchoice == 'N':
                wantsuggestion = False
                return False
            else:
                print("input not recognise")

    @staticmethod
    def RandomPassWordGen_UI(password_length):  # This should be taken from the UI
        length = int(password_length)  # Convert user input to integer
        if length <= 24 and length >= 8:  # Making sure only a password of reasonable length is created
            characters = string.ascii_letters + string.digits + string.punctuation  # Characters variable stores all characters
            newpassword = ''.join(random.choice(characters) for i in range(length))  # Characters are selected at random and are joined
            return newpassword
        else:
            return ""

    @staticmethod
    def PassStrengthCheck(password):
        if (len(password) >= 8 and len(password)<=24):
            if (bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*"£^\[\]\(\)\>\<\?\|\/-]).{8,24})', password)) == True):
                print("The password is strong")
            elif (bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*"£^\[\]\(\)\>\<\?\|\/-]*).{8,24})', password)) == True):
                print("The password is weak")
        else:
            print("The password is too short or invalid. Please try again ")

    @staticmethod
    def SecurityQuestions():
        global selection
        while True:
            print("Please pick a security question:\n")  # user input
            menu = ["Your favourite place?", "What is your favourite colour?", "Your first school?", "Your pet name?", "Exit"]
            for i in range(len(menu)):
                print(' [{}] {}'.format(i + 1, menu[i]))
            try:
                selection = int(input("Selection: "))
            except ValueError:
                print("Invalid selection")
            except IndexError:
                print("Invalid selection")
            except KeyboardInterrupt:
                print("\nExiting.")
                break

            if selection == 1:
                print("Your favourite place?")
            elif selection == 2:
                print("What is your favourite colour?")
            elif selection == 3:
                print("Your first school?")
            elif selection == 4:
                print("Your pet name?")
            elif selection == 5:
                print("\nExiting.... back to security questions")


    @staticmethod
    def questions(mode):
        if mode ==1:
            question_list =["Your favourite place?","What is your favourite colour?","Your first school?","Your pet name?","What is your favourite driver?"]
            return question_list

    @staticmethod
    def categories():
        category_list = ["Email", "Work", "Study", "Entertainment", "Programming","Shopping","Software", "Others"]
        return category_list

def main():
    # functions.RandomPassWordGen()
    print(functions.RandomPassWordGen_UI(10))
    print(functions.SecurityQuestions())

if __name__ == "__main__":
    main()