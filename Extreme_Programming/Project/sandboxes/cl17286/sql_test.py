from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QComboBox, QCheckBox, QGroupBox, QVBoxLayout, QWidget, \
    QLabel, QLineEdit, QDialogButtonBox, QAction, qApp, QMenuBar, QPlainTextEdit, QMessageBox, QTableWidget, \
    QTableWidgetItem, QStatusBar, QMainWindow
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import csv
import csv
# from trunk.PasswordManager_function import functions
from PasswordManager_function import functions
# import sqlite3
#
# con = sqlite3.Connection('newdb.sqlite')
# cur = con.cursor()
# cur.execute('CREATE TABLE "stuff" ("one" varchar(12), "two" varchar(12));')
#
# f = open('stuff.csv')
# csv_reader = csv.reader(f, delimiter=',')
#
# cur.executemany('INSERT INTO stuff VALUES (?, ?)', csv_reader)
# cur.close()
# con.commit()
# con.close()
# f.close()

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
        list_search = ["All", "Password Name", "Description", "Username", "Password"]
        self.combo_search = QComboBox()
        self.combo_search.addItems(list_search)
        category_label = QLabel("Category:")
        list_category = functions.categories()
        self.combo_category = QComboBox()
        self.combo_category.setEnabled(False)
        self.combo_category.addItems(list_category)
        self.button_switch = QtWidgets.QPushButton('Switch to Category')
        self.button_switch.clicked.connect(lambda: self.enable_category())
        button_search = QtWidgets.QPushButton('Search')
        button_search.clicked.connect(lambda: self.search())
        vbox = QtWidgets.QGridLayout()
        vbox.addWidget(SearchLabel, 0, 0)
        vbox.addWidget(self.SearchEdit, 0, 1)
        vbox.addWidget(self.combo_search, 0, 2)
        vbox.addWidget(category_label, 1, 0)
        vbox.addWidget(self.combo_category, 1, 1)
        vbox.addWidget(self.button_switch, 1, 2)
        vbox.addWidget(button_search, 2, 2)
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
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/AccountPassword.csv"), "r",
                  encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # lines = csv_file.readlines()
            next(csv_reader)
            lines = list(csv_reader)
            csv_file.close()
        self.tableWidget.setRowCount(len(lines))  # set the number of rows to be = to the nr of lines read from file

        # loop that processes lines from the file
        for i in range(0, len(lines)):
            if int(lines[i][1]) == self.session_ID and str(lines[i][6]) == category:
                for column_number, data in enumerate(lines[i]):
                    # print(str(column_number)+ ":"+(data))
                    if column_number < 1:
                        self.tableWidget.setItem(i, column_number, QTableWidgetItem(data))
                    elif column_number > 1:
                        self.tableWidget.setItem(i, (column_number - 1), QTableWidgetItem(data))

        self.tableWidget.resizeColumnsToContents()

        # for i in range(0, len(lines)):
        #     tokens = lines[i].strip().split(",")  # split the lines by "," and store list of strings as tokens
        #     if int(tokens[1]) == self.session_ID and category == tokens[6] :
        #         colID = QTableWidgetItem(tokens[0])
        #         # userID = QTableWidgetItem(tokens[1])
        #         title = QTableWidgetItem(tokens[2])
        #         username = QTableWidgetItem(tokens[3])
        #         password = QTableWidgetItem(tokens[4])
        #         desc = QTableWidgetItem(tokens[5])
        #         cat = QTableWidgetItem(tokens[6])
        #         email = QTableWidgetItem(tokens[7])
        #         created = QTableWidgetItem(tokens[8])
        #         updated = QTableWidgetItem(tokens[9])
        #         strength = QTableWidgetItem(tokens[10])
        #
        #         # populate the table
        #         self.tableWidget.setItem(i, 0, colID)
        #         # self.tableWidget.setItem(i, 1, userID)
        #         self.tableWidget.setItem(i, 1, title)
        #         self.tableWidget.setItem(i, 2, username)
        #         self.tableWidget.setItem(i, 3, password)
        #         self.tableWidget.setItem(i, 4, desc)
        #         self.tableWidget.setItem(i, 5, cat)
        #         self.tableWidget.setItem(i, 6, email)
        #         self.tableWidget.setItem(i, 7, created)
        #         self.tableWidget.setItem(i, 8, updated)
        #         self.tableWidget.setItem(i, 9, strength)
        # self._delegate.setFilters(list(set(category.split())))
        # self.tableWidget.findItems(str(category),QtCore.Qt.MatchContains)
        self.tableWidget.resizeColumnsToContents()

    def search(self):
        print(str(self.combo_category.currentText()))
        self.tableWidget.clearContents()
        # self.tableWidget.show()

        self.set_table(str(self.combo_category.currentText()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # controller = Login()
    # controller = create_account()
    controller = TabSearchPassword("test", "test", 1)
    controller.show()
    app.exec()
