from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QComboBox, QCheckBox, QGroupBox, QVBoxLayout, QWidget, \
    QLabel, QLineEdit, QDialogButtonBox, QAction, qApp, QMenuBar, QPlainTextEdit, QMessageBox, QTableWidget, \
    QTableWidgetItem, QStatusBar, QMainWindow
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from trunk.PasswordManager_main import PasswordManager_main
from trunk.PasswordManager_function import functions

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
        actionAbout.triggered.connect(lambda: self.showInfo())# set submenu name
        forgetPassword.setText("Forget Password")
        forgetPassword.triggered.connect(lambda: self.showRecoverAccount())
        fileMenu.addAction(exitAct)
        layout.addWidget(menubar, 0, 0,1,0)
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

        button_login = QtWidgets.QPushButton('Login')
        button_login.setShortcut("Return")
        button_login.clicked.connect(lambda: self.login())
        button_create_account = QtWidgets.QPushButton('Create Account', default=False, autoDefault=False)
        button_create_account.clicked.connect(lambda: self.showCreateAccount())
        # self.button.clicked.connect(lambda: on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        layout.addWidget(button_create_account)
        layout.addWidget(button_login)
        self.setLayout(layout)

    @pyqtSlot()
    def login(self):
        result, username, password, ID = PasswordManager_main.login_check(str(self.lineEdit_username.text()), str(self.lineEdit_password.text()))
        if result == True:
            self.cams = PasswordManagerMenu(username, password, ID)
            self.cams.show()
            self.close()
        elif result == False :
            QtWidgets.QMessageBox.warning(self,"Password Manager Notification","Incorrect Username or Password!",
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
        actionAbout.triggered.connect(lambda: self.showInfo())# set submenu name
        forgetPassword.setText("Forget Password")
        forgetPassword.triggered.connect(lambda: self.showRecoverAccount())
        fileMenu.addAction(exitAct)
        layout.addWidget(menubar, 0, 0,1,0)
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

        button_create = QtWidgets.QPushButton('Create')
        button_create.clicked.connect(lambda: self.showLogin())
        button_show_login = QtWidgets.QPushButton('Login with existing account', default=False, autoDefault=False)
        button_show_login.clicked.connect(lambda: self.showLogin())
        # self.button.clicked.connect(lambda: on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        layout.addWidget(button_show_login)
        layout.addWidget(button_create)
        self.setLayout(layout)

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
        actionAbout.triggered.connect(lambda: self.showInfo())# set submenu name
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
        helpMenu.addAction(helpAct)
        helpMenu.addAction(actionAbout)   # add submenu item to help
        actionAbout.setText("About")  # set submenu name
        fileMenu.addAction(exitAct)
        # self.StatusBar_welcome = self.statusBar()
        # self.StatusBar_welcome.showMessage("Welcome back ")
        welcome_label = QLabel()
        welcome_label.setText('<font size="5"> Welcome Back '+ self.global_username +'<font size="5">')
        tabWidget = QTabWidget()
        # buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonbox.accepted.connect(self.accept)
        # buttonbox.rejected.connect(self.reject)
        tabWidget.setFont(QtGui.QFont("Arial", 12))
        tabWidget.addTab(TabNewPassword(username, password, ID), "Create New Password")
        tabWidget.addTab(TabSearchPassword(), "Search")
        tabWidget.addTab(TabChangePassword(), "Account Setting(Password)")
        tabWidget.addTab(TabSecurityQuestion(), "Account Setting(Security Question)")
        tabWidget.addTab(TabAccounts(username, password, ID), "Accounts")
        vbox.addWidget(menubar)
        vbox.addWidget(welcome_label)
        vbox.addWidget(tabWidget)
        # vbox.addWidget(buttonbox)
        self.setLayout(vbox)


    @pyqtSlot()
    def showInfo(self):
        QtWidgets.QMessageBox.about(self, "Password Manager About",
                                    "<b>Password Manager created by</b> Aiden Lai, <br>Damilola Araba, Ishita Chabra, Jarogniew Witkowski, <br>Jonathan Devaux, Laura Dumitrescu")


# Tab to show list of current accounts
class TabAccounts(QWidget):
    def __init__(self,username, password, ID):
        QWidget.__init__(self)
        # super().__init__()
        self.globlal_id = ID
        self.table_row = 0
        vbox = QVBoxLayout()  # layout of the window/widget/table/tab
        self.tableWidget = QTableWidget(1, 10)  # create the table with 1 row and 11 columns
        self.columnNames = ["ID", "Title", "Username", "Password", "Description", "Category", "Email",
                            "Created", "Last Updated", "Strength"]  # setting the column names
        self.tableWidget.setHorizontalHeaderLabels(self.columnNames)  # setting the headers of the table to match column names
        # PasswordManagerMenu.setCentralWidget(self.tableWidget)  # what is the main window of this program???!
        # self.setGeometry(50, 50, 1000, 800)
        font = QtGui.QFont("Arial", 12)  # selecting font and size
        self.tableWidget.setFont(font)  # setting the font to the table
        self.tableWidget.setAlternatingRowColors(True)  # sets alternate row colours
        self.tableWidget.sortItems(0,QtCore.Qt.AscendingOrder)
        self.tableWidget.verticalHeader().setVisible(False)
        self.show()
        self.openFile()
        vbox.addWidget(self.tableWidget)  # add table widget to the layout
        self.setLayout(vbox)  # set layout
        self.tableWidget.setSortingEnabled(True)  # enable table sorting

        # read the csv file
    def openFile(self):
        row_count = 0
        with open("data/1_AccountPassword.csv","r", encoding='utf8') as csv_file:
            # csv_reader = csv.reader(csv_file, delimiter=',')
            lines = csv_file.readlines()
            for i in range(0, len(lines)):
                value = lines[i].strip().split(",")
                if int(value[1]) == self.globlal_id:
                    row_count = row_count + 1
            csv_file.close()
        self.tableWidget.setRowCount(row_count)  # set the number of rows to be = to the nr of lines read from file

        # loop that processes lines from the file
        for i in range(0, len(lines)):
            tokens = lines[i].strip().split(",")  # split the lines by "," and store list of strings as tokens
            if int(tokens[1]) == self.globlal_id:
                colID = QTableWidgetItem(tokens[0])
                # userID = QTableWidgetItem(tokens[1])
                title = QTableWidgetItem(tokens[2])
                username = QTableWidgetItem(tokens[3])
                password = QTableWidgetItem(tokens[4])
                desc = QTableWidgetItem(tokens[5])
                cat = QTableWidgetItem(tokens[6])
                email = QTableWidgetItem(tokens[7])
                created = QTableWidgetItem(tokens[8])
                updated = QTableWidgetItem(tokens[9])
                strength = QTableWidgetItem(tokens[10])

                # populate the table
                self.tableWidget.setItem(i, 0, colID)
                # self.tableWidget.setItem(i, 1, userID)
                self.tableWidget.setItem(i, 1, title)
                self.tableWidget.setItem(i, 2, username)
                self.tableWidget.setItem(i, 3, password)
                self.tableWidget.setItem(i, 4, desc)
                self.tableWidget.setItem(i, 5, cat)
                self.tableWidget.setItem(i, 6, email)
                self.tableWidget.setItem(i, 7, created)
                self.tableWidget.setItem(i, 8, updated)
                self.tableWidget.setItem(i, 9, strength)

        self.tableWidget.resizeColumnsToContents()  # resizes the columns to fit the content read from file

        # font.setBold(True)  # set header titles to bold
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)  # align the table text to centre of cells
        # tableWidget.setIconSize(QtCore.QSize(20, 20))  # sets the size of the icons (had them added previously but removed for now)
        # tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        # tableWidget.horizontalHeader().setDefaultSectionSize(233)
        # tableWidget.horizontalHeader().setMinimumSectionSize(50)
        # tableWidget.verticalHeader().setDefaultSectionSize(30)
        # tableWidget.verticalHeader().setMinimumSectionSize(20)
        # tableWidget.verticalHeader().setSortIndicatorShown(False)

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
        list = functions.questions(1)
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
    def __init__(self, username, password, ID):
        super().__init__()
        # QDialog.__init__()
        self.echo_mode = False
        self.session_username = username
        self.session_password = password
        self.session_ID = ID
        nameLabel = QLabel("Name: ")
        self.nameEdit = QLineEdit()
        usernameLabel = QLabel("Username:")
        self.usernameEdit = QLineEdit()
        passwordLabel = QLabel("Password:")
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        password_check_Label = QLabel("Confirm Password:")
        self.password_check_Edit = QLineEdit()
        self.password_check_Edit.setEchoMode(QLineEdit.Password)
        w = QWidget()
        w.resize(200, 200)
        descriptionLabel = QLabel("Description:")
        self.descriptionEdit = QPlainTextEdit(w)
        RegisterEnailLabel = QLabel("Please enter the registered email address:")
        self.RegisterEnailEdit = QLineEdit()
        CategoryLabel = QLabel("Please chose a category")
        list = functions.categories()
        self.combo = QComboBox()
        self.combo.addItems(list)
        button_submit = QtWidgets.QPushButton('Login')
        button_submit.setShortcut("Return")
        button_submit.clicked.connect(lambda: self.submit())
        button_suggest_password = QtWidgets.QPushButton('Suggest password', default=False, autoDefault=False)
        button_suggest_password.clicked.connect(lambda : self.suggest_password())
        # button_create_account.clicked.connect(lambda: self.showCreateAccount())
        # self.combo_text = self.combo.currentText()
        button_show_password = QtWidgets.QPushButton(r'Show/Hide Password', default=False, autoDefault=False)
        button_show_password.clicked.connect(lambda : self.show_password())
        vbox = QtWidgets.QGridLayout()
        vbox.addWidget(nameLabel,0,0)
        vbox.addWidget(self.nameEdit,0,1)
        vbox.addWidget(usernameLabel,1,0)
        vbox.addWidget(self.usernameEdit,1,1)
        vbox.addWidget(passwordLabel,2,0)
        vbox.addWidget(self.passwordEdit,2,1)
        vbox.addWidget(button_suggest_password,2,2)
        vbox.addWidget(password_check_Label,3,0)
        vbox.addWidget(self.password_check_Edit,3,1)
        vbox.addWidget(button_show_password,3,2)
        # vbox.addWidget(descriptionLabel)
        # vbox.addWidget(self.descriptionEdit)
        # vbox.addWidget(RegisterEnailLabel)
        # vbox.addWidget(self.RegisterEnailEdit)
        # vbox.addWidget(CategoryLabel)
        # vbox.addWidget(self.combo)
        # vbox.addWidget(button_submit)
        self.setLayout(vbox)

    def submit(self):
        if str(self.passwordEdit.text()) == str(self.password_check_Edit.text()):
            print(self.session_username)
            print(str(self.nameEdit.text()))
            print(str(self.usernameEdit.text()))
            print(str(self.descriptionEdit.toPlainText()))
            print(str(self.RegisterEnailEdit.text()))
            print(str(self.combo.currentText()))
        else:
            QtWidgets.QMessageBox.warning(self, "Password Manager Notification", "Password not match!",
                                          QtWidgets.QMessageBox.Ok)

    def suggest_password(self):
        get_int, ok = QtWidgets.QInputDialog.getInt(self, "Password Manager Input", "Please chose suggest password length:")
        random_password = functions.RandomPassWordGen_UI(get_int)
        QtWidgets.QMessageBox.warning(self, "Password Manager Suggest Password", "Your suggest password: "+ random_password,
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
    # controller = Login()
    controller = PasswordManagerMenu("test","test",1)
    controller.show()
    app.exec()