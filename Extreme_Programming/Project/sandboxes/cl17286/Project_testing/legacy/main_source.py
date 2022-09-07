import json
import os
import PyQt5
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)
import sys


class on_startup:
    # def __init__(self, PasswordManagerUsername, PasswordManagerAccountNumber, PasswordManagerAccountPassword):
    #     self.PasswordManagerUsername = PasswordManagerUsername
    #     self.PasswordManagerAccountNumber = PasswordManagerAccountNumber
    #     self.PasswordManagerPassword = PasswordManagerAccountPassword
    @staticmethod
    def start():
        if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/UserAccount.json")):
            with open("../data/UserAccount.json", 'r') as user_account_data:
                datafile = json.load(user_account_data)
            input_username = input("Please enter username")

        else:
            try:
                os.mkdir("../data/")
            except FileExistsError:
                pass
            PasswordManagerUsername = input("Please create a username: ")
            PasswordManagerPassword = ""
            PasswordManagerPassword_check = ""
            while PasswordManagerPassword_check == "" or PasswordManagerPassword != PasswordManagerPassword_check:
                PasswordManagerPassword = input("Please create a password: ")
                PasswordManagerPassword_check = input("Please confirm password: ")
                if PasswordManagerPassword != PasswordManagerPassword_check: print("Password does not match: ")

            userdata = {"1": {"UserName": str(PasswordManagerUsername),
                              "Password": str(PasswordManagerPassword)}}
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/UserAccount.json"), "w") as datafile:
            json.dump(userdata, datafile, sort_keys=False, indent=4)

        print("Done!")


#     @staticmethod
#     def input_box():
#         name, done1 = PyQt5.QtWidgets.QInputDialog.getText()
#
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # Add button
#         self.btn = QPushButton('Show Input Dialog', self)
#         self.btn.move(30, 20)
#         self.btn.clicked.connect(self.showDialog)
#         # Add label
#         self.le = QLabel(self)
#         self.le.move(30, 62)
#         self.le.resize(400,22)
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Input dialog')
#         self.show()
#
#
#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter text:')
#         if ok:
#             self.le.setText(str(text))


# class AccountManager:
#     def __init__(self, PasswordManagerUsername, PasswordManagerAccountNumber, PasswordManagerAccountPassword):
#         self.PasswordManagerUsername = PasswordManagerUsername
#         self.PasswordManagerAccountNumber = PasswordManagerAccountNumber
#         self.PasswordManagerPasswordID = PasswordManagerAccountPassword
#
#     def return_ID(self):
#         return self.PasswordManagerAccountNumber
#
#
# class password(AccountManager):
#     def __init__(self, PasswordManagerAccountNumber, PasswordManagerPasswordID, AccountName, AccountUsername, AccountPassword):
#         # AccountManager.return_ID()
#         AccountManager.__init__(self, PasswordManagerAccountNumber)
#         self.PasswordManagerPasswordID = PasswordManagerPasswordID
#         self.AccountName = AccountName
#         self.AccountUsername = AccountUsername
#         self.AccountPassword = AccountPassword


def main():
    # print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.json"))
    # test = on_startup("Peter", 1, "abcd1234")
    on_startup.start()


if __name__ == '__main__':
    main()
