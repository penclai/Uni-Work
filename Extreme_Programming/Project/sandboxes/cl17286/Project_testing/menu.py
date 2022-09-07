from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QComboBox, QCheckBox, QGroupBox, QVBoxLayout, QWidget, \
    QLabel, QLineEdit, QDialogButtonBox,QAction, qApp, QMenuBar, QPlainTextEdit
import sys
from PyQt5.QtGui import QIcon



class PasswordManagerMenu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager Menu")
        self.setWindowIcon(QIcon("icon.png"))
        # self.setStyleSheet('background-color:grey')
        vbox = QVBoxLayout()
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        menubar = QMenuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        tabWidget = QTabWidget()
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        tabWidget.setFont(QtGui.QFont("Arial", 12))
        tabWidget.addTab(TabSearchPassword(), "Search")
        tabWidget.addTab(TabNewPassword(), "Create New Passowrd")
        tabWidget.addTab(TabChangePassword(), "Account Setting(Password)")
        tabWidget.addTab(TabSecurityQuestion(), "Account Setting(Security Question)")
        vbox.addWidget(menubar)
        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)


class TabChangePassword(QWidget):
    def __init__(self):
        super().__init__()
        CurrentPasswordLabel = QLabel("Please enter your current password: ")
        CurrentPasswordEdit = QLineEdit()
        NewPasswordLabel = QLabel("Please enter new password:")
        NewPasswordEdit = QLineEdit()
        NewPasswordConfirmLabel = QLabel("Please confirm password:")
        NewPasswordConfirmEdit = QLineEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(CurrentPasswordLabel)
        vbox.addWidget(CurrentPasswordEdit)
        vbox.addWidget(NewPasswordLabel)
        vbox.addWidget(NewPasswordEdit)
        vbox.addWidget(NewPasswordConfirmLabel)
        vbox.addWidget(NewPasswordConfirmEdit)
        self.setLayout(vbox)



class TabSecurityQuestion(QWidget):
    def __init__(self):
        super().__init__()
        groupBox = QGroupBox("Security Question")
        list = ["Your favourite place?", "What is your favourite colour?", "Your first school?", "Your pet name?"]
        combo = QComboBox()
        combo.addItems(list)
        vbox = QVBoxLayout()
        vbox.addWidget(combo)
        groupBox.setLayout(vbox)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
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
        RegisterEnailLabel = QLabel("Please enter the registered email adddress:")
        RegisterEnailEdit = QLineEdit()
        CategoryLabel = QLabel("Please chose a category")
        list = ["Email", "Work", "Study", "Entertainment", "Programming", "Others"]
        combo = QComboBox()
        combo.addItems(list)
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
        self.setLayout(vbox)

class TabSearchPassword(QWidget):
    def __init__(self):
        super().__init__()
        SearchLabel = QLabel("Search: ")
        SearchEdit = QLineEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(SearchLabel)
        vbox.addWidget(SearchEdit)

        self.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    tabdialog = PasswordManagerMenu()
    tabdialog.show()
    app.exec()

if __name__ == "__main__":
    main()