import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
import csv
from trunk.PasswordManager_main import PasswordManager_main

class Login(QtWidgets.QWidget):
    # switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Password Manager')
        self.resize(500, 120)

        layout = QtWidgets.QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)
        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        self.button_login = QtWidgets.QPushButton('Login')
        self.button_login.clicked.connect(lambda: self.login())
        self.button_create_account = QtWidgets.QPushButton('Create Account', default=False, autoDefault=False)
        # self.button.clicked.connect(lambda: on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        layout.addWidget(self.button_create_account)
        layout.addWidget(self.button_login)

        self.setLayout(layout)
    @pyqtSlot()
    def login(self):
        result, username, password, ID = PasswordManager_main.login_check(str(self.lineEdit_username.text()), str(self.lineEdit_password.text()))
        if result == True:
            self.cams = PasswordManagerMenu()
            self.cams.show()
            self.close()
        elif result == False :
            QtWidgets.QMessageBox.warning(self,"Password Manager Notification","Incorrect Username or Password!",
                                          QtWidgets.QMessageBox.Ok)

class create_account(QDialog):
    pass



class PasswordManagerMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager Menu")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(1050, 800)  # window size
        self.setGeometry(100,100,680,500)
        # self.setStyleSheet('background-color:grey')
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
        helpMenu.addAction(helpAct)
        helpMenu.addAction(actionAbout)   # add submenu item to help
        actionAbout.setText("About")  # set submenu name
        fileMenu.addAction(exitAct)
        tabWidget = QTabWidget()
        # buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonbox.accepted.connect(self.accept)
        # buttonbox.rejected.connect(self.reject)
        tabWidget.setFont(QtGui.QFont("Arial", 12))
        tabWidget.addTab(TabNewPassword(), "Create New Password")
        tabWidget.addTab(TabSearchPassword(), "Search")
        tabWidget.addTab(TabChangePassword(), "Account Setting(Password)")
        tabWidget.addTab(TabSecurityQuestion(), "Account Setting(Security Question)")
        tabWidget.addTab(TabAccounts(), "Accounts")
        vbox.addWidget(menubar)
        vbox.addWidget(tabWidget)
        # vbox.addWidget(buttonbox)
        self.setLayout(vbox)


# Tab to show list of current accounts
class TabAccounts(QWidget):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)  # container for the table
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)  # add table to centralwidget
        self.tableWidget.setGeometry(QtCore.QRect(25, 90, 953, 601))  # set size of table
        font = QtGui.QFont()  # select font and save it to "font"
        font.setPointSize(16)  # set font size
        font.setBold(False)  # set text to not be bold
        font.setWeight(50)
        self.tableWidget.setFont(font)  # assign font to table
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAlternatingRowColors(True)  # sets alternate row colours
        self.tableWidget.setIconSize(QtCore.QSize(20, 20))  # sets the size of the icons (had them added previously but removed for now)
        self.tableWidget.setShowGrid(True)  # shows grid lines of table
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)  # the style of grid
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)  # number of columns/horizontal headers
        self.tableWidget.setRowCount(10)  # number of rows - change it later to make it increase automatically with each new addition

        # Rows
        item = QtWidgets.QTableWidgetItem()
        font.setBold(True)  # makes the selected column and row bold
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)

        # Columns
        item = QtWidgets.QTableWidgetItem()
        font.setBold(True)
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font.setBold(True)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        font.setBold(True)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        font.setBold(True)
        self.tableWidget.setHorizontalHeaderItem(3, item)

        # Data
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(233)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

# Sets the table headers text and enables sorting
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("", "Account"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("", "Created"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("", "Last updated"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("", "Strength"))
        # __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(False)
        # self.tableWidget.setSortingEnabled(__sortingEnabled)

        """item = self.tableWidget.item(1, 0)
        item.setText(_translate("", "Youtube.com"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("", "11/10/2015"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("", "10/03/2017"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("", "Moderate"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("", "Google.com"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("", "09/03/2010"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("", "09/03/2010"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("", "Strong"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("", "Reddit.com"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("", "17/01/2018"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("", "23/04/2020"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("", "Moderate"))"""


# Testing reading from csv file - this reads the UserAccount file and displays the information in console
        with open("Dummy_data/UserAccount.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} Username: {row[1]}, Password: {row[2]}, Security Question: {row[3]}, Answer: {row[4]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')

# Reading from csv file AccountPassword and displaying information in console for now
        with open("Dummy_data/1_AccountPassword.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} UserID: {row[1]}, Title: {row[2]}, Username: {row[3]}, Password: {row[4]}, Description: {row[5]}, Category: {row[6]}, Email: {row[7]}.')
                    item = self.tableWidget.item(1, 0)
                    item.setText(row[2])
                    line_count += 1
            print(f'Processed {line_count} lines.')


class TabChangePassword(QWidget):
    def __init__(self):
        super().__init__()
        CurrentPasswordLabel = QLabel("Please enter your current password: ")
        CurrentPasswordEdit = QLineEdit()
        NewPasswordLabel = QLabel("Please enter new password:")
        NewPasswordEdit = QLineEdit()
        NewPasswordConfirmLabel = QLabel("Please confirm password:")
        NewPasswordConfirmEdit = QLineEdit()
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        vbox = QVBoxLayout()
        vbox.addWidget(CurrentPasswordLabel)
        vbox.addWidget(CurrentPasswordEdit)
        vbox.addWidget(NewPasswordLabel)
        vbox.addWidget(NewPasswordEdit)
        vbox.addWidget(NewPasswordConfirmLabel)
        vbox.addWidget(NewPasswordConfirmEdit)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)



class TabSecurityQuestion(QWidget):
    def __init__(self):
        super().__init__()
        groupBox = QGroupBox("Security Question Changer")
        headerLabel = QLabel("Please fill in your current Security question and answer:")
        list = ["Your favourite place?", "What is your favourite colour?", "Your first school?", "Your pet name?"]
        combo = QComboBox()
        combo.addItems(list)
        currentLabel = QLabel("Current answer:")
        currentEdit = QLineEdit()
        newAskLabel = QLabel("Please chose a new security question and answer:")
        combo2 = QComboBox()
        combo2.addItems(list)
        newLabel = QLabel("Answer:")
        newEdit = QLineEdit()
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        vbox = QVBoxLayout()
        vbox.addWidget(headerLabel)
        vbox.addWidget(combo)
        vbox.addWidget(currentLabel)
        vbox.addWidget(currentEdit)
        vbox.addWidget(newAskLabel)
        vbox.addWidget(combo2)
        vbox.addWidget(newLabel)
        vbox.addWidget(newEdit)
        groupBox.setLayout(vbox)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        vbox.addWidget(buttonbox)
        self.setLayout(mainLayout)

class TabNewPassword(QWidget):
    def __init__(self):
        super().__init__()
        nameLabel = QLabel("Name: ")
        nameEdit = QLineEdit()
        usernameLabel = QLabel("Username:")
        usernameEdit = QLineEdit()
        passwordLabel = QLabel("Password:")
        passwordEdit = QLineEdit()
        w = QWidget()
        w.resize(200, 200)
        descriptionLabel = QLabel("Description:")
        descriptionEdit = QPlainTextEdit(w)
        RegisterEnailLabel = QLabel("Please enter the registered email address:")
        RegisterEnailEdit = QLineEdit()
        CategoryLabel = QLabel("Please chose a category")
        list = ["Email", "Work", "Study", "Entertainment", "Programming", "Others"]
        combo = QComboBox()
        combo.addItems(list)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        vbox = QVBoxLayout()
        vbox.addWidget(nameLabel)
        vbox.addWidget(nameEdit)
        vbox.addWidget(usernameLabel)
        vbox.addWidget(usernameEdit)
        vbox.addWidget(passwordLabel)
        vbox.addWidget(passwordEdit)
        vbox.addWidget(descriptionLabel)
        vbox.addWidget(descriptionEdit)
        vbox.addWidget(RegisterEnailLabel)
        vbox.addWidget(RegisterEnailEdit)
        vbox.addWidget(CategoryLabel)
        vbox.addWidget(combo)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)

class TabSearchPassword(QWidget):
    def __init__(self):
        super().__init__()
        SearchLabel = QLabel("Search: ")
        SearchEdit = QLineEdit()
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        vbox = QVBoxLayout()
        vbox.addWidget(SearchLabel)
        vbox.addWidget(SearchEdit)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Login()
    controller.show()
    app.exec()