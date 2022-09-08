from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QComboBox, QCheckBox, QGroupBox, QVBoxLayout, QWidget, \
    QLabel, QLineEdit, QDialogButtonBox, QAction, qApp, QMenuBar, QPlainTextEdit, QMessageBox, QTableWidget, \
    QTableWidgetItem, QStatusBar, QMainWindow, QErrorMessage
from PyQt5.QtCore import *
import pandas as pd
import re, sys, os, csv, nltk, json, time
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from elasticsearch import Elasticsearch, helpers
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from itertools import islice, chain
import Assigment1
from tkinter import messagebox





class ManagerMenu(QDialog):
    def __init__(self):
        super().__init__()
        # QDialog.__init__()
        self.setWindowTitle("Manager Menu")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(1500, 600)  # window size - please keep it a larger size, it's easier to test
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
        # welcome_label.setText('<font size="5"> Welcome Back ' + self.global_username + '<font size="5">')
        tabWidget = QTabWidget()

        tabWidget.setFont(QtGui.QFont("Arial", 12))
        tabWidget.addTab(TabSearch(), "Search")

        vbox.addWidget(menubar)
        vbox.addWidget(welcome_label)
        vbox.addWidget(tabWidget)
        self.setLayout(vbox)

    def showInfo(self):
        QtWidgets.QMessageBox.about(self, "Search Manager About",
                                    "Elastic Manager created by Aiden Lai")
    def showSearchInfo(self):
        QtWidgets.QMessageBox.about(self, "Search Manager About",
                                    'Please key in anything to the search box,\n'
                                    'chose column using the drop down menu next to the input box')


class TabSearch(QWidget):
    def __init__(self):
        super().__init__()

        self.enable_mode = False
        groupBox = QGroupBox("Search search:")
        groupBox2 = QGroupBox("Result:")
        SearchLabel = QLabel("Search: ")
        self.SearchEdit = QLineEdit()
        self.list_search = ["Title", "Plot", "Director", "Cast", "Origin/Ethnicity","Genre","Release Year"]
        self.combo_search = QComboBox()
        self.combo_search.addItems(self.list_search)
        self.button_search = QtWidgets.QPushButton('Search')
        self.button_search.clicked.connect(lambda: self.search())
        self.button_show = QtWidgets.QPushButton('Show All')
        self.button_show.clicked.connect(lambda: self.show_all())
        vbox = QtWidgets.QGridLayout()
        vbox.addWidget(SearchLabel, 0, 0)
        vbox.addWidget(self.SearchEdit, 0, 1)
        vbox.addWidget(self.combo_search, 0, 2)
        vbox.addWidget(self.button_search, 1, 2)
        vbox.addWidget(self.button_show, 2, 2)
        vbox2 = QVBoxLayout()
        ########## Table Setting
        self.tableWidget = QTableWidget(1, 8)  # create the table with 1 row and 11 columns
        self.columnNames = [ "Title", "Release Year", "Origin/Ethnicity", "Genre", "Director", "Cast", "Plot",
                            "Wiki Page"]  # setting the column names
        self.tableWidget.setHorizontalHeaderLabels(
            self.columnNames)  # setting the headers of the table to match column names
        # self.setGeometry(50, 50, 1000, 800)
        font = QtGui.QFont("Arial", 12)  # selecting font and size
        self.tableWidget.setFont(font)  # setting the font to the table
        self.tableWidget.setAlternatingRowColors(True)  # sets alternate row colours
        # self.tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)
        # self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setSortingEnabled(False)
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



    def set_table(self, category):
        self.tableWidget.setSortingEnabled(False)
        es = Elasticsearch()
        if category == 1:
            result = es.search(index="movies", body={
                "_source": ["Title","Release Year","Genre","Director","Origin/Ethnicity","Plot","Wiki Page","Plot_keyword","Cast"],
                "size": 20,
                "min_score": 0.5,
                "query": {
                    "bool": {
                        "must": [{
                            "match_phrase_prefix": {
                                "Title": {
                                    "query": "{}".format(str(self.SearchEdit.text()))
                                }
                            }
                        }]
                    }
                },
                "aggs": {
                    "auto_complete": {
                        "terms": {
                            "field": "title.keyword",
                            "order": {
                                "_count": "desc"
                            },
                            "size": 25
                        }
                    }
                }
            })
        elif category == 2:
            result = es.search(index="movies", body={
                "_source": ["Title","Release Year","Genre","Director","Origin/Ethnicity","Plot","Wiki Page","Plot_keyword","Cast"],
                "size": 20,
                "min_score": 0.5,
                "query": {
                    "bool": {
                        "must": [{
                            "match_phrase_prefix": {
                                "Plot_keyword": {
                                    "query": "{}".format(str(self.SearchEdit.text()))
                                }
                            }
                        }]
                    }
                },
                "aggs": {
                    "auto_complete": {
                        "terms": {
                            "field": "title.keyword",
                            "order": {
                                "_count": "desc"
                            },
                            "size": 25
                        }
                    }
                }
            })
        elif category == 3:
             result = es.search(index="movies", body={
                 "_source": ["Title","Release Year","Genre","Director","Origin/Ethnicity","Plot","Wiki Page","Plot_keyword","Cast"],
                 "size": 20,
                 "min_score": 0.5,
                 "query": {
                     "bool": {
                         "must": [{
                             "match_phrase_prefix": {
                                 "Director": {
                                     "query": "{}".format(str(self.SearchEdit.text()))
                                 }
                             }
                         }]
                     }
                 },
                 "aggs": {
                     "auto_complete": {
                         "terms": {
                             "field": "title.keyword",
                             "order": {
                                 "_count": "desc"
                             },
                             "size": 25
                         }
                     }
                 }
             })
        elif category == 4:
            result = es.search(index="movies", body={
                "_source": ["Title","Release Year","Genre","Director","Origin/Ethnicity","Plot","Wiki Page","Plot_keyword","Cast"],
                "size": 20,
                "min_score": 0.5,
                "query": {
                    "bool": {
                        "must": [{
                            "match_phrase_prefix": {
                                "Cast": {
                                    "query": "{}".format(str(self.SearchEdit.text()))
                                }
                            }
                        }]
                    }
                },
                "aggs": {
                    "auto_complete": {
                        "terms": {
                            "field": "title.keyword",
                            "order": {
                                "_count": "desc"
                            },
                            "size": 25
                        }
                    }
                }
            })
        elif category == 5:
            result = es.search(index="movies", body={
                "_source": ["Title","Release Year","Genre","Director","Origin/Ethnicity","Plot","Wiki Page","Plot_keyword","Cast"],
                "size": 20,
                "min_score": 0.5,
                "query": {
                    "bool": {
                        "must": [{
                            "match_phrase_prefix": {
                                "Origin/Ethnicity": {
                                    "query": "{}".format(str(self.SearchEdit.text()))
                                }
                            }
                        }]
                    }
                },
                "aggs": {
                    "auto_complete": {
                        "terms": {
                            "field": "title.keyword",
                            "order": {
                                "_count": "desc"
                            },
                            "size": 25
                        }
                    }
                }
            })

        elif category == 6:
            result = es.search(index="movies", body={
                "_source": ["Title","Release Year","Genre","Director","Origin/Ethnicity","Plot","Wiki Page","Plot_keyword","Cast"],
                "size": 20,
                "min_score": 0.5,
                "query": {
                    "bool": {
                        "must": [{
                            "match_phrase_prefix": {
                                "Genre": {
                                    "query": "{}".format(str(self.SearchEdit.text()))
                                }
                            }
                        }]
                    }
                },
                "aggs": {
                    "auto_complete": {
                        "terms": {
                            "field": "title.keyword",
                            "order": {
                                "_count": "desc"
                            },
                            "size": 25
                        }
                    }
                }
            })
        elif category == 7:
            result = es.search(index="movies", body={
                "_source": ["Title","Release Year","Genre","Director","Origin/Ethnicity","Plot","Wiki Page","Cast","Plot_keyword"],
                "size": 20,
                "min_score": 0.5,
                "query": {
                    "match":{
                        "Release Year": {
                            "query": int(self.SearchEdit.text())

                        }
                    }
                },
                "aggs": {
                    "auto_complete": {
                        "terms": {
                            "field": "title.keyword",
                            "order": {
                                "_count": "desc"
                            },
                            "size": 25
                        }
                    }
                }
            })

        # result_list = result.values.tolist()
        if len(result['hits']['hits']) != 0:
            self.tableWidget.setRowCount(len(result['hits']['hits']))
            print(result['hits']['hits'])
            print(len(result['hits']['hits']))
            # print(result)
            i = 0
            for row in result['hits']['hits']:
                print('debug')
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row['_source']['Release Year'])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row['_source']['Origin/Ethnicity'])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(row['_source']['Genre'])))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(row['_source']['Director'])))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(str(row['_source']['Cast'])))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(str(row['_source']['Plot'])))
                self.tableWidget.setItem(i, 7, QTableWidgetItem(str(row['_source']['Wiki Page'])))
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(row['_source']['Title'])))
                print(Assigment1.pretty_print_message(row['_source']))
                i = i+1
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

        else:
            QtWidgets.QMessageBox.about(self, "Search Manager Notification", "No result for : " + str(self.SearchEdit.text()) )



    def search(self):
        self.tableWidget.clearContents()
        if self.combo_search.currentText() == "Title":
            self.set_table(1)
        elif self.combo_search.currentText() == "Plot":
            self.set_table(2)
        elif self.combo_search.currentText() == "Director":
            self.set_table(3)
        elif self.combo_search.currentText() == "Cast":
            self.set_table(4)
        elif self.combo_search.currentText() == "Origin/Ethnicity":
            self.set_table(5)
        elif self.combo_search.currentText() == "Genre":
            self.set_table(6)
        elif self.combo_search.currentText() == "Release Year":
            self.set_table(7)


    def show_all(self):
        self.tableWidget.clearContents()
        self.tableWidget.setSortingEnabled(True)
        es = Elasticsearch()
        result = es.search(index="movies", body={
            "from": 0,
            "size": 1000,
            "query": {
                "match_all": {}
            }
        })
        i = 0
        print(len(result['hits']['hits']))
        for row in result['hits']['hits']:
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row['_source']['Release Year'])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row['_source']['Origin/Ethnicity'])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(row['_source']['Genre'])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(row['_source']['Director'])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(row['_source']['Cast'])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(row['_source']['Plot'])))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(row['_source']['Wiki Page'])))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(row['_source']['Title'])))
            print(Assigment1.pretty_print_message(row['_source']))
            i = i + 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()



if __name__ == '__main__':
    try:
        result = Assigment1.indexing() # call the indexing method
        if result[0] > 0:
            messagebox.showinfo("Search Manager","File uploaded successfully")
            app = QtWidgets.QApplication(sys.argv)
            controller = ManagerMenu()
            controller.show()
            app.exec()
        else:
            messagebox.showerror("Search Manager","An error occured!")
    except Exception as e:
        print(e)


