__author__ ="penclai"

import random
import string
import re

class functions:
    #RandomPassWordGen(mode, length): to get rid of while loop.
    #when called, call with user choice in brackets. No user input apart from characters and length.

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
    def check(lower, upper, special, number, password):

        lowercasechar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercasechar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numberchar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        specialchar = ['!', '£', '$', '%', '"', '^', '&', '(', ')', '-', '_', '+', '=', '[', ']', '@', '#', '~', ':', ';', '?', '.', '|', '/', ',', '<', '>', '*']
        # This loop will check if the required characters are present in the password
        if lower == True:
            if not any(char in password for char in lowercasechar): return False
        if upper == True:
            if not any(char in password for char in uppercasechar): return False
        if special == True:
            if not any(char in password for char in specialchar): return False
        if number == True:
            if not any(char in password for char in numberchar): return False
        return True

    @staticmethod
    def Iteration2PassGen(lower,upper,special,number,length):
        # These maps contain all characters that can be used to make the password.
        lowercasechar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercasechar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numberchar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        specialchar = ['!', '£', '$', '%', '"', '^', '&', '(', ')', '-', '_', '+', '=', '[', ']', '@', '#', '~', ':', ';', '?', '.', '|', '/', ',', '<', '>', '*']
        # Blank password initialised as a string
        password = ""
        # This map is used to randomly select which character to add
        mode = [1, 2, 3, 4]
        counter = 0
        while counter < length: # Simple while loop that will add a count when a
                                # character is added till a password matching the required length is created
            random_mode = random.choice(mode) # Mode is chosen randomly
            if lower == True and random_mode == 1:   # If a character is wanted and the mode is appropriate the character is added
                password += random.choice(lowercasechar)    # This is done to achieve unique passwords.
                counter += 1                                # Counter is added to to eventually terminate the loop.
            elif upper == True and random_mode == 2:
                password += random.choice(uppercasechar)
                counter += 1
            elif special == True and random_mode == 3:
                password += random.choice(specialchar)
                counter += 1
            elif number == True and random_mode == 4:
                password += random.choice(numberchar)
                counter += 1
            if counter == length:
                if functions.check(lower, upper, special, number, password):    # If the appropriate characters are present
                                                                                # Then the password is returned
                    return password
                else:
                    counter = 0     # If not all characters are present then the loop repeats till a suitable one is generated
                    password = ""



    @staticmethod
    def PassStrengthCheck(password):
        if (len(password) >= 8 and len(password)<12):
            if (bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*"£^\[\]\(\)\>\<\?\|\/-]).{8,24})', password)) == True):
                return "Strong"
            elif (bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*"£^\[\]\(\)\>\<\?\|\/-]*).{8,24})', password)) == True):
                return "Medium"
        elif (len(password) >= 12):
            if (bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*"£^\[\]\(\)\>\<\?\|\/-]).{8,24})', password)) == True):
                return "Very Strong"
            elif (bool(
                re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*"£^\[\]\(\)\>\<\?\|\/-]*).{8,24})', password)) == True):
                return "Medium"
        else:
            return "Weak"

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