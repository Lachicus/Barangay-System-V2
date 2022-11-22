import mysql.connector
import logging

## UI Object access
from Main import *
from mainwindow import *
from PySide6.QtWidgets import *  # type: ignore
from datetime import date

## Warning, Info & Help Messages
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

logging.basicConfig(
    filename=r'C:\Barangay-System\database.log',
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
    )
    mycursor = mydb.cursor()
    mycursor2 = mydb.cursor()
except:
    messagebox.showwarning("Database Error", "MYSQL Database is appeared to be offline")
    logging.info("[ Database not Found ]")



def execute_multiple_statements(statement,message):
    result = mycursor.execute(statement, multi=True)
    result.send(None)
    logging.info(f"[ {message}, {result}]")


def initialize_database(init):
    try:
        execute_multiple_statements(
            "CREATE DATABASE BarangaySystemV2",
            "CREATE SCHEMA"
        )
        execute_multiple_statements(
            "CREATE TABLE BarangaySystemV2.officials "
            "(offcial_id INT AUTO_INCREMENT PRIMARY KEY, "
            "firstName VARCHAR(255), "
            "lastName VARCHAR(255), "
            "position VARCHAR(255), "
            "contactNumber VARCHAR(45))",
            "CREATE TABLE"
        )
        execute_multiple_statements(
            "CREATE TABLE BarangaySystemV2.credentials "
            "(credential_id INT AUTO_INCREMENT PRIMARY KEY, "
            "username VARCHAR(255),"
            "password VARCHAR(255))",
            "CREATE TABLE"
        )
        execute_multiple_statements(
            "CREATE TABLE BarangaySystemV2.residents "
            "(resident_id INT AUTO_INCREMENT PRIMARY KEY, "
            "firstName VARCHAR(255), "
            "lastName VARCHAR(255), "
            "middleName VARCHAR(255), "
            "gender VARCHAR(255), "
            "birthDate VARCHAR(255), "
            "fullAddress VARCHAR(255), "
            "voterStatus VARCHAR(255), "
            "civilStatus VARCHAR(255), "
            "birthPlace VARCHAR(255), "
            "citizenship VARCHAR(255), "
            "contactNumber INTEGER(15), "
            "residency INTEGER(50))",
            "CREATE TABLE"
        )
        execute_multiple_statements("INSERT INTO BarangaySystemV2.credentials (username, password) VALUES ('dfusrv2','dfpsdv2')","INSERT DATA")
        execute_multiple_statements("INSERT INTO BarangaySystemV2.credentials (username, password) VALUES ('user','pass')", "INSERT DATA")

        mydb.commit()
        logging.info("[ Database Initialized Successfully ]")
    except:
        pass

def authenticate_login(username,password):
    statement = f"SELECT * FROM BarangaySystemV2.credentials WHERE BINARY username = '{username}' AND BINARY password = '{password}'"
    mycursor.execute(statement)

    if mycursor.fetchone():
        return 1
    else:
        return 0


## Officials Database Remote

def get_officials_data(self):
    statement = "SELECT * FROM BarangaySystemV2.officials"
    mycursor.execute(statement)
    result = mycursor.fetchall()
    count = len(result)
    tablerow = 0
    self.ui.tableWidget.setRowCount(count)
    for row in result:
        self.ui.tableWidget.setItem(tablerow,0,QTableWidgetItem(row[1]))
        self.ui.tableWidget.setItem(tablerow,1, QTableWidgetItem(row[2]))
        self.ui.tableWidget.setItem(tablerow,2, QTableWidgetItem(row[3]))
        self.ui.tableWidget.setItem(tablerow,3, QTableWidgetItem(str(row[4])))
        tablerow = tablerow+1

    rowPosition = self.ui.tableWidget.rowCount()
    self.ui.tableWidget.insertRow(rowPosition)

    self.ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(""))
    self.ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(""))
    self.ui.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(""))
    self.ui.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(""))
    logging.info(" [ Official list Displayed ] ")



def insert_new_officials(self):
    statement = "SELECT * FROM BarangaySystemV2.officials"
    mycursor.execute(statement)
    count = len(mycursor.fetchall())

    firstName = self.ui.tableWidget.item(count, 0).text()
    lastName = self.ui.tableWidget.item(count, 1).text()
    position = self.ui.tableWidget.item(count, 2).text()
    contactNumber = self.ui.tableWidget.item(count, 3).text()

    if firstName and lastName and position:
        if  firstName.isspace() or lastName.isspace() or position.isspace():
            print("contains empty string")
        else:
            try:
                statement = f"INSERT INTO BarangaySystemV2.officials (firstName, lastName, position , contactNumber) VALUES ('{firstName}','{lastName}','{position}','{contactNumber}')"
                mycursor2.execute(statement)
                logging.info("[ Officials: Data Successfully Added.]")
            except:
                logging.info("[ Officials: Data insertion failed.]")
    else:
        messagebox.showwarning("Insert Officials","You Entered Incomplete or Blank Data")



def edit_official(self,cell):
    statement = "UPDATE BarangaySystemV2.officials SET position = 'Janitor' WHERE firstName = 'tobedeleted'"




def get_residents_data(self):
    statement = "SELECT * FROM BarangaySystemV2.residents"
    mycursor.execute(statement)
    result = mycursor.fetchall()
    count = len(result)
    tablerow = 0
    self.ui.residentTableWidget.setRowCount(count)
    for row in result:
        for index in range(12):
            self.ui.residentTableWidget.setItem(tablerow,index, QTableWidgetItem(str(row[index+1])))

        tablerow = tablerow+1

    rowPosition = self.ui.residentTableWidget.rowCount()
    self.ui.residentTableWidget.insertRow(rowPosition)

    for index in range(13):
        self.ui.residentTableWidget.setItem(tablerow, index, QTableWidgetItem(""))

    logging.info(" [ Resident list Displayed ] ")

identifier = ""
def relay_residents_data(self,cell):
    global identifier
    #try:
    firstName = self.ui.residentTableWidget.item(cell, 0).text()
    lastName = self.ui.residentTableWidget.item(cell, 1).text()
    middleName = self.ui.residentTableWidget.item(cell, 2).text()
    gender = self.ui.residentTableWidget.item(cell, 3).text()
    birthDate = self.ui.residentTableWidget.item(cell, 4).text()
    address = self.ui.residentTableWidget.item(cell, 5).text()
    voterStatus = self.ui.residentTableWidget.item(cell, 6).text()
    civilStatus = self.ui.residentTableWidget.item(cell, 7).text()
    birthPlace = self.ui.residentTableWidget.item(cell, 8).text()
    citizenship = self.ui.residentTableWidget.item(cell, 9).text()
    contactNumber = self.ui.residentTableWidget.item(cell, 10).text()
    residency = self.ui.residentTableWidget.item(cell, 11).text()

    formatdate = date.today()
    year = formatdate.year
    yearResult = year - int(residency)

    fullName = f"{firstName} {middleName} {lastName}"
    residencyYear = f"since {yearResult}"

    self.ui.ln_fullName.setText(fullName)
    self.ui.ln_fullAddress.setText(address)
    self.ui.ln_gender.setText(gender)
    self.ui.ln_civilStatus.setText(civilStatus)
    self.ui.ln_birthPlace.setText(birthPlace)
    self.ui.ln_birthDate.setText(birthDate)
    self.ui.ln_voterStatus.setText(voterStatus)
    self.ui.ln_citizenship.setText(citizenship)
    self.ui.ln_contactNumber.setText(contactNumber)
    self.ui.ln_residency.setText(residencyYear)
    identifier = firstName

    # except:
    #     logging.info(" [ An Error Ocurred Displaying Resident Preview ]")

def edit_residents_data(self):
    global identifier
    fullName = self.ui.ln_fullName.text().split(); count = 0
    for word in fullName:
        count = count+1
    last = count - 1; middle = last - 1; temp = ""
    for index in range(middle):
        temp = temp + " " +fullName[index]
    residency = self.ui.ln_residency.text().split()
    formatdate = date.today()
    year = formatdate.year
    yearTemp = int(residency[1])

    yearOfResidency = year - yearTemp
    firstName = temp.strip()
    lastName = fullName[last]
    middleName = fullName[middle]
    fullAddress = self.ui.ln_fullAddress.text()
    gender = self.ui.ln_gender.text()
    civilStatus = self.ui.ln_civilStatus.text()
    birthPlace = self.ui.ln_birthPlace.text()
    birthDate = self.ui.ln_birthDate.text()
    voterStatus = self.ui.ln_voterStatus.text()
    citizenship = self.ui.ln_citizenship.text()
    contactNumber = self.ui.ln_contactNumber.text()

    statement = f"UPDATE BarangaySystemV2.residents SET firstName='{firstName}', lastName='{lastName}', middleName='{middleName}', gender='{gender}', birthDate='{birthDate}', fullAddress='{fullAddress}', voterStatus='{voterStatus}', civilStatus='{civilStatus}', birthPlace='{birthPlace}', citizenship='{citizenship}', contactNumber='{contactNumber}', residency='{yearOfResidency}' WHERE firstName = '{identifier}'"
    mycursor.execute(statement)





