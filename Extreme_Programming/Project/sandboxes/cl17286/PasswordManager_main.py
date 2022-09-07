import csv
import os
import getpass

# from tkinter import messagebox
from datetime import datetime
from trunk.PasswordManager_function import functions
# from trunk.PasswordManager_window import Ui_PasswordManagerWindow
from trunk.PasswordManager_menu import PasswordManagerMenu
from trunk.legacy.loginmenu import *


class on_startup:

    # def __init__(self, PasswordManagerUsername, PasswordManagerAccountNumber, PasswordManagerAccountPassword):
    #     self.PasswordManagerUsername = PasswordManagerUsername
    #     self.PasswordManagerAccountNumber = PasswordManagerAccountNumber
    #     self.PasswordManagerPassword = PasswordManagerAccountPassword
    default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv")
    # @staticmethod
    # def check_username(): # bug fix needed, for multiple user login
    #     password = ""
    #     id = 0
    #     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "r", encoding='utf8') as datafile:
    #         csv_reader = csv.reader(datafile, delimiter=',')
    #         next(csv_reader)
    #         username = input("Username: ")
    #         password = ""
    #         length = on_startup.line_counter(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"))
    #         for line in csv_reader:
    #             if username == line[1]:
    #                 while password == "" or password_check != password:
    #                     password = input("Please enter your password: ")
    #                     password_check = line[2]
    #                     if password_check == password:
    #                         id = line[0]
    #                         username = line[1]
    #                         password = line[2]
    #                         return id, username, password
    #                         break
    #                     else:
    #                         print("Incorrect Password")
    #             else:
    #                 length = length - 1
    #                 if length == 0: print("User non found:")
    @staticmethod
    def check_username():
        password = ""
        id = 0
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "r", encoding='utf8') as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                password = ""
                username = ""
                while username != line[1]:
                    username = input("Username: ")
                    if username == line[1]:
                        while password == "" or password_check != password:
                            password = input("Please enter your password: ")
                            password_check = line[2]
                            if password_check != password:
                                print("Incorrect Password")
                            else:
                                id = line[0]
                                name = line[1]
                                password = line[2]
                                break

                    else:
                        print("User non found:")
        return id, name, password

    @staticmethod
    def line_counter(filename):
        with open(filename,"r", encoding='utf8' ) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    @staticmethod
    def password_checker():
        pass

    @staticmethod
    def call_menu():
        window = QApplication(sys.argv)
        tabdialog = PasswordManagerMenu()
        tabdialog.show()
        window.exec()

    @staticmethod
    def create_account():
        PasswordManagerUsername = input("Please create a username: ")
        # functions.RandomPassWordGen()
        PasswordManagerPassword = ""
        PasswordManagerPassword_check = ""
        while PasswordManagerPassword_check == "" or PasswordManagerPassword != PasswordManagerPassword_check:
            mode ,suggestPassword = functions.RandomPassWordGen()
            if mode == True:
                PasswordManagerPassword = suggestPassword
                PasswordManagerPassword_check = suggestPassword
            elif mode == False:
                PasswordManagerPassword = getpass.getpass("Please create a password: ")
                PasswordManagerPassword_check = getpass.getpass("Please confirm password: ")
            if PasswordManagerPassword != PasswordManagerPassword_check:
                print("Password does not match: ")
        functions.SecurityQuestions()
        question_choice = ''
        while question_choice == '':
            question_choice = input("Please chose a security question(1-4):  ")
            if question_choice == '1':
                security_question = "Your favourite place?"
                print(security_question)
                security_question_answer = input("Answer: ")
            elif question_choice == '2':
                security_question = "Your favourite place?"
                print(security_question)
                security_question_answer = input("Answer: ")
            elif question_choice == '3':
                security_question = "Your favourite place?"
                print(security_question)
                security_question_answer = input("Answer: ")
            elif question_choice == '4':
                security_question = "Your favourite place?"
                print(security_question)
                security_question_answer = input("Answer: ")
            else:
                print("Input not recognised!")
                question_choice = ''
        return PasswordManagerUsername, PasswordManagerPassword, security_question, security_question_answer

    @staticmethod
    def create_account_UI(username,password,password_check,security_question,security_question_answer):
        PasswordManagerUsername = input("Please create a username: ")
        PasswordManagerPassword = ""
        PasswordManagerPassword_check = ""
        while PasswordManagerPassword_check == "" or PasswordManagerPassword != PasswordManagerPassword_check:
            PasswordManagerPassword = getpass.getpass("Please create a password: ")
            PasswordManagerPassword_check = getpass.getpass("Please confirm password: ")
            if PasswordManagerPassword != PasswordManagerPassword_check : print("Password does not match: ")

        return PasswordManagerUsername, PasswordManagerPassword, security_question, security_question_answer

    @staticmethod
    def create_password(id, title, username, password, description, category, email):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", str(id) + "_AccountPassword.csv"),
                  "a+", encoding='utf8', newline="") as datafile:
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerow(
                [on_startup.get_last_id(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", str(id) +
                                                     "_AccountPassword.csv")),id, title, username, password,
                 description, category, email, datetime.today().strftime('%d-%m-%Y')])

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
        with open(on_startup.default_path, "a+", encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow([int(on_startup.get_last_id(on_startup.default_path))+1, PasswordManagerUsername, PasswordManagerPassword, SecurityQuestion, SecurityQuestionAnswer])

    @staticmethod
    def get_last_id(file):
        with open(file, 'r', encoding='utf8') as f:
            for row in reversed(list(csv.reader(f))):
                return(row[0])
                break

    @staticmethod
    def create_account_db(ID):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", str(ID)+"_AccountPassword.csv"),
                  "w", encoding='utf8') as datafile:
            csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
            csv_writer.writerow(
                ['ID', 'UserID', 'Title', 'Username', 'Password', 'Description', 'Category', 'Email', 'Last Updated'])
        return os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", str(ID)+"_AccountPassword.csv"))

    @staticmethod
    def login_check(username,password):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"), "r",
                  encoding='utf8') as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                while username == line[1] and password == line[2]:
                    return True
            return False

    @staticmethod
    def login_onclick(username, password):
        login = None
        login = on_startup.login_check(username,password)
        if login == True:
            print("debug")
            # QtCore.QCoreApplication.instance().quit()
            on_startup.call_menu()
        elif login == False:
            print("test1")
            # messagebox.showwarning(title="Password Manager Message", message="Username or Password incorrect !")
        else:
            print("test2")
            # messagebox.showerror(title="Password Manager Error", message="Error detected please contact support")


    @staticmethod
    def call_login():
        app = QApplication(sys.argv)
        tabdialog = Login()
        tabdialog.show()
        app.exec()
        # app = QtWidgets.QApplication(sys.argv)
        # controller = Controller()
        # controller.show_login()
        # app.exec()


    @staticmethod
    def check_db():
        on_startup.call_login()

    @staticmethod
    def start_ui():
        username, password = on_startup.call_login()
        print(username)
        print(password)

    @staticmethod
    def start():
        logged_in = False
        id = 0
        if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv")):
            mode = None
            while logged_in == False:
                mode = input("Type L to [L]ogin or C to [C]reate account:  ")
                if mode == "L" or mode == "l":
                    id, name, password = on_startup.check_username()
                    logged_in = True
                    print("Welcome back " + name)
                elif mode == "C" or mode == "c":
                    PasswordManagerUsername, PasswordManagerPassword, SecurityQuestion, SecurityQuestionAnswer = on_startup.create_account()
                    id = on_startup.append_csv_user(PasswordManagerUsername, PasswordManagerPassword, SecurityQuestion, SecurityQuestionAnswer)
                    logged_in = True
                else:
                    print("Input not recognise!")

            while logged_in == True:
                mode = input("Type E to [E]nter main menu or L to [L]ist all Password or Q to [Q]uit programme or A to [A]dd password:  ")
                if mode == "E" or mode == "e":
                    on_startup.call_menu()
                elif mode == "L" or mode == "l":
                    on_startup.call_Window()
                elif mode == "a" or mode == "a":
                    title = input("Please create a title: ")
                    username = input("Username of this account: ")
                    password = input("Password for this Account: ")
                    description = input("Brief description: \n")
                    category = input("Please give this password a category: ")
                    email = input("Registered email for this account: ")
                    on_startup.create_password(id, title, username, password, description, category, email)
                elif mode == "Q" or mode == "q":
                    logged_in = False
                    print("Goodbye!")
                else:
                    print("Input not recognise!")
            # input_username = input("Please enter username")

        else:
            try:
                os.mkdir("data/")
            except FileExistsError:
                pass
            PasswordManagerUsername, PasswordManagerPassword, SecurityQuestion, SecurityQuestionAnswer = on_startup.create_account()
            id =1
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"),
                      "w", encoding='utf8') as datafile:
                csv_writer = csv.writer(datafile, delimiter=',', quotechar='"')
                csv_writer.writerow(['ID', 'Username', 'Password','Security Question', 'Answer'])
                csv_writer.writerow([1, PasswordManagerUsername, PasswordManagerPassword, SecurityQuestion,SecurityQuestionAnswer])
            on_startup.create_account_db(1)
            logged_in = True
            while logged_in == True:
                mode = input("Type E to [E]nter main menu or L to [L]ist all Password or Q to [Q]uit programme or A to [A]dd password:  ")
                if mode == "E" or mode == "e":
                    on_startup.call_menu()
                elif mode == "L" or mode == "l":
                    on_startup.call_Window()
                elif mode == "a" or mode == "a":
                    title = input("Please create a unique title: ")
                    username = input("Username of this account: ")
                    password = input("Password for this Account: ")
                    description = input("Brief description: \n")
                    category = input("Please give this password a category: ")
                    email = input("Registered email for this account: ")
                    on_startup.create_password(id,title,username,password,description,category,email)
                elif mode == "Q" or mode == "q":
                    logged_in = False
                    print("Goodbye!")
                else:
                    print("Input not recognise!")


def main():
    on_startup.check_db()


if __name__ == '__main__':
    main()
