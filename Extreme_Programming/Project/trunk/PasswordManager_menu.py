__author__ ="penclai"

from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QComboBox, QCheckBox, QGroupBox, QVBoxLayout, QWidget, \
    QLabel, QLineEdit, QDialogButtonBox, QAction, qApp, QMenuBar, QPlainTextEdit, QMessageBox, QTableWidget, \
    QTableWidgetItem, QStatusBar, QMainWindow
from PyQt5.QtCore import *
import pandas as pd
import re
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import csv
from trunk.PasswordManager_main import *
from trunk.PasswordManager_function import functions


# from PasswordManager_main import PasswordManager_main
# from PasswordManager_function import functions

class Login(QtWidgets.QWidget):
    # switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Password Manager Log In')
        self.resize(500, 120)
        # layout = QVBoxLayout()
        layout = QtWidgets.QGridLayout()
        menubar = QMenuBar()  # menu bar
        self.exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(qApp.quit)
        self.helpAct = QAction('Help')
        fileMenu = menubar.addMenu('&Application')
        helpMenu = menubar.addMenu('Help')  # add item to menu bar
        self.actionAbout = QtWidgets.QAction(self)  # subitem
        self.actionAbout.setObjectName("actionAbout")
        self.forgetPassword = QtWidgets.QAction(self)
        self.forgetPassword.setObjectName("forgetPassword")
        helpMenu.addAction(self.helpAct)
        helpMenu.addAction(self.forgetPassword)
        helpMenu.addAction(self.actionAbout)  # add submenu item to help
        self.actionAbout.setText("About")
        self.actionAbout.setShortcut('F1')
        self.actionAbout.triggered.connect(lambda: self.showInfo())  # set submenu name
        self.forgetPassword.setText("Forget Password")
        self.forgetPassword.triggered.connect(lambda: self.showRecoverAccount())
        fileMenu.addAction(self.exitAct)
        layout.addWidget(menubar, 0, 0, 1, 0)
        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 1, 0)
        layout.addWidget(self.lineEdit_username, 1, 1)
        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 2, 0)
        layout.addWidget(self.lineEdit_password, 2, 1)

        self.button_login = QtWidgets.QPushButton('Login')
        self.button_login.setShortcut("Return")
        self.button_login.clicked.connect(lambda: self.login())
        self.button_create_account = QtWidgets.QPushButton('Create Account', default=False, autoDefault=False)
        self.button_create_account.clicked.connect(lambda: self.showCreateAccount())
        # self.button.clicked.connect(lambda: on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        layout.addWidget(self.button_create_account)
        layout.addWidget(self.button_login)
        self.setLayout(layout)

    @pyqtSlot()
    def login(self):
        result, username, password, ID = PasswordManager_main.login_check(str(self.lineEdit_username.text()),
                                                                          str(self.lineEdit_password.text()))
        if result == True:
            self.cams = PasswordManagerMenu(username, password, ID)
            self.cams.show()
            self.close()
        elif result == False:
            QtWidgets.QMessageBox.warning(self, "Password Manager Notification", "Incorrect Username or Password!",
                                          QtWidgets.QMessageBox.Ok)

    @pyqtSlot()
    def showRecoverAccount(self):
        self.cams = recover_account()
        self.cams.show()
        self.close()

    def showCreateAccount(self):
        self.cams = create_account()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def showInfo(self):
        QtWidgets.QMessageBox.about(self, "Password Manager About",
                                    "<b>Password Manager created by</b> Aiden Lai, <br>Damilola Araba, Ishita Chabra, Jarogniew Witkowski, <br>Jonathan Devaux, Laura Dumitrescu")


class create_account(QDialog):
    # switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Password Manager Create Account')
        self.resize(600, 200)

        layout = QtWidgets.QGridLayout()
        menubar = QMenuBar()  # menu bar
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        helpAct = QAction('Help')
        fileMenu = menubar.addMenu('&Application')
        helpMenu = menubar.addMenu('Help')  # add item to menu bar
        actionAbout = QtWidgets.QAction(self)  # subitem
        actionAbout.setObjectName("actionAbout")
        forgetPassword = QtWidgets.QAction(self)
        forgetPassword.setObjectName("forgetPassword")
        helpMenu.addAction(helpAct)
        helpMenu.addAction(forgetPassword)
        helpMenu.addAction(actionAbout)  # add submenu item to help
        actionAbout.setText("About")
        actionAbout.setShortcut('F1')
        actionAbout.triggered.connect(lambda: self.showInfo())  # set submenu name
        forgetPassword.setText("Forget Password")
        forgetPassword.triggered.connect(lambda: self.showRecoverAccount())
        fileMenu.addAction(exitAct)
        layout.addWidget(menubar, 0, 0, 1, 0)
        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 1, 0)
        layout.addWidget(self.lineEdit_username, 1, 1)
        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 2, 0)
        layout.addWidget(self.lineEdit_password, 2, 1)
        label_confirmpassword1 = QLabel('<font size="4"> Confirm password </font>')
        self.lineEdit_confirmPassword = QLineEdit()
        self.lineEdit_confirmPassword.setEchoMode(QLineEdit.Password)
        self.lineEdit_confirmPassword.setPlaceholderText('Please confirm your password')
        layout.addWidget(label_confirmpassword1, 3, 0)
        layout.addWidget(self.lineEdit_confirmPassword, 3, 1)
        label_securityQuestion = QLabel('<font size="4"> Please answer the security question: </font>')
        layout.addWidget(label_securityQuestion, 4, 0)
        list = functions.questions(1)
        self.combo3 = QComboBox()
        self.combo3.addItems(list)
        layout.addWidget(self.combo3)
        self.lineEdit_answer = QLineEdit()
        self.lineEdit_answer.setPlaceholderText('Answer')
        layout.addWidget(self.lineEdit_answer, 5, 1)

        self.button_create = QtWidgets.QPushButton('Create')
        self.button_create.clicked.connect(lambda: self.createAccount())
        button_show_login = QtWidgets.QPushButton('Login with existing account', default=False, autoDefault=False)
        button_show_login.clicked.connect(lambda: self.showLogin())
        # self.button.clicked.connect(lambda: on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        layout.addWidget(button_show_login)
        layout.addWidget(self.button_create)
        self.setLayout(layout)

    def createAccount(self):

        if (self.lineEdit_password.text() == self.lineEdit_confirmPassword.text()):
            PasswordManager_main.create_account_UI(str(self.lineEdit_username.text()),
                                                   str(self.lineEdit_password.text()),
                                                   str(self.combo3.currentText()), str(self.lineEdit_answer.text()))
            self.cams = PasswordManagerMenu(self.lineEdit_username.text(), self.lineEdit_password.text(), (int(
                PasswordManager_main.get_last_id(
                    os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv"))) + 1))
            self.cams.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Password Manager Notification", "Incorrect Username or Password!",
                                          QtWidgets.QMessageBox.Ok)

    def showRecoverAccount(self):
        self.cams = recover_account()
        self.cams.show()
        self.close()

    def showLogin(self):
        self.cams = Login()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def showInfo(self):
        QtWidgets.QMessageBox.about(self, "Password Manager About",
                                    "<b>Password Manager created by</b> Aiden Lai, <br>Damilola Araba, Ishita Chabra, Jarogniew Witkowski, <br>Jonathan Devaux, Laura Dumitrescu")


class recover_account(QDialog):
    # switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Password Manager Forget Password')
        self.resize(500, 120)

        layout = QtWidgets.QGridLayout()
        menubar = QMenuBar()  # menu bar
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        helpAct = QAction('Help')
        fileMenu = menubar.addMenu('&Application')
        helpMenu = menubar.addMenu('Help')  # add item to menu bar
        actionAbout = QtWidgets.QAction(self)  # subitem
        actionAbout.setObjectName("actionAbout")
        login = QtWidgets.QAction(self)
        login.setObjectName("login")
        helpMenu.addAction(helpAct)
        helpMenu.addAction(login)
        helpMenu.addAction(actionAbout)  # add submenu item to help
        actionAbout.setText("About")
        actionAbout.setShortcut('F1')
        actionAbout.triggered.connect(lambda: self.showInfo())  # set submenu name
        login.setText("Return to login")
        login.triggered.connect(lambda: self.showLogin())
        fileMenu.addAction(exitAct)
        layout.addWidget(menubar, 0, 0, 1, 0)
        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 1, 0)
        layout.addWidget(self.lineEdit_username, 1, 1)
        label_question_answer = QLabel('<font size="4"> Answer:</font>')
        self.lineEdit_question_answer = QLineEdit()
        self.lineEdit_question_answer.setEchoMode(QLineEdit.Password)
        self.lineEdit_question_answer.setPlaceholderText('Please enter your security question answer:')
        layout.addWidget(label_question_answer, 2, 0)
        layout.addWidget(self.lineEdit_question_answer, 2, 1)

        button_login = QtWidgets.QPushButton('Login')
        button_login.clicked.connect(lambda: self.login())
        # self.button.clicked.connect(lambda: on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        layout.addWidget(button_login)
        self.setLayout(layout)

    def login(self):
        pass

    def showLogin(self):
        self.cams = Login()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def showInfo(self):
        QtWidgets.QMessageBox.about(self, "Password Manager About",
                                    "<b>Password Manager created by</b> Aiden Lai, <br>Damilola Araba, Ishita Chabra, Jarogniew Witkowski, <br>Jonathan Devaux, Laura Dumitrescu")


class PasswordManagerMenu(QDialog):
    def __init__(self, username, password, ID):
        super().__init__()
        # QDialog.__init__()
        self.setWindowTitle("Password Manager Menu")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(1106, 500)  # window size - please keep it a larger size, it's easier to test
        # self.setGeometry(100,100,680,500)
        # self.setStyleSheet('background-color:grey')
        self.global_username = username
        vbox = QVBoxLayout()
        menubar = QMenuBar()  # menu bar
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        helpAct = QAction('Help')
        fileMenu = menubar.addMenu('&File')
        helpMenu = menubar.addMenu('Help')  # add item to menu bar
        actionAbout = QtWidgets.QAction(self)  # subitem
        actionAbout.setObjectName("actionAbout")
        actionAbout.setText("About")
        actionAbout.setShortcut('F1')
        actionAbout.triggered.connect(lambda: self.showInfo())
        actionSearch = QtWidgets.QAction(self)  # subitem
        actionSearch.setObjectName("actionSearchInfo")
        actionSearch.setText("Search Tab Information")
        actionSearch.setShortcut('F2')
        actionSearch.triggered.connect(lambda: self.showSearchInfo())
        helpMenu.addAction(helpAct)
        helpMenu.addAction(actionAbout)  # add submenu item to help
        helpMenu.addAction(actionSearch)
        actionAbout.setText("About")  # set submenu name
        fileMenu.addAction(exitAct)
        # self.StatusBar_welcome = self.statusBar()
        # self.StatusBar_welcome.showMessage("Welcome back ")
        welcome_label = QLabel()
        welcome_label.setText('<font size="5"> Welcome Back ' + self.global_username + '<font size="5">')
        tabWidget = QTabWidget()
        # buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonbox.accepted.connect(self.accept)
        # buttonbox.rejected.connect(self.reject)
        tabWidget.setFont(QtGui.QFont("Arial", 12))
        tabWidget.addTab(TabNewPassword(username, password, ID), "Create New Password")
        tabWidget.addTab(TabSearchPassword(username, password, ID), "Search")
        tabWidget.addTab(TabChangeAccountPassword(username, password, ID), "Change Passwords")
        tabWidget.addTab(TabChangePassword(username, password, ID), "Account Setting(Password)")
        tabWidget.addTab(TabSecurityQuestion(username, password, ID), "Account Setting(Security Question)")
        tabWidget.addTab(TabAccounts(username, password, ID), "Accounts")
        vbox.addWidget(menubar)
        vbox.addWidget(welcome_label)
        vbox.addWidget(tabWidget)
        # vbox.addWidget(buttonbox)
        self.setLayout(vbox)

    def showInfo(self):
        QtWidgets.QMessageBox.about(self, "Password Manager About",
                                    "<b>Password Manager created by</b> Aiden Lai, <br>Damilola Araba, Ishita Chabra, Jarogniew Witkowski, <br>Jonathan Devaux, Laura Dumitrescu")
    def showSearchInfo(self):
        QtWidgets.QMessageBox.about(self, "Password Manager About",
                                    'For all search option regular expression search are suport, except double quote "\n'
                                    'For Advance search, Please use this format: (<column name>:<value>)\n'
                                    'All value needs to be places inside Parenthesis (, each Parenthesis must contain '
                                    'the column name, for instance: (Category:Email) to search for any password with'
                                    ' "Email" in the category column. \nTo add multiple rules please use "AND" or "OR" between each rules.\n'
                                    'Example:((Category:Email)AND(Description:mclaren))OR(Username:norris)\n'
                                    'You can also use the first three character of the column name as the <column name>')


# Tab to show list of current accounts
class TabAccounts(QWidget):
    def __init__(self, username, password, ID):
        QWidget.__init__(self)
        # super().__init__()
        self.globlal_id = ID
        self.table_row = 0
        vbox = QVBoxLayout()  # layout of the window/widget/table/tab
        self.tableWidget = QTableWidget(1, 10)  # create the table with 1 row and 11 columns
        self.columnNames = ["ID", "Title", "Username", "Password", "Description", "Category", "Email",
                            "Created", "Last Updated", "Strength"]  # setting the column names
        self.tableWidget.setHorizontalHeaderLabels(
            self.columnNames)  # setting the headers of the table to match column names
        font_header = QtGui.QFont("Arial", 12)  # selecting font and size
        self.tableWidget.setFont(font_header)
        self.tableWidget.horizontalHeader().setFont(font_header)
        # PasswordManagerMenu.setCentralWidget(self.tableWidget)  # what is the main window of this program???!
        # self.setGeometry(50, 50, 1000, 800)
        font = QtGui.QFont("Arial", 11)  # selecting font and size
        self.tableWidget.setFont(font)  # setting the font to the table
        self.tableWidget.setAlternatingRowColors(True)  # sets alternate row colours
        self.tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)
        self.tableWidget.verticalHeader().setVisible(False)
        self.show()
        self.openFile()
        vbox.addWidget(self.tableWidget)  # add table widget to the layout
        self.setLayout(vbox)  # set layout
        self.tableWidget.setSortingEnabled(True)  # enable table sorting

        # read the csv file

    def openFile(self):
        row_count = 0
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"), "r",
                  encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # lines = csv_file.readlines()
            next(csv_reader)
            lines = list(csv_reader)
            csv_file.close()
        self.tableWidget.setRowCount(len(lines))  # set the number of rows to be = to the nr of lines read from file
        if len(lines) !=1:
        # loop that processes lines from the file
            for i in range(0, len(lines)):
                if int(lines[i][1]) == self.globlal_id:
                    for column_number, data in enumerate(lines[i]):
                        # print(str(column_number)+ ":"+(data))
                        if column_number < 1:
                            self.tableWidget.setItem(i, column_number, QTableWidgetItem(data))
                        elif column_number > 1:
                            self.tableWidget.setItem(i, (column_number - 1), QTableWidgetItem(data))

            self.tableWidget.resizeColumnsToContents()  # resizes the columns to fit the content read from file
        else:
            pass

class TabChangeAccountPassword(QWidget):
    def __init__(self, username, password, ID):
        QWidget.__init__(self)
        # super().__init__()
        self.session_ID = ID
        self.session_username = username
        self.session_password = password
        groupBox = QGroupBox("Account Search:")
        groupBox2 = QGroupBox("Change Account Password:")
        SearchLabel = QLabel("Search: ")
        self.SearchEdit = QLineEdit()
        list_search = ["All", "Password Name", "Description", "Username", "Password", "Category", "Advance Search"]
        self.combo_search = QComboBox()
        self.combo_search.addItems(list_search)
        category_label = QLabel("Filter by Category:")
        list_category = functions.categories()
        self.combo_category = QComboBox()
        # self.combo_category.setEnabled(False)
        self.combo_category.addItems(list_category)
        self.combo_search.currentIndexChanged.connect(lambda: self.hint())
        button_search = QtWidgets.QPushButton('Search')
        button_search.clicked.connect(lambda: self.search())
        NewPasswordLabel = QLabel("Please enter new password:")
        self.NewPasswordEdit = QLineEdit()
        self.NewPasswordEdit.setEchoMode(QLineEdit.Password)
        button_show_password1 = QtWidgets.QPushButton('Show/\nHide Password', default=False, autoDefault=False)
        button_show_password1.clicked.connect(lambda: self.show_password1())
        button_suggest_password = QtWidgets.QPushButton('Use Password\nSuggestion', default=False, autoDefault=False)
        button_suggest_password.clicked.connect(lambda: self.suggest_password1())
        NewPasswordConfirmLabel = QLabel("Please confirm password:")
        self.NewPasswordConfirmEdit = QLineEdit()
        self.NewPasswordConfirmEdit.setEchoMode(QLineEdit.Password)
        button_submit = QtWidgets.QPushButton('Submit')
        button_submit.setShortcut("Return")
        button_submit.clicked.connect(lambda: self.submit())
        vbox = QtWidgets.QGridLayout()
        vbox.addWidget(SearchLabel, 0, 0)
        vbox.addWidget(self.SearchEdit, 0, 1)
        vbox.addWidget(self.combo_search, 0, 2)
        vbox.addWidget(category_label, 1, 0)
        vbox.addWidget(self.combo_category, 1, 1)
        vbox.addWidget(button_search, 1, 2)

        vbox2 = QtWidgets.QGridLayout()
        vbox2.addWidget(NewPasswordLabel, 2, 0)
        vbox2.addWidget(self.NewPasswordEdit, 2, 1)
        vbox2.addWidget(NewPasswordConfirmLabel, 3, 0)
        vbox2.addWidget(self.NewPasswordConfirmEdit, 3, 1)
        vbox2.addWidget(button_show_password1, 2, 2, 1, 1)
        vbox2.addWidget(button_suggest_password, 3, 2, 1, 1)
        vbox2.addWidget(button_submit, 4,0,2,2)


        groupBox.setLayout(vbox)
        groupBox2.setLayout(vbox2)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox2)
        self.setLayout(mainLayout)



    def show_password1(self):
        if self.echo_mode == False:

            self.NewPasswordEdit.setEchoMode(QLineEdit.Normal)
            self.NewPasswordConfirmEdit.setEchoMode(QLineEdit.Normal)
            self.echo_mode = True
        elif self.echo_mode == True:

            self.NewPasswordEdit.setEchoMode(QLineEdit.Password)
            self.NewPasswordConfirmEdit.setEchoMode(QLineEdit.Password)
            self.echo_mode = False

    def suggest_password(self):
        get_int, ok = QtWidgets.QInputDialog.getInt(self, "Password Manager Input",
                                                    "Please chose suggest password length:")
        random_password = functions.RandomPassWordGen_UI(get_int)
        QtWidgets.QMessageBox.warning(self, "Password Manager Suggest Password",
                                      "Your suggest password: " + random_password,
                                      QtWidgets.QMessageBox.Ok)
        self.NewpasswordEdit.setText(random_password)
        self.NewPasswordConfirmEdit.setText(random_password)

    # def submit(self):





class TabChangePassword(QWidget):
    def __init__(self, username, password, ID):

        super().__init__()
        self.session_username = username
        self.session_password = password
        self.session_ID = ID
        self.echo_mode = False
        CurrentUsernameLabel = QLabel("Please enter your username: ")
        self.CurrentUsernameEdit = QLineEdit()
        CurrentPasswordLabel = QLabel("Please enter your current password: ")
        self.CurrentPasswordEdit = QLineEdit()
        self.CurrentPasswordEdit.setEchoMode(QLineEdit.Password)
        NewPasswordLabel = QLabel("Please enter new password:")
        self.NewPasswordEdit = QLineEdit()
        self.NewPasswordEdit.setEchoMode(QLineEdit.Password)
        self.button_show_password1 = QtWidgets.QPushButton('Show/\nHide Password', default=False, autoDefault=False)
        self.button_show_password1.clicked.connect(lambda: self.show_password())
        NewPasswordConfirmLabel = QLabel("Please confirm password:")
        self.NewPasswordConfirmEdit = QLineEdit()
        self.NewPasswordConfirmEdit.setEchoMode(QLineEdit.Password)
        self.button_enter = QtWidgets.QPushButton('Submit')
        self.button_enter.setShortcut("Return")
        self.button_enter.clicked.connect(lambda: self.enter())

        vbox = QVBoxLayout()
        vbox.addWidget(CurrentUsernameLabel)
        vbox.addWidget(self.CurrentUsernameEdit)
        vbox.addWidget(CurrentPasswordLabel)
        vbox.addWidget(self.CurrentPasswordEdit)
        vbox.addWidget(NewPasswordLabel)
        vbox.addWidget(self.NewPasswordEdit)

        vbox.addWidget(NewPasswordConfirmLabel)
        vbox.addWidget(self.NewPasswordConfirmEdit)
        vbox.addWidget(self.button_show_password1)
        vbox.addWidget(self.button_enter)
        self.setLayout(vbox)

    def enter(self):
        if self.CurrentUsernameEdit.text() == self.session_username and self.CurrentPasswordEdit.text() == self.session_password:
            if (self.NewPasswordEdit.text() == self.NewPasswordConfirmEdit.text()):
                print("debug")
                PasswordManager_main.change_password(self.session_ID, str(self.NewPasswordEdit.text()))
            # PasswordManager_main.change_password(ID, new_password)
            else:
                QtWidgets.QMessageBox.warning(self, "Password Manager Notification", "Passwords don't match!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, "Password Manager Notification", "Incorrect Username or Password!",
                                          QtWidgets.QMessageBox.Ok)

    def show_password(self):
        if self.echo_mode == False:
            self.CurrentPasswordEdit.setEchoMode(QLineEdit.Normal)
            self.NewPasswordEdit.setEchoMode(QLineEdit.Normal)
            self.NewPasswordConfirmEdit.setEchoMode(QLineEdit.Normal)
            self.echo_mode = True
        elif self.echo_mode == True:
            self.CurrentPasswordEdit.setEchoMode(QLineEdit.Password)
            self.NewPasswordEdit.setEchoMode(QLineEdit.Password)
            self.NewPasswordConfirmEdit.setEchoMode(QLineEdit.Password)
            self.echo_mode = False


class TabSecurityQuestion(QWidget):
    def __init__(self, username, password, ID):
        super().__init__()
        groupBox = QGroupBox("Security Question Changer")

        headerLabel = QLabel("Please fill in your current security question and answer:")
        self.list1 = functions.questions(1)
        combo = QComboBox()
        combo.addItems(self.list1)
        currentLabel = QLabel("Current answer:")
        self.currentEdit = QLineEdit()
        newAskLabel = QLabel("Please choose a new security question and answer:")
        combo2 = QComboBox()
        combo2.addItems(self.list1)
        newLabel = QLabel("Answer:")
        self.newEdit = QLineEdit()
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        vbox = QVBoxLayout()
        vbox.addWidget(headerLabel)
        vbox.addWidget(combo)
        vbox.addWidget(currentLabel)
        vbox.addWidget(self.currentEdit)
        vbox.addWidget(newAskLabel)
        vbox.addWidget(combo2)
        vbox.addWidget(newLabel)
        vbox.addWidget(self.newEdit)
        groupBox.setLayout(vbox)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        vbox.addWidget(self.buttonbox)
        self.setLayout(mainLayout)


class TabNewPassword(QWidget):
    def __init__(self, username, password, ID):
        super().__init__()
        # QDialog.__init__()
        self.echo_mode = False
        self.session_username = username
        self.session_password = password
        self.session_ID = ID
        nameLabel = QLabel("Name: ")
        self.nameEdit = QLineEdit()
        self.nameEdit.setPlaceholderText('Please create a "Unique" name for your password')
        usernameLabel = QLabel("Username:")
        self.usernameEdit = QLineEdit()
        self.usernameEdit.setPlaceholderText('Please create a user name')
        passwordLabel = QLabel("Password:")
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setPlaceholderText('Please create password')
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.textChanged.connect(lambda: self.strength_checker(self.passwordEdit.text()))
        self.passwordEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passwordEdit.setFont(QFont('Arial', 12))
        self.passwordEdit.setFixedHeight(25)
        password_check_Label = QLabel("Confirm Password:")
        self.password_check_Edit = QLineEdit()
        self.password_check_Edit.setPlaceholderText('Please enter your password again')
        self.password_check_Edit.setEchoMode(QLineEdit.Password)
        self.password_check_Edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_check_Edit.textChanged.connect(lambda: self.strength_checker_check(self.password_check_Edit.text()))
        self.password_check_Edit.setFont(QFont('Arial', 12))
        self.password_check_Edit.setFixedHeight(25)
        w = QWidget()
        w.resize(200, 200)
        descriptionLabel = QLabel("Description:")
        self.descriptionEdit = QPlainTextEdit(w)
        self.descriptionEdit.setPlaceholderText("Brief description for your password")
        RegisterEnailLabel = QLabel("Please enter the registered email address:")
        self.RegisterEnailEdit = QLineEdit()
        self.RegisterEnailEdit.setPlaceholderText('example@example.com')
        CategoryLabel = QLabel("Please chose a category")
        list = functions.categories()
        self.combo = QComboBox()
        self.combo.addItems(list)
        self.button_submit = QtWidgets.QPushButton('Create')
        self.button_submit.setShortcut("Return")
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_suggest_password = QtWidgets.QPushButton('Use Password\nSuggestion', default=False, autoDefault=False)
        # button_suggest_password.clicked.connect(lambda: self.suggest_password())
        self.button_suggest_password.clicked.connect(lambda: self.suggest_password())
        # button_create_account.clicked.connect(lambda: self.showCreateAccount())
        # self.combo_text = self.combo.currentText()
        self.button_show_password = QtWidgets.QPushButton('Show/\nHide Password', default=False, autoDefault=False)
        self.button_show_password.clicked.connect(lambda: self.show_password())
        vbox = QtWidgets.QGridLayout()
        vbox.addWidget(nameLabel, 0, 0)
        vbox.addWidget(self.nameEdit, 0, 1)
        vbox.addWidget(usernameLabel, 1, 0)
        vbox.addWidget(self.usernameEdit, 1, 1)
        vbox.addWidget(passwordLabel, 2, 0)
        vbox.addWidget(self.passwordEdit, 2, 1)
        vbox.addWidget(self.button_suggest_password, 2, 2)
        vbox.addWidget(password_check_Label, 3, 0)
        vbox.addWidget(self.password_check_Edit, 3, 1)
        vbox.addWidget(self.button_show_password, 3, 2)
        vbox.addWidget(descriptionLabel, 4, 0)
        vbox.addWidget(self.descriptionEdit, 4, 1)
        vbox.addWidget(RegisterEnailLabel, 5, 0)
        vbox.addWidget(self.RegisterEnailEdit, 5, 1)
        vbox.addWidget(CategoryLabel, 6, 0)
        vbox.addWidget(self.combo, 6, 1)
        vbox.addWidget(self.button_submit, 7, 2)
        self.setLayout(vbox)

    def submit(self):
        try:
            if self.nameEdit.text():
                result = PasswordManager_main.password_name_checker(self.nameEdit.text(), self.session_ID)
                if result == False:
                    if str(self.passwordEdit.text()) == str(self.password_check_Edit.text()):
                        strength = functions.PassStrengthCheck(str(self.passwordEdit.text()))
                        PasswordManager_main.create_password_ui(int(self.session_ID), str(self.nameEdit.text()),
                                                                str(self.usernameEdit.text()),
                                                                str(self.passwordEdit.text()),
                                                                str(self.descriptionEdit.toPlainText()),
                                                                str(self.combo.currentText()),
                                                                str(self.RegisterEnailEdit.text()),strength)
                        self.nameEdit.setText("")
                        self.usernameEdit.setText("")
                        self.passwordEdit.setText("")
                        self.password_check_Edit.setText("")
                        self.descriptionEdit.setPlainText("")
                        self.RegisterEnailEdit.setText("")
                        QtWidgets.QMessageBox.about(self, "Password Manager Notification", "Password added to database")

                    else:
                        QtWidgets.QMessageBox.warning(self, "Password Manager Notification", "Password not match!",
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.warning(self, "Password Manager Notification",
                                                  "Password Name " + str(self.nameEdit.text()) + " exist!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.warning(self, "Password Manager Notification",
                                              "Password Name can not be empty!",
                                              QtWidgets.QMessageBox.Ok)

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Password Manager Error",
                                          "An error occure! Error Information: " + str(e),
                                          QtWidgets.QMessageBox.Ok)

    def suggest_password(self):
        get_int, ok = QtWidgets.QInputDialog.getInt(self, "Password Manager Input",
                                                    "Please chose suggest password length:", 8,8)
        if ok and get_int != 0:
            random_password = functions.Iteration2PassGen(True,True,True,True,get_int)
            QtWidgets.QMessageBox.warning(self, "Password Manager Suggest Password",
                                          "Your suggest password: " + random_password,
                                          QtWidgets.QMessageBox.Ok)
            self.passwordEdit.setText(random_password)
            self.password_check_Edit.setText(random_password)

    def show_password(self):
        if self.echo_mode == False:
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
            self.password_check_Edit.setEchoMode(QLineEdit.Normal)
            self.echo_mode = True
        elif self.echo_mode == True:
            self.passwordEdit.setEchoMode(QLineEdit.Password)
            self.password_check_Edit.setEchoMode(QLineEdit.Password)
            self.echo_mode = False

    def strength_checker(self,password):
        if len(password)  == 0:
            self.passwordEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        else:
            check = functions.PassStrengthCheck(password)
            if check == "Weak":
                self.passwordEdit.setStyleSheet("background-color: rgb(255, 127, 127);")
            elif check == "Medium":
                self.passwordEdit.setStyleSheet("background-color: rgb(255, 255, 127);")
            elif check == "Strong":
                self.passwordEdit.setStyleSheet("background-color: rgb(200, 255, 200);")
            elif check == "Very Strong":
                self.passwordEdit.setStyleSheet("background-color: rgb(127, 255, 127);")
            else:
                self.passwordEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

    def strength_checker_check(self,password):
        if len(password) == 0:
            self.passwordEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        else:
            check = functions.PassStrengthCheck(password)
            if check == "Weak":
                self.password_check_Edit.setStyleSheet("background-color: rgb(255, 127, 127);")
            elif check == "Medium":
                self.password_check_Edit.setStyleSheet("background-color: rgb(255, 255, 127);")
            elif check == "Strong":
                self.password_check_Edit.setStyleSheet("background-color: rgb(200, 255, 200);")
            elif check == "Very Strong":
                self.password_check_Edit.setStyleSheet("background-color: rgb(127, 255, 127);")
            else:
                self.password_check_Edit.setStyleSheet("background-color: rgb(255, 255, 255);")

    # def call_pop_up(self):
    #     self.dialog = popup_dialog()
    #     self.dialog.exec_()
    #     value, value2, value3, value4 = popup_dialog.submit_handel()
    #     print(value)



class TabSearchPassword(QWidget):
    def __init__(self, username, password, ID):
        super().__init__()
        self.session_ID = ID
        self.session_username = username
        self.session_password = password
        self.enable_mode = False
        groupBox = QGroupBox("Password search:")
        groupBox2 = QGroupBox("Result:")
        SearchLabel = QLabel("Search: ")
        self.SearchEdit = QLineEdit()
        self.list_search = ["All", "Password Name", "Description", "Username", "Password","Category","Advance Search"]
        self.combo_search = QComboBox()
        self.combo_search.addItems(self.list_search)
        category_label = QLabel("Filter by Category:")
        list_category = functions.categories()
        self.combo_category = QComboBox()
        self.combo_category.setEnabled(False)
        self.combo_category.addItems(list_category)
        self.combo_search.currentIndexChanged.connect(lambda: self.hint())
        self.button_switch = QtWidgets.QPushButton('Switch to Category')
        self.button_switch.clicked.connect(lambda: self.enable_category())
        self.button_search = QtWidgets.QPushButton('Search')
        self.button_search.clicked.connect(lambda: self.search())
        vbox = QtWidgets.QGridLayout()
        vbox.addWidget(SearchLabel, 0, 0)
        vbox.addWidget(self.SearchEdit, 0, 1)
        vbox.addWidget(self.combo_search, 0, 2)
        vbox.addWidget(category_label, 1, 0)
        vbox.addWidget(self.combo_category, 1, 1)
        vbox.addWidget(self.button_switch, 1, 2)
        vbox.addWidget(self.button_search, 2, 2)
        vbox2 = QVBoxLayout()
        ########## Table Setting
        self.tableWidget = QTableWidget(1, 10)  # create the table with 1 row and 11 columns
        self.columnNames = ["ID", "Title", "Username", "Password", "Description", "Category", "Email",
                            "Created", "Last Updated", "Strength"]  # setting the column names
        self.tableWidget.setHorizontalHeaderLabels(
            self.columnNames)  # setting the headers of the table to match column names
        # PasswordManagerMenu.setCentralWidget(self.tableWidget)  # what is the main window of this program???!
        # self.setGeometry(50, 50, 1000, 800)
        font = QtGui.QFont("Arial", 12)  # selecting font and size
        self.tableWidget.setFont(font)  # setting the font to the table
        self.tableWidget.setAlternatingRowColors(True)  # sets alternate row colours
        self.tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setSortingEnabled(True)
        # self._delegate = HighlightDelegate(self.tableWidget)
        # self.tableWidget.setItemDelegate(self._delegate)

        ########## Table Setting
        vbox2.addWidget(self.tableWidget)
        groupBox.setLayout(vbox)
        groupBox2.setLayout(vbox2)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox2)
        self.setLayout(mainLayout)

    def enable_category(self):
        if self.enable_mode == False:
            self.SearchEdit.setEnabled(False)
            self.combo_category.setEnabled(True)
            self.button_switch.setText("Switch to Search")
            self.enable_mode = True
        else:
            self.SearchEdit.setEnabled(True)
            self.combo_category.setEnabled(False)
            self.button_switch.setText("Switch to Category")
            self.enable_mode = False

    def set_table(self, category):
        data = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"))
        # example = "(Description:google password)"
        user_query = self.SearchEdit.text()
        if category == 1:
            final = '( UserID == "' + str(self.session_ID) + '")&(' + 'Category.str.contains("('+user_query+\
                    ')",regex=True,case=False)|Description.str.contains("('+user_query+\
                    ')",regex=True,case=False)|Username.str.contains("('+user_query+\
                    ')",regex=True,case=False)|Name.str.contains("('+user_query+ ')",regex=True,case=False))'
        elif category == 2:
            final = '( UserID == "' + str(self.session_ID) + '")&(' + 'Name.str.contains("(' + user_query + \
                    ')",regex=True,case=False))'
        elif category == 3:
            final = '( UserID == "' + str(self.session_ID) + '")&(' + 'Description.str.contains("(' + user_query + \
                    ')",regex=True,case=False))'
        elif category == 4:
            final = '( UserID == "' + str(self.session_ID) + '")&(' + 'Username.str.contains("(' + user_query + \
                    ')",regex=True,case=False))'
        elif category == 5:
            final = '( UserID == "' + str(self.session_ID) + '")&(' + 'Password.str.contains("(' + user_query + \
                    ')",regex=True,case=False))'
        elif category == 6:
            final = '( UserID == "' + str(self.session_ID) + '")&(' + 'Category.str.contains("(' + user_query + \
                    ')",regex=True,case=False))'
        elif category == 7:
            final = '( UserID == "' + str(self.session_ID) + '")&(' + 'Category.str.contains("(' + \
                    self.combo_category.currentText() + ')",regex=True,case=False))'
        result = data.query(final, engine='python')
        result_list = result.values.tolist()
        if len(result_list) != 0:
            self.tableWidget.setRowCount(len(result_list))
            # print(result)
            try:
                for i in range(0, len(result_list)):
                    for column_number, data in enumerate(result_list[i]):
                        if column_number < 1:
                            self.tableWidget.setItem(i, column_number, QTableWidgetItem(str(data)))
                        elif column_number > 1:
                            self.tableWidget.setItem(i, (column_number - 1), QTableWidgetItem(str(data)))
                self.tableWidget.resizeColumnsToContents()
            except Exception as e:
                print(e)
        else:
            if not self.enable_mode:
                QtWidgets.QMessageBox.about(self, "Password Manager Notification", "No result for : "+user_query )
            else:
                QtWidgets.QMessageBox.about(self, "Password Manager Notification", "No result for : "+
                                            self.combo_category.currentText())


    def set_table_advance(self):
        data = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"))
        # example = "(Description:google password)"
        replace = ["Name:","Username:","Password:","Description:","Category:","Email:",
                      "CreateCreated_Date:","Updated_Date:","Strength:"]
        need_replace=[["name:","password name:","Passwordname:"],["usr:","username:","USR:","user:","User:"],
                      ["pw:","password:","PW:","pass:","pas:"],["description","des:","DES:"],["cat:","category:","CAT:"],
                      ["email:","mail:","ema:","EMA:"],["Created:","created:","create date:","Create Date","CreateDate:"],
                      ["Updated:","updated:","updated date:","Updated Date","UpdatedDate:"],["strength","str:","STR:"]]
        user_query_original = self.SearchEdit.text()
        user_query = self.SearchEdit.text()
        for i in range(0,len(replace)):
            for j , value in enumerate(need_replace[i]):
                user_query = re.sub(value,replace[i],user_query)

        user_query_AND = re.sub('\)AND\(', ')&(', user_query)
        user_query_OR = re.sub('\)OR\(', ')|(', user_query_AND)
        search = re.sub(r'\((ID|Name|Username|Password|Description|Category|Email|CreateCreated_Date|Updated_Date|Strength):(.*?)\)',
                        "\\1.str.contains(\"(\\2)\",regex=True,case=False)", user_query_OR)
        final = '( UserID == "'+str(self.session_ID)+'")&('+search+')'
        print(final)
        try:
            result = data.query(final, engine='python')
            result_list = result.values.tolist()
            if result_list != 0:
                self.tableWidget.setRowCount(len(result_list))
                for i in range(0, len(result_list)):
                    for column_number, data in enumerate(result_list[i]):
                        # print(str(column_number)+ ":"+(data))
                        if column_number < 1:
                            self.tableWidget.setItem(i, column_number, QTableWidgetItem(str(data)))
                        elif column_number > 1:
                            self.tableWidget.setItem(i, (column_number - 1), QTableWidgetItem(str(data)))
                self.tableWidget.resizeColumnsToContents()
            else:
                QtWidgets.QMessageBox.about(self, "Password Manager Notification", "No result for : "+user_query_original )
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "Password Manager Notification", "Invalid search string : "+user_query_original )
        # Final = re.sub(r'\b(.*?)\s+\b(.*?)', r'\1|\2', search)


    def search(self):
        self.tableWidget.clearContents()
        if self.enable_mode == False:
            if not '"' in self.SearchEdit.text():
                if self.enable_mode == False:
                    if self.combo_search.currentText() == "All":
                        self.set_table(1)
                    elif self.combo_search.currentText() == "Password Name":
                        self.set_table(2)
                    elif self.combo_search.currentText() == "Description":
                        self.set_table(3)
                    elif self.combo_search.currentText() == "Username":
                        self.set_table(4)
                    elif self.combo_search.currentText() == "Password":
                        self.set_table(5)
                    elif self.combo_search.currentText() == "Category":
                        self.set_table(6)
                    elif self.combo_search.currentText() == "Advance Search":
                        self.set_table_advance()
            else:
                QtWidgets.QMessageBox.about(self, "Password Manager Notification",
                                            "Invalid search string : " + self.SearchEdit.text() +'<br> " are not supported for advance search')
        else:
            self.set_table(7)


    def hint(self):
        if self.combo_search.currentText() == "Advance Search":
            self.SearchEdit.setPlaceholderText("Example:((Category:Email)AND(Description:mclaren))OR(Username:norris)")
        else:
            self.SearchEdit.setPlaceholderText("")

# class popup_dialog(QDialog):
#     def __init__(self):
#         super().__init__()
#         CurrentLabel = QLabel("Suggest password parameter: ")
#         self.check_upper = QCheckBox("Uppercase Character")
#         self.check_lower = QCheckBox("Lowercase Character")
#         self.check_special = QCheckBox("Special Character")
#         self.check_number = QCheckBox("Numbers")
#         # self.ui.buttonBox.accepted.connect(self.accept)
#         button_submit = QtWidgets.QPushButton('Submit', default=False, autoDefault=False)
#         button_submit.clicked.connect(lambda: self.submit_handel())
#         buttonbox = QDialogButtonBox(QDialogButtonBox.Ok)
#         button_enter = QtWidgets.QPushButton('Submit')
#         button_enter.setShortcut("Return")
#         vbox = QtWidgets.QGridLayout()
#         vbox.addWidget(CurrentLabel,0,0)
#         vbox.addWidget(self.check_lower,1,0)
#         vbox.addWidget(self.check_upper,1,1)
#         vbox.addWidget(self.check_special,2,0)
#         vbox.addWidget(self.check_number,2,1)
#         vbox.addWidget(button_submit,3,1)
#         # vbox.addWidget(button_enter)
#         self.setLayout(vbox)

    # def submit_handel(self):
    #     # if self.exec() == QDialog.accept():
    #     if self.check_number.isChecked():
    #         TabSearchPassword. = True
    #     if self.check_upper.isChecked():
    #         upper = True
    #     if self.check_lower.isChecked():
    #         lower = True
    #     if self.check_special.isChecked():
    #         special = True
    #     return upper, lower, spcial, number
    #         # print(self.check_number)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # controller = Login()
    # controller = create_account()
    controller = PasswordManagerMenu("abc", "abc", 1)
    controller.show()
    app.exec()
    # if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/UserAccount.csv")):
    #     # PasswordManager_main.
    #     app = QtWidgets.QApplication(sys.argv)
    #     controller = Login()
    #     # controller = create_account()
    #     # controller = PasswordManagerMenu("abc", "abc", 1)
    #     controller.show()
    #     app.exec()
    # else:
    #
    #     try:
    #         os.mkdir( os.path.join(os.path.dirname(os.path.abspath(__file__)),"data/"))
    #     except FileExistsError:
    #         pass
    #     PasswordManager_main.create_account_db()
    #     PasswordManager_main.create_password_db()
    #     app = QtWidgets.QApplication(sys.argv)
    #     controller = create_account()
    #     controller.show()
    #     app.exec()
