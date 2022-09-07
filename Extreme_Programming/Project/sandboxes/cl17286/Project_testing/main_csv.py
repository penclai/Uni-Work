import csv
import os
#import PyQt5
#from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)
import sys


class on_startup:
    # def __init__(self, PasswordManagerUsername, PasswordManagerAccountNumber, PasswordManagerAccountPassword):
    #     self.PasswordManagerUsername = PasswordManagerUsername
    #     self.PasswordManagerAccountNumber = PasswordManagerAccountNumber
    #     self.PasswordManagerPassword = PasswordManagerAccountPassword
    @staticmethod
    def start():
        logged_in=False
        id = 0
        if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv")):

            password = ""
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "r") as datafile:
                csv_reader = csv.reader(datafile, delimiter=',')
                next(csv_reader)
                for line in csv_reader:
                    password = ""
                    username = ""
                    while username != line[1]:
                        username = input("Username: ")
                        if username == line[1]:
                            print("Welcome back "+ username)
                            while password == "" or password_check != password:
                                password = input("Please enter your password: ")
                                password_check = line[2]
                                if password_check != password:
                                    print("Incorrect Password")
                                else:
                                    print("Hello " + username + "Please chose a function" )
                                    logged_in = True
                                    id = line[1]
                        else:
                            print("User non found:")
            print(username+id+password)
            print(logged_in)

            # input_username = input("Please enter username")

        else:
            try:
                os.mkdir("data/")
            except FileExistsError:
                pass
            PasswordManagerUsername = input("Please create a username: ")
            PasswordManagerPassword = ""
            PasswordManagerPassword_check = ""
            while PasswordManagerPassword_check == "" or PasswordManagerPassword != PasswordManagerPassword_check:
                PasswordManagerPassword = input("Please create a password: ")
                PasswordManagerPassword_check = input("Please confirm password: ")
                if PasswordManagerPassword != PasswordManagerPassword_check: print("Password does not match: ")

            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "w") as datafile:
                csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
                csv_writer.writerow(['ID', 'Username', 'Password'])
                csv_writer.writerow([ 1 , PasswordManagerUsername, PasswordManagerPassword])
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "1_AccountPassword.csv"), "w") as datafile:
                csv_writer = csv.writer(datafile, delimiter=',', quotechar='"',)
                csv_writer.writerow(['ID', 'UserID', 'Title', 'Username', 'Password', 'Description', 'Category', 'Email'])



            print("Done!")




def main():
    # print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.json"))
    # test = on_startup("Peter", 1, "abcd1234")
    on_startup.start()


if __name__ == '__main__':
    main()
