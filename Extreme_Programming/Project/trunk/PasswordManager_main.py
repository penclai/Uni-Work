__author__ ="penclai"

import csv
import os
import getpass

from cryptography.fernet import Fernet
from tkinter import messagebox
import sys
from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from trunk.PasswordManager_function import functions
# from PasswordManager_function import functions
"""
<<<<<<< .mine
from trunk.PasswordManager_menu import PasswordManagerMenu
||||||| .r102
from trunk.PasswordManager_menu import PasswordManagerMenu
=======
# from trunk.PasswordManager_menu import PasswordManagerMenu
>>>>>>> .r106
"""

# def __init__(self, PasswordManagerUsername, PasswordManagerAccountNumber, PasswordManagerAccountPassword):
#     self.PasswordManagerUsername = PasswordManagerUsername
#     self.PasswordManagerAccountNumber = PasswordManagerAccountNumber
#     self.PasswordManagerPassword = PasswordManagerAccountPassword
class PasswordManager_main():
    default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv")
    global_account_ID = 0
    global_username = ""
    global_password = ""

    def __init__(self, PasswordManagerUsername, PasswordManagerAccountPassword, PasswordManagerAccountNumber = None):
        self.PasswordManagerUsername = PasswordManagerUsername
        self.PasswordManagerPassword = PasswordManagerAccountPassword
        self.PasswordManagerAccountNumber = PasswordManagerAccountNumber

    # def check_username(self):
    #     password = ""
    #     id = 0
    #     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "r", encoding='utf8') as datafile:
    #         csv_reader = csv.reader(datafile, delimiter=',')
    #         next(csv_reader)
    #         for line in csv_reader:
    #             password = ""
    #             username = ""
    #             while username != line[1]:
    #                 username = input("Username: ")
    #                 if username == line[1]:
    #                     while password == "" or password_check != password:
    #                         password = input("Please enter your password: ")
    #                         password_check = line[2]
    #                         if password_check != password:
    #                             print("Incorrect Password")
    #                         else:
    #                             id = line[0]
    #                             name = line[1]
    #                             password = line[2]
    #                             break
    #
    #                 else:
    #                     print("User non found:")
    #     return id, name, password

    @staticmethod
    def line_counter(filename):
        with open(filename,"r", encoding='utf8' ) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    @staticmethod
    def password_checker():
        pass

    # @staticmethod
    # def call_menu():
    #     window = QApplication(sys.argv)
    #     tabdialog = PasswordManagerMenu()
    #     tabdialog.show()
    #     window.exec()

    # @staticmethod
    # def create_account():
    #     PasswordManagerUsername = input("Please create a username: ")
    #     # functions.RandomPassWordGen()
    #     PasswordManagerPassword = ""
    #     PasswordManagerPassword_check = ""
    #     while PasswordManagerPassword_check == "" or PasswordManagerPassword != PasswordManagerPassword_check:
    #         mode ,suggestPassword = functions.RandomPassWordGen()
    #         if mode == True:
    #             PasswordManagerPassword = suggestPassword
    #             PasswordManagerPassword_check = suggestPassword
    #         elif mode == False:
    #             PasswordManagerPassword = getpass.getpass("Please create a password: ")
    #             PasswordManagerPassword_check = getpass.getpass("Please confirm password: ")
    #         if PasswordManagerPassword != PasswordManagerPassword_check:
    #             print("Password does not match: ")
    #     functions.SecurityQuestions()
    #     question_choice = ''
    #     while question_choice == '':
    #         question_choice = input("Please chose a security question(1-4):  ")
    #         if question_choice == '1':
    #             security_question = "Your favourite place?"
    #             print(security_question)
    #             security_question_answer = input("Answer: ")
    #         elif question_choice == '2':
    #             security_question = "Your favourite place?"
    #             print(security_question)
    #             security_question_answer = input("Answer: ")
    #         elif question_choice == '3':
    #             security_question = "Your favourite place?"
    #             print(security_question)
    #             security_question_answer = input("Answer: ")
    #         elif question_choice == '4':
    #             security_question = "Your favourite place?"
    #             print(security_question)
    #             security_question_answer = input("Answer: ")
    #         else:
    #             print("Input not recognised!")
    #             question_choice = ''
    #     return PasswordManagerUsername, PasswordManagerPassword, security_question, security_question_answer

    @staticmethod
    def create_account_UI(username,password,security_question,security_question_answer):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"),
                  "a+", encoding='utf8', newline="") as datafile:
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerow(
                [(int(PasswordManager_main.get_last_id(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv")))+1), username,password,
                 security_question,security_question_answer]
            )



    @staticmethod
    def password_name_checker(name,id):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"), "r", encoding='utf8') as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                try:
                    if int(id) == int(line[1]) and name == line[2]: return True
                except:
                    pass
        return False

    @staticmethod
    def create_password(id, title, username, password, description, category, email):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", str(id) + "_AccountPassword.csv"),
                  "a+", encoding='utf8', newline="") as datafile:
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerow(
                [PasswordManager_main.get_last_id(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", str(id) +
                                                     "_AccountPassword.csv")),id, title, username, password,
                 description, category, email, datetime.today().strftime('%d-%m-%Y')])

    @staticmethod
    def create_password_ui(id, title, username, password, description, category, email, strength):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"),
                  "a+", encoding='utf8', newline="") as datafile:
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerow(
                [(int(PasswordManager_main.get_last_id(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv")))+1),id, title, username, password,
                 description, category, email, datetime.today().strftime('%d/%m/%Y'),datetime.today().strftime('%d/%m/%Y'),strength])

    @staticmethod
    def username_checker(username):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "r", encoding='utf8') as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                if username == line[1]: return True

    @staticmethod
    def empty_checker(value):
        return True if len(value) == 0 else False

    @staticmethod
    def append_csv_user(PasswordManagerUsername, PasswordManagerPassword, SecurityQuestion, SecurityQuestionAnswer):
        with open(PasswordManager_main.default_path, "a+", encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow([int(PasswordManager_main.get_last_id(PasswordManager_main.default_path))+1, PasswordManagerUsername, PasswordManagerPassword, SecurityQuestion, SecurityQuestionAnswer])

    @staticmethod
    def get_last_id(file):
        with open(file, 'r', encoding='utf8') as f:
            for row in reversed(list(csv.reader(f))):
                # print(row)
                try:
                    if row == [] or str(row[0]) == "ID" or str(row[0]) == "" :
                        return 0
                    else:
                        return(row[0])
                except:
                    pass
        return 0

    @staticmethod
    def create_password_db():
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"),
                  "w", encoding='utf8') as datafile:
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerow(
                ['ID', 'UserID', 'Name', 'Username', 'Password', 'Description', 'Category', 'Email', 'Created_Date','Updated_Date','Strength'])
        return os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"))

    @staticmethod
    def create_account_db():
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\UserAccount.csv"),
                  "w", encoding='utf8') as datafile:
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerow(
                ['ID', 'Username', 'Password', 'Security Question', 'Answer'])


    @staticmethod
    def change_password(ID,new_password):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\UserAccount.csv"), "r",
                  encoding='utf8') as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')
            old_list=list(csv_reader)
        print(old_list)
        new_list = []
        first_line = True
        for line in old_list:
            if first_line:
                new_list.append(line)
                first_line = False
            elif ID == int(line[0]):
                temp = []
                for i in range(0,5):
                    if i != 2 :
                        temp.append(line[i])
                    else:
                        temp.append(str(new_password))
                new_list.append(temp)
            else:
                new_list.append(line)

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\UserAccount.csv"), "w+",
                  encoding='utf8', newline="") as datafile:
            # for i in range(0,len(new_list)):
            #     new_list[i][]
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerows(new_list)
            # for line in new_list:
            #     csv_writer.writerow(line)

            # csv_writer.writerow(new_list)




        # open csv
        # csv_reader
        # new_csv
        # for line in csv_reader:
        #     new_csv.append
        #     if ID == line[0]:
        #         line[2]
    @staticmethod
    def get_all_passwordname(ID):
        pass

    @staticmethod
    def login_check(username,password):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\UserAccount.csv"), "r",
                  encoding='utf8') as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                while username == line[1] and password == line[2]:
                    return True, username ,password, int(line[0])
            return False,"","",0



# def main():
#     pass
#     print(PasswordManager_main.get_last_id(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\AccountPassword.csv")))
#     PasswordManager_main.check_db()
#     PasswordManager_main.create_account_UI("ishi","largeScale", "abcd", "abcd")
#     PasswordManager_main.change_password(1,"abcd")
#
#
# if __name__ == '__main__':
#     main()
