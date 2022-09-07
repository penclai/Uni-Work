__author__ ="penclai"

from unittest import TestCase

import pytest
from PyQt5.QtTest import QTest
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
from trunk.PasswordManager_menu import *
from trunk.PasswordManager_function import *

# from PasswordManager_menu import Login
app = QApplication(sys.argv)


class TestPasswordManager(TestCase):

    def setUp(self):
        self.userlogin = Login()
        self.usercreate = create_account()
        self.passchange = TabChangePassword("Laura", "1234", "12")
        self.securitychange = TabSecurityQuestion("Laura", "1234", "12")
        self.create_password = TabNewPassword("Aiden", "abc", 1)
        self.search_password = TabSearchPassword("Aiden", "abc", 1)
        self.account = TabAccounts("Aiden", "abc", 1)

    def test_default_lineEdit(self):
        # Login tab testing
        self.userlogin.lineEdit_username.setText("Aiden")
        self.assertEqual(self.userlogin.lineEdit_username.text(), 'Aiden')
        self.userlogin.lineEdit_password.setText("abc")
        self.assertEqual(self.userlogin.lineEdit_password.text(), 'abc')
        QTest.mouseClick(self.userlogin.button_login, Qt.LeftButton)
        QTest.mouseClick(self.usercreate.button_create, Qt.LeftButton)

        # Account Setting(Password) tab testing
        self.passchange.CurrentUsernameEdit.setText("Laura")
        self.assertEqual(self.passchange.CurrentUsernameEdit.text(), "Laura")
        self.passchange.CurrentPasswordEdit.setText("1234")
        self.assertEqual(self.passchange.CurrentPasswordEdit.text(), "1234")
        self.passchange.NewPasswordEdit.setText("12345")
        self.assertEqual(self.passchange.NewPasswordEdit.text(), "12345")
        self.passchange.NewPasswordConfirmEdit.setText("12345")
        self.assertEqual(self.passchange.NewPasswordConfirmEdit.text(), "12345")
        QTest.mouseClick(self.passchange.button_show_password1, QtCore.Qt.LeftButton)
        QTest.mouseClick(self.passchange.button_enter, QtCore.Qt.LeftButton)

        # Account Setting(Security Questions) tab testing
        self.securitychange.list1 = functions.questions(2)
        self.securitychange.currentEdit.setText("blue")
        self.assertEqual(self.securitychange.currentEdit.text(), "blue")
        self.securitychange.list1 = functions.questions(1)
        self.securitychange.newEdit.setText("Hogwarts")
        self.assertEqual(self.securitychange.newEdit.text(), "Hogwarts")
        okWidget = self.securitychange.buttonbox.button(self.securitychange.buttonbox.Ok)
        QTest.mouseClick(okWidget, QtCore.Qt.LeftButton)
        cancelWidget = self.securitychange.buttonbox.button(self.securitychange.buttonbox.Cancel)
        QTest.mouseClick(cancelWidget, QtCore.Qt.LeftButton)

    # def test_menu_buttons(self):
    # Login tab testing

    # QTest.mouseClick(self.userlogin.exitAct, QtCore.Qt.LeftButton)
    # aboutopt = self.userlogin.actionAbout.triggered
    # QTest.mouseClick(aboutopt, QtCore.Qt.LeftButton)
    # self.assertEqual(self.userlogin.actionAbout.triggered, "true")
    # QTest.mouseClick(self.userlogin.forgetPassword, QtCore.Qt.LeftButton)
    def test_create_password_strengh_checker(self):
        # test password input
        self.create_password.passwordEdit.setText("abcdefg")
        self.assertEqual(self.create_password.passwordEdit.text(), "abcdefg")
        self.assertEqual(self.create_password.passwordEdit.styleSheet(), "background-color: rgb(255, 127, 127);")
        self.create_password.passwordEdit.setText("abcdefgh")
        self.assertEqual(self.create_password.passwordEdit.text(), "abcdefgh")
        self.assertEqual(self.create_password.passwordEdit.styleSheet(), "background-color: rgb(255, 255, 127);")
        self.create_password.passwordEdit.setText("abcde*A0")
        self.assertEqual(self.create_password.passwordEdit.styleSheet(), "background-color: rgb(200, 255, 200);")
        self.create_password.passwordEdit.setText("abcde*A00A**")
        self.assertEqual(self.create_password.passwordEdit.styleSheet(), "background-color: rgb(127, 255, 127);")

        # @patch("TabNewPassword")

    def test_create_password_button(self):
        # QTest.mouseClick(self.create_password.button_suggest_password, Qt.LeftButton)
        # test for show hide password
        self.create_password.echo_mode = False
        QTest.mouseClick(self.create_password.button_show_password, Qt.LeftButton)
        self.assertEqual(self.create_password.passwordEdit.echoMode(), 0)
        QTest.mouseClick(self.create_password.button_show_password, Qt.LeftButton)
        self.assertEqual(self.create_password.passwordEdit.echoMode(), 2)

    def test_default_input(self):
        self.create_password.nameEdit.setText("google")
        self.assertEqual(self.create_password.nameEdit.text(), 'google')
        self.create_password.usernameEdit.setText("google")
        self.assertEqual(self.create_password.usernameEdit.text(), 'google')
        self.create_password.passwordEdit.setText("abcde*A00A**")
        self.assertEqual(self.create_password.passwordEdit.text(), 'abcde*A00A**')
        self.create_password.password_check_Edit.setText("abcde*A00A**")
        self.assertEqual(self.create_password.password_check_Edit.text(), 'abcde*A00A**')

    def test_search_password_switcher(self):
        self.search_password.enable_mode = False
        QTest.mouseClick(self.search_password.button_switch, Qt.LeftButton)
        self.assertEqual(self.search_password.combo_category.isEnabled(), True)
        QTest.mouseClick(self.search_password.button_switch, Qt.LeftButton)
        self.assertEqual(self.search_password.combo_category.isEnabled(), False)

    def test_combo_placeholder_text(self):
        #set to advance search
        self.search_password.combo_search.setCurrentIndex(6)
        self.assertEqual(self.search_password.SearchEdit.placeholderText(),'Example:((Category:Email)AND(Description:mclaren))OR(Username:norris)')
        self.search_password.combo_search.setCurrentIndex(5) # set back to normal
        self.assertEqual(self.search_password.SearchEdit.placeholderText(),'')
        self.search_password.combo_search.setCurrentIndex(0) # set back to normal
        self.assertEqual(self.search_password.SearchEdit.placeholderText(),'')

    def test_advance_search(self):
        self.search_password.combo_search.setCurrentIndex(6)
        self.search_password.SearchEdit.setText("(des:google)")
        QTest.mouseClick(self.search_password.button_search, Qt.LeftButton)
        self.assertEqual(self.search_password.tableWidget.rowCount(),1)

    def test_account_rows(self):
        rows = 0
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\AccountPassword.csv"), "r",
                  encoding='utf8') as datafile:
            csv_reader = csv.reader(datafile, delimiter=',')
            next(csv_reader)
            list_csv = list(csv_reader)
            rows = len(list_csv)
        self.assertEqual(self.account.tableWidget.rowCount(),rows)