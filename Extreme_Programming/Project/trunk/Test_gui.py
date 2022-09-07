__author__ ="penclai"

from unittest import TestCase
from unittest.mock import patch

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
import mock
from trunk.PasswordManager_menu import *

# from PasswordManager_menu import Login
app = QApplication(sys.argv)
class TestPasswordManager(TestCase):

    def setUp(self):
        self.userlogin = Login()
        self.create_password = TabNewPassword("Aiden","abc",1)

    def test_default_lineEdit(self):
        self.userlogin.lineEdit_username.setText("Aiden")
        self.assertEqual(self.userlogin.lineEdit_username.text(),'Aiden')
        self.userlogin.lineEdit_password.setText("abc")
        self.assertEqual(self.userlogin.lineEdit_password.text(),'abc')
        QTest.mouseClick(self.userlogin.button_login, Qt.LeftButton)
        QTest.mouseClick(self.userlogin.button_login, Qt.LeftButton)

    def test_create_password_strengh_checker(self):
        #test password input
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
        #test for show hide password
        self.create_password.echo_mode = False
        QTest.mouseClick(self.create_password.button_show_password, Qt.LeftButton)
        self.assertEqual(self.create_password.passwordEdit.echoMode(), 0)

    def test_default_imput(self):
        self.create_password.nameEdit.setText("google")
        self.assertEqual(self.create_password.nameEdit.text(),'google')


    # @patch.object(QtWidgets.QMessageBox, 'aboutQt')
    # @mock.patch('PyQt5.QtWidgets.QMessageBox.warning(self, "Password Manager Notification", "Password not match!",QtWidgets.QMessageBox.Ok)')
    # def test_same_name(self,mock_os):
    #     QTest.mouseClick(self.create_password.submit(), Qt.LeftButton)
    #     self.assertTrue(mock_os.called)
    #     # self.create_password.nameEdit.setText("Google general")
    #     # self.assertEqual(QTest.mouseClick(self.create_password.submit(), Qt.LeftButton),)



