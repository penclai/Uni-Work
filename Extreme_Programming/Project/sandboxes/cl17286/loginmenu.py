import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui
from trunk.PasswordManager_main import on_startup


class MainWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        """QtWidgets.QWidget.__init__(self)"""
        self.setWindowTitle('Password Manager')
        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "Password Storage")
        tabwidget.addTab(SecondTab(), "Password Retrieval")
        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('Switch Window')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())


class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)


class Login(QDialog):
    switch_window = QtCore.pyqtSignal()
    username = ""
    password = ""

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

        self.button = QtWidgets.QPushButton('Login')
        # self.button.clicked.connect(lambda: on_startup.login_check(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        self.button.clicked.connect(lambda: on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text())))
        # self.button.clicked.connect(self.close)
        layout.addWidget(self.button)

        self.setLayout(layout)


    def login(self):
        a = on_startup()
        on_startup.login_onclick(str(self.lineEdit_username.text()), str(self.lineEdit_password.text()))
        QCoreApplication.instance().quit()

    # @staticmethod
    # def get_output():
    #     return Login.username, Login.password


class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        # self.login.switch_window.connect(self.show_main)
        self.login.show()




def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    app.exec_()


if __name__ == '__main__':
    main()