# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loginvXHqHp.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res.login.source_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
            Form.setWindowFlags(Qt.FramelessWindowHint)
            Form.setAttribute(Qt.WA_TranslucentBackground)
        Form.resize(325, 436)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 290, 410))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color:rgba(16,30,41,240);\n"
"border-radius:10px;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 20, 31, 21))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(163, 11, 42);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(240, 12, 58);\n"
"}")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 230, 250, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,225);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 330, 251, 31))
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 280, 250, 30))
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,225);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 380, 271, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 50, 171, 151))
        self.label.setStyleSheet(u"image: url(:/Prefix1/brgy_logo_ccexpress.png);")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 20, 31, 21))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(17, 133, 09);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 82, 27);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"X", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Type Your Username and Password", None))
        self.label.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"?", None))
    # retranslateUi

