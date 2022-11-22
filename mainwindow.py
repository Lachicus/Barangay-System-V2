# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainpwOeaD.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res.main.main_source_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1276, 685)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 50))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(60, 50))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(8, 60, 104);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(15)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255,255,255);\n"
"border:1px solid;\n"
"border-top-color:rgb(255,255,255);\n"
"border-left-color:rgb(255,255,255);\n"
"border-right-color:rgb(255,255,255);\n"
"border-bottom-color:rgb(255,255,255);\n"
"")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"background-color: rgb(8, 60, 104);")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(60, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(8, 60, 104);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_dashboard = QPushButton(self.frame_top_menus)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setMinimumSize(QSize(0, 60))
        self.btn_dashboard.setFont(font)
        self.btn_dashboard.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_dashboard)

        self.btn_residents = QPushButton(self.frame_top_menus)
        self.btn_residents.setObjectName(u"btn_residents")
        self.btn_residents.setMinimumSize(QSize(0, 60))
        self.btn_residents.setMaximumSize(QSize(16777215, 16777215))
        self.btn_residents.setFont(font)
        self.btn_residents.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_residents)

        self.btn_officials = QPushButton(self.frame_top_menus)
        self.btn_officials.setObjectName(u"btn_officials")
        self.btn_officials.setMinimumSize(QSize(0, 60))
        self.btn_officials.setFont(font)
        self.btn_officials.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_officials)

        self.btn_forms = QPushButton(self.frame_top_menus)
        self.btn_forms.setObjectName(u"btn_forms")
        self.btn_forms.setMinimumSize(QSize(0, 60))
        self.btn_forms.setFont(font)
        self.btn_forms.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_forms)

        self.btn_settings = QPushButton(self.frame_top_menus)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 60))
        self.btn_settings.setFont(font)
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_settings)

        self.filler = QPushButton(self.frame_top_menus)
        self.filler.setObjectName(u"filler")
        self.filler.setMinimumSize(QSize(0, 230))
        self.filler.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(8, 60, 104);\n"
"}")

        self.verticalLayout_4.addWidget(self.filler)

        self.btn_logout = QPushButton(self.frame_top_menus)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setEnabled(True)
        self.btn_logout.setMinimumSize(QSize(0, 30))
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_logout, 0, Qt.AlignBottom)

        self.pushButton = QPushButton(self.frame_top_menus)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(8, 60, 104);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(8, 60, 104);\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: rgb(29, 42, 53);")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.pg_dashboard = QWidget()
        self.pg_dashboard.setObjectName(u"pg_dashboard")
        self.label_4 = QLabel(self.pg_dashboard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(640, 30, 251, 111))
        self.label_4.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"")
        self.label_5 = QLabel(self.pg_dashboard)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(900, 30, 251, 111))
        self.label_5.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"\n"
"")
        self.label_6 = QLabel(self.pg_dashboard)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(640, 150, 251, 111))
        self.label_6.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"\n"
"")
        self.label_7 = QLabel(self.pg_dashboard)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(900, 150, 251, 111))
        self.label_7.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"\n"
"")
        self.label_2 = QLabel(self.pg_dashboard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(640, 40, 251, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"color:rgb(1,1,1)")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.pg_dashboard)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(900, 40, 251, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.pg_dashboard)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(640, 160, 251, 20))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.pg_dashboard)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(900, 160, 251, 20))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.pg_dashboard)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(25, 39, 501, 501))
        self.label_11.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"")
        self.label_12 = QLabel(self.pg_dashboard)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(35, 39, 481, 31))
        font3 = QFont()
        font3.setPointSize(17)
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"")
        self.tableWidget = QTableWidget(self.pg_dashboard)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(254, 254, 254));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 70, 491, 461))
        self.tableWidget.setStyleSheet(u"Background-color:rgb(152, 193, 217)")
        self.groupBox = QGroupBox(self.pg_dashboard)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(630, 10, 531, 261))
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"color: rgb(152, 193, 217);\n"
"")
        self.groupBox_2 = QGroupBox(self.pg_dashboard)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 531, 591))
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"color: rgb(152, 193, 217);\n"
"")
        self.btn_insertOfficial = QPushButton(self.groupBox_2)
        self.btn_insertOfficial.setObjectName(u"btn_insertOfficial")
        self.btn_insertOfficial.setGeometry(QRect(20, 540, 111, 41))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(False)
        self.btn_insertOfficial.setFont(font5)
        self.btn_insertOfficial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_insertOfficial.setAutoFillBackground(False)
        self.btn_insertOfficial.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(17, 133, 09);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 82, 27);\n"
"}")
        self.btn_removeOfficial = QPushButton(self.groupBox_2)
        self.btn_removeOfficial.setObjectName(u"btn_removeOfficial")
        self.btn_removeOfficial.setGeometry(QRect(400, 540, 111, 41))
        self.btn_removeOfficial.setFont(font5)
        self.btn_removeOfficial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_removeOfficial.setAutoFillBackground(False)
        self.btn_removeOfficial.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(163, 11, 42);\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(240, 12, 58);\n"
"}")
        self.btn_editOfficial = QPushButton(self.groupBox_2)
        self.btn_editOfficial.setObjectName(u"btn_editOfficial")
        self.btn_editOfficial.setGeometry(QRect(140, 540, 111, 41))
        self.btn_editOfficial.setFont(font5)
        self.btn_editOfficial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editOfficial.setAutoFillBackground(False)
        self.btn_editOfficial.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(17, 133, 09);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 82, 27);\n"
"}")
        self.groupBox_3 = QGroupBox(self.pg_dashboard)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(630, 280, 531, 241))
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet(u"color: rgb(152, 193, 217);\n"
"")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 40, 191, 171))
        self.label_13.setStyleSheet(u"image: url(:/logo/brgy_logo_ccexpress.png);")
        self.dash_refresh = QPushButton(self.groupBox_3)
        self.dash_refresh.setObjectName(u"dash_refresh")
        self.dash_refresh.setGeometry(QRect(340, 150, 141, 51))
        font6 = QFont()
        font6.setBold(True)
        self.dash_refresh.setFont(font6)
        self.dash_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.dash_refresh.setAutoFillBackground(False)
        self.dash_refresh.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(17, 133, 09);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 82, 27);\n"
"}")
        self.brgy_population = QLabel(self.pg_dashboard)
        self.brgy_population.setObjectName(u"brgy_population")
        self.brgy_population.setGeometry(QRect(640, 80, 251, 41))
        font7 = QFont()
        font7.setPointSize(20)
        self.brgy_population.setFont(font7)
        self.brgy_population.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"color:rgb(1,1,1)")
        self.brgy_population.setAlignment(Qt.AlignCenter)
        self.brgy_male = QLabel(self.pg_dashboard)
        self.brgy_male.setObjectName(u"brgy_male")
        self.brgy_male.setGeometry(QRect(640, 200, 251, 41))
        self.brgy_male.setFont(font7)
        self.brgy_male.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"color:rgb(1,1,1)")
        self.brgy_male.setAlignment(Qt.AlignCenter)
        self.brgy_voters = QLabel(self.pg_dashboard)
        self.brgy_voters.setObjectName(u"brgy_voters")
        self.brgy_voters.setGeometry(QRect(900, 80, 251, 41))
        self.brgy_voters.setFont(font7)
        self.brgy_voters.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"color:rgb(1,1,1)")
        self.brgy_voters.setAlignment(Qt.AlignCenter)
        self.brgy_female = QLabel(self.pg_dashboard)
        self.brgy_female.setObjectName(u"brgy_female")
        self.brgy_female.setGeometry(QRect(900, 200, 251, 41))
        self.brgy_female.setFont(font7)
        self.brgy_female.setStyleSheet(u"background-color: rgb(61, 90, 128);\n"
"color:rgb(1,1,1)")
        self.brgy_female.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pg_dashboard)
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.tableWidget.raise_()
        self.groupBox_3.raise_()
        self.brgy_population.raise_()
        self.brgy_male.raise_()
        self.brgy_voters.raise_()
        self.brgy_female.raise_()
        self.pg_residents = QWidget()
        self.pg_residents.setObjectName(u"pg_residents")
        self.groupBox_4 = QGroupBox(self.pg_residents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 0, 1181, 611))
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setStyleSheet(u"color: rgb(152, 193, 217);\n"
"")
        self.btn_insertResident = QPushButton(self.groupBox_4)
        self.btn_insertResident.setObjectName(u"btn_insertResident")
        self.btn_insertResident.setGeometry(QRect(10, 560, 111, 41))
        self.btn_insertResident.setFont(font5)
        self.btn_insertResident.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_insertResident.setAutoFillBackground(False)
        self.btn_insertResident.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(17, 133, 09);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 82, 27);\n"
"}")
        self.btn_removeResident = QPushButton(self.groupBox_4)
        self.btn_removeResident.setObjectName(u"btn_removeResident")
        self.btn_removeResident.setGeometry(QRect(130, 560, 111, 41))
        self.btn_removeResident.setFont(font5)
        self.btn_removeResident.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_removeResident.setAutoFillBackground(False)
        self.btn_removeResident.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(163, 11, 42);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(240, 12, 58);\n"
"}")
        self.btn_saveResident = QPushButton(self.groupBox_4)
        self.btn_saveResident.setObjectName(u"btn_saveResident")
        self.btn_saveResident.setGeometry(QRect(680, 490, 91, 41))
        self.btn_saveResident.setFont(font5)
        self.btn_saveResident.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saveResident.setAutoFillBackground(False)
        self.btn_saveResident.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(17, 133, 09);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 82, 27);\n"
"}")
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 30, 611, 521))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"")
        self.residentTableWidget = QTableWidget(self.groupBox_4)
        if (self.residentTableWidget.columnCount() < 12):
            self.residentTableWidget.setColumnCount(12)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setBackground(QColor(254, 254, 254));
        self.residentTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(254, 254, 254));
        self.residentTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.residentTableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem15)
        self.residentTableWidget.setObjectName(u"residentTableWidget")
        self.residentTableWidget.setGeometry(QRect(20, 50, 591, 491))
        self.residentTableWidget.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0);\n"
"")
        self.lineEdit_search = QLineEdit(self.groupBox_4)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(750, 560, 411, 41))
        self.lineEdit_search.setStyleSheet(u"background-color: rgb(224, 251, 252);\n"
"color: rgb(8, 60, 104);")
        self.btn_search = QPushButton(self.groupBox_4)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(660, 560, 81, 41))
        self.btn_search.setFont(font5)
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setAutoFillBackground(False)
        self.btn_search.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(17, 133, 09);\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 82, 27);\n"
"}")
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(660, 30, 511, 521))
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(61, 90, 128);\n"
"\n"
"")
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(680, 60, 81, 41))
        self.label_16.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(670, 50, 491, 491))
        self.label_17.setStyleSheet(u"Background-color:rgb(152, 193, 217);")
        self.line = QFrame(self.groupBox_4)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(680, 120, 201, 16))
        self.line.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(680, 140, 81, 41))
        self.label_18.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_2 = QFrame(self.groupBox_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(680, 200, 201, 16))
        self.line_2.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.groupBox_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(910, 120, 231, 16))
        self.line_3.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(910, 60, 81, 41))
        self.label_21.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(910, 140, 81, 41))
        self.label_23.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_4 = QFrame(self.groupBox_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(910, 200, 231, 16))
        self.line_4.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(680, 220, 81, 41))
        self.label_25.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_5 = QFrame(self.groupBox_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(680, 280, 201, 16))
        self.line_5.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(910, 220, 81, 41))
        self.label_27.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_6 = QFrame(self.groupBox_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(910, 280, 231, 16))
        self.line_6.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(680, 300, 81, 41))
        self.label_29.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_7 = QFrame(self.groupBox_4)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(680, 360, 201, 16))
        self.line_7.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(910, 300, 81, 41))
        self.label_31.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_8 = QFrame(self.groupBox_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(910, 360, 231, 16))
        self.line_8.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(680, 380, 111, 41))
        self.label_33.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_9 = QFrame(self.groupBox_4)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(680, 440, 201, 16))
        self.line_9.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.label_res = QLabel(self.groupBox_4)
        self.label_res.setObjectName(u"label_res")
        self.label_res.setGeometry(QRect(910, 380, 111, 41))
        self.label_res.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(152, 193, 217);\n"
"color: rgb(0,0,0)\n"
"\n"
"")
        self.line_10 = QFrame(self.groupBox_4)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(910, 440, 231, 16))
        self.line_10.setStyleSheet(u"background-color: rgb(152, 193, 217);")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.ln_fullName = QLineEdit(self.groupBox_4)
        self.ln_fullName.setObjectName(u"ln_fullName")
        self.ln_fullName.setGeometry(QRect(680, 100, 201, 21))
        self.ln_fullName.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_fullAddress = QLineEdit(self.groupBox_4)
        self.ln_fullAddress.setObjectName(u"ln_fullAddress")
        self.ln_fullAddress.setGeometry(QRect(910, 100, 231, 21))
        self.ln_fullAddress.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_gender = QLineEdit(self.groupBox_4)
        self.ln_gender.setObjectName(u"ln_gender")
        self.ln_gender.setGeometry(QRect(680, 180, 201, 21))
        self.ln_gender.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_civilStatus = QLineEdit(self.groupBox_4)
        self.ln_civilStatus.setObjectName(u"ln_civilStatus")
        self.ln_civilStatus.setGeometry(QRect(910, 180, 201, 21))
        self.ln_civilStatus.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_birthPlace = QLineEdit(self.groupBox_4)
        self.ln_birthPlace.setObjectName(u"ln_birthPlace")
        self.ln_birthPlace.setGeometry(QRect(680, 260, 201, 21))
        self.ln_birthPlace.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_birthDate = QLineEdit(self.groupBox_4)
        self.ln_birthDate.setObjectName(u"ln_birthDate")
        self.ln_birthDate.setGeometry(QRect(910, 260, 201, 21))
        self.ln_birthDate.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_voterStatus = QLineEdit(self.groupBox_4)
        self.ln_voterStatus.setObjectName(u"ln_voterStatus")
        self.ln_voterStatus.setGeometry(QRect(680, 340, 201, 21))
        self.ln_voterStatus.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_citizenship = QLineEdit(self.groupBox_4)
        self.ln_citizenship.setObjectName(u"ln_citizenship")
        self.ln_citizenship.setGeometry(QRect(910, 340, 201, 21))
        self.ln_citizenship.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_contactNumber = QLineEdit(self.groupBox_4)
        self.ln_contactNumber.setObjectName(u"ln_contactNumber")
        self.ln_contactNumber.setGeometry(QRect(680, 420, 201, 21))
        self.ln_contactNumber.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.ln_residency = QLineEdit(self.groupBox_4)
        self.ln_residency.setObjectName(u"ln_residency")
        self.ln_residency.setGeometry(QRect(910, 420, 201, 21))
        self.ln_residency.setStyleSheet(u"Background-color:rgb(152, 193, 217);\n"
"color:rgb(0,0,0,);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-color: rgb(152, 193, 217);")
        self.btn_insertResident.raise_()
        self.btn_removeResident.raise_()
        self.label_14.raise_()
        self.residentTableWidget.raise_()
        self.lineEdit_search.raise_()
        self.btn_search.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        self.line.raise_()
        self.label_18.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.line_4.raise_()
        self.label_25.raise_()
        self.line_5.raise_()
        self.label_27.raise_()
        self.line_6.raise_()
        self.label_29.raise_()
        self.line_7.raise_()
        self.label_31.raise_()
        self.line_8.raise_()
        self.label_33.raise_()
        self.line_9.raise_()
        self.label_res.raise_()
        self.line_10.raise_()
        self.ln_fullName.raise_()
        self.ln_fullAddress.raise_()
        self.ln_gender.raise_()
        self.ln_civilStatus.raise_()
        self.ln_birthPlace.raise_()
        self.ln_birthDate.raise_()
        self.ln_voterStatus.raise_()
        self.ln_citizenship.raise_()
        self.ln_contactNumber.raise_()
        self.ln_residency.raise_()
        self.btn_saveResident.raise_()
        self.stackedWidget.addWidget(self.pg_residents)
        self.pg_officials = QWidget()
        self.pg_officials.setObjectName(u"pg_officials")
        self.verticalLayout_8 = QVBoxLayout(self.pg_officials)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.pg_officials)
        self.label.setObjectName(u"label")
        font8 = QFont()
        font8.setPointSize(40)
        self.label.setFont(font8)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.pg_officials)
        self.pg_forms = QWidget()
        self.pg_forms.setObjectName(u"pg_forms")
        self.label_3 = QLabel(self.pg_forms)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, -20, 1061, 561))
        self.label_3.setStyleSheet(u"color: #FFF;")
        self.stackedWidget.addWidget(self.pg_forms)
        self.pg_settings = QWidget()
        self.pg_settings.setObjectName(u"pg_settings")
        self.stackedWidget.addWidget(self.pg_settings)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Welcome to Barangay System v2", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"🖥️", None))
        self.btn_residents.setText(QCoreApplication.translate("MainWindow", u"👪", None))
        self.btn_officials.setText(QCoreApplication.translate("MainWindow", u"🗃️", None))
        self.btn_forms.setText(QCoreApplication.translate("MainWindow", u"📃", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"⚙", None))
        self.filler.setText("")
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\ue036", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#aaffff;\">Barangay Population</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#aaffff;\">Registered Voters</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#aaffff;\">Male</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#aaffff;\">Female</span></p></body></html>", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Residents Record Summary", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Current Elected Barangay Officials", None))
        self.btn_insertOfficial.setText(QCoreApplication.translate("MainWindow", u"Insert Official", None))
        self.btn_removeOfficial.setText(QCoreApplication.translate("MainWindow", u"Remove Official", None))
        self.btn_editOfficial.setText(QCoreApplication.translate("MainWindow", u"Edit Official", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Barangay Gumaok East Barangay System", None))
        self.label_13.setText("")
        self.dash_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.brgy_population.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#aaffff;\">0</span></p></body></html>", None))
        self.brgy_male.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#aaffff;\">0</span></p></body></html>", None))
        self.brgy_voters.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#aaffff;\">0</span></p></body></html>", None))
        self.brgy_female.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#aaffff;\">0</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Residents Profile", None))
        self.btn_insertResident.setText(QCoreApplication.translate("MainWindow", u"New Resident", None))
        self.btn_removeResident.setText(QCoreApplication.translate("MainWindow", u"Remove Resident", None))
        self.btn_saveResident.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        ___qtablewidgetitem4 = self.residentTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem5 = self.residentTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem6 = self.residentTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None));
        ___qtablewidgetitem7 = self.residentTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem8 = self.residentTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Birth Date", None));
        ___qtablewidgetitem9 = self.residentTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Full Address", None));
        ___qtablewidgetitem10 = self.residentTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Voter Status", None));
        ___qtablewidgetitem11 = self.residentTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None));
        ___qtablewidgetitem12 = self.residentTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Birth Place", None));
        ___qtablewidgetitem13 = self.residentTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None));
        ___qtablewidgetitem14 = self.residentTableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None));
        ___qtablewidgetitem15 = self.residentTableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Residency", None));
#if QT_CONFIG(tooltip)
        self.lineEdit_search.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Type here to search</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_search.setInputMask("")
        self.lineEdit_search.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Type Here to search...", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Full Name</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Gender</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Full Address</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Civil Status</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Birth Place</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Birth Date</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Voter Status</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Citizenship</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Contact Number</span></p></body></html>", None))
        self.label_res.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Residency Years</span></p></body></html>", None))
        self.ln_fullName.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.ln_fullAddress.setText(QCoreApplication.translate("MainWindow", u"Full Address", None))
        self.ln_gender.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.ln_civilStatus.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.ln_birthPlace.setText(QCoreApplication.translate("MainWindow", u"Birth Place", None))
        self.ln_birthDate.setText(QCoreApplication.translate("MainWindow", u"Birth Date", None))
        self.ln_voterStatus.setText(QCoreApplication.translate("MainWindow", u"Voter status", None))
        self.ln_citizenship.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.ln_contactNumber.setText(QCoreApplication.translate("MainWindow", u"Contact Number", None))
        self.ln_residency.setText(QCoreApplication.translate("MainWindow", u"Year of residency", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SETTINGS PAGE", None))
    # retranslateUi

