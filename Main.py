import sys
import os.path
import platform

## Warning, Info & Help Messages
import tkinter as tk
root = tk.Tk()
root.withdraw()

## UI classes
from loginwindow import Ui_Form
from mainwindow import *
from mainwindow_functions import *
from PySide6.QtWidgets import QTableWidget, QApplication

## Logging directory creation
import logging
try:
    directory = "Barangay-System"
    parent_dir = "C:"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
except: pass

logging.basicConfig(
    filename=r'C:\Barangay-System\Info.log',
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

## database access
import database
database.initialize_database(True)

class LoginWindow(QMainWindow):
    def __init__(self):
        ## MENU INSTANCES
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## BUTTON INTERACTABLES
        self.ui.pushButton_2.clicked.connect(lambda: self.exit())
        self.ui.pushButton.clicked.connect(lambda: self.login())

        ## SHOW
        self.show()


    def login(self):
        try:
            username = self.ui.lineEdit_2.text()
            password = self.ui.lineEdit.text()
            res = database.authenticate_login(username,password)
            if res == 1:
                self.main = MainWindow()
                self.main.show()
                self.close()
                logging.info("[ Successfully Logged In ]")
            else:
                self.ui.label_3.setText("Incorrect Username or Password")
        except:
            self.ui.label_3.setText("Database is Offline: Please Restart")
            logging.info("[ SQL Database is Offline ]")


    def exit(self):
        sys.exit(0)

## End of Login Window


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        database.get_officials_data(self)
        database.get_residents_data(self)

        ## Cell Detectors
        self.ui.residentTableWidget.selectionModel().selectionChanged.connect(self.on_resident_changed)
        self.ui.tableWidget.selectionModel().selectionChanged.connect(self.on_official_changed)

        ## Burger Menu Interface Animation
        self.ui.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(True))

        ## Incoming Page

        self.ui.btn_dashboard.clicked.connect(lambda: self.open_dashboard())
        self.ui.btn_residents.clicked.connect(lambda: self.open_residents())
        self.ui.btn_officials.clicked.connect(lambda: self.open_officials())
        self.ui.btn_settings.clicked.connect(lambda: self.open_settings())
        self.ui.btn_logout.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.logout()))

        ## Dashboard Buttons
        self.ui.btn_editOfficial.clicked.connect(lambda: database.edit_official(self,0))

        ## Dashboard Buttons
        self.ui.dash_refresh.clicked.connect(lambda: self.refresh_dashboard())
        self.ui.btn_insertOfficial.clicked.connect(lambda: self.insert_dashboard())
        self.ui.btn_saveResident.clicked.connect(lambda: self.save_resident_changes())

        self.show()


## DASHBOARD FUNCTIONS
    def open_dashboard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_dashboard)
        database.get_officials_data(self)

    def refresh_dashboard(self):
        database.get_officials_data(self)

    def insert_dashboard(self):
        database.insert_new_officials(self)
        database.get_officials_data(self)

    def on_official_changed(self,selected,deselected):
        for ix in selected.indexes():
            cell = int(ix.row())



## RESIDENT FUNCTIONS
    def open_residents(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_residents)
        database.get_residents_data(self)

    def on_resident_changed(self,selected,deselected):
        for ix in selected.indexes():
            cell = int(ix.row())
            database.relay_residents_data(self,cell)

    def save_resident_changes(self):
        database.edit_residents_data(self)
        database.get_residents_data(self)

## OTHERS
    def open_officials(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_officials)

    def open_settings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_settings)

    def toggleMenu(self, enable):
        global switch
        UIFunctions.toggleMenu(self, 250, True)

        cfont = QFont()
        cfont.setFamilies([u"Segoe UI Semibold"])
        cfont.setPointSize(13)

        dfont = QFont()
        dfont.setBold(True)
        dfont.setFamilies([u"dripicons-v2"])
        dfont.setPointSize(15)

        if self.ui.btn_dashboard.text() == ("🖥️Dashboard"):
            self.ui.btn_dashboard.setFont(dfont)
            self.ui.btn_dashboard.setText("🖥️")
        else:
            self.ui.btn_dashboard.setFont(cfont)
            self.ui.btn_dashboard.setText("🖥️Dashboard")

        if self.ui.btn_residents.text() == ("👪Residents  "):
            self.ui.btn_residents.setFont(dfont)
            self.ui.btn_residents.setText("👪")
        else:
            self.ui.btn_residents.setFont(cfont)
            self.ui.btn_residents.setText("👪Residents  ")

        if self.ui.btn_officials.text() == ("🗃️Accounts  "):
            self.ui.btn_officials.setFont(dfont)
            self.ui.btn_officials.setText("🗃️")
        else:
            self.ui.btn_officials.setFont(cfont)
            self.ui.btn_officials.setText("🗃️Accounts  ")

        if self.ui.btn_forms.text() == ("📃Forms       "):
            self.ui.btn_forms.setFont(dfont)
            self.ui.btn_forms.setText("📃")
        else:
            self.ui.btn_forms.setFont(cfont)
            self.ui.btn_forms.setText("📃Forms       ")

        if self.ui.btn_settings.text() == ("⚙Settings   "):
            self.ui.btn_settings.setFont(dfont)
            self.ui.btn_settings.setText("⚙")
        else:
            self.ui.btn_settings.setFont(cfont)
            self.ui.btn_settings.setText("⚙Settings   ")


    def logout(self):
        logging.info("[ User Logged Out ]")
        self.main = LoginWindow()
        self.main.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())