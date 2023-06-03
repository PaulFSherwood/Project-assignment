# Name: Paul Sherwood
# Course: CYBR-260-40
# Section: Week 7 - Final Programming Assignment
# Date: February 23, 2023
# Description: This program will provide a GUI interface to several IT security tools.

# QT libraries used for the GUI and connecting signals and slots
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QAction, QTransform
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QSystemTrayIcon

# Libraries for low level system calls, shell commands
#  - grab system information, and to complete network 
#  - calls and commands, HTTP requests
from datetime import datetime
import platform, sys, paramiko, ctypes
from scp import SCPClient
import subprocess, socket, requests, os

# Libraries for network mapping and scanning
import nmap, sys
import netifaces as ni
import networkx as nx

# Libraries to show graphical charts
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

# Gives access to icons
import qtawesome

# Libraries for XML file creation and addition
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ElementTree
import xml.dom.minidom

# Setup to test for operating system version
os_name = platform.system()
os_version = platform.version()


# Class: Ui_Form
# Purpose: Class provides the intial UI and all usable funcitons to support it.  
# Inputs: object, Form also gets passed into it
# Returns: Displays UI and runs functions
class Ui_Form(object):

    # Function: setupUi
    # Purpose: Function to setup the intial UI.  
    # Inputs: self, Form
    # Returns: Inital placement of GUI will be applied.
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 312)
        Form.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 312))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet("/*** MAIN SECTION ***/\n"
                                    "QWidget {\n"
                                    "    background-color: #404258;\n"
                                    "    color: #fff;\n"
                                    " }\n"
                                    "QTabWidget {\n"
                                    "    background: #404258;\n"
                                    "    border-color: #BFE7FF;\n"
                                    "}\n"

                                    "/*** PUSH BUTTON SECTION ***/\n"
                                    " QPushButton {\n"
                                    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #404258, stop: 1 #6B728E);\n"
                                    "    border-radius: 6px;\n"
                                    "    padding: 5px;\n"
                                    "    color: white;\n"
                                    "    font-weight: bold;\n"
                                    "}\n"
                                    "QPushButton:hover {;\n"
                                    "    border: 1px solid;\n"
                                    "    border-color: #fff;\n"
                                    " }\n"
                                    "QPushButton:pressed {\n"
                                    "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6B728E, stop: 1 #404258);\n"
                                    "}\n"

                                    "/*** TAB BAR SECTION ***/\n"
                                    "QTabBar:tab { \n"
                                    "    background: #474E68;\n"
                                    "    color: #fff; padding: 10px; \n"
                                    "    min-width: 5px; width: 15px; min-height: 5px; max-height: 15px; \n"
                                    "}\n"
                                    "QTabBar:tab:hover {\n"
                                    "    background: #50577A;\n"
                                    "}\n"
                                    "QTabBar:tab:selected { \n"
                                    "    background: #6B728E; \n"
                                    "}\n"

                                    "/*** LINE EDIT SECTION ***/\n"
                                    "QLineEdit {\n"
                                    "    border: 1px solid;\n"
                                    "    border-color: #50577A;\n"
                                    "    background-color: #6B728E;\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "    background: #7B8FA1;\n"
                                    "    border: 2px solid;\n"
                                    "    border-color: #50577A;\n"
                                    "}\n"

                                    "/*** TEXT EDIT SECTION ***/\n"
                                    "QTextEdit {\n"
                                    "    border: 1px solid;\n"
                                    "    border-color: #50577A;\n"
                                    "    background-color: #6B728E;\n"
                                    "}\n"
                                    "QTextEdit:focus {\n"
                                    "    background: #7B8FA1;\n"
                                    "    border: 2px solid;\n"
                                    "    border-color: #50577A;\n"
                                    "}\n"

                                    "/** TEXT BROWSER SECTION **/\n"
                                    "QTextBrowser {\n"
                                    "    border: 2px solid;\n"
                                    "    border-color: #50577A;\n"
                                    "    background: #6B728E;\n"
                                    "}")

        # Setup variables for the main icons and the xml log file
        icon_color = '#8e876b'
        icon_color2 = '#8e6b72'
        self.my_file = 'log.xml'

        ##################################################
        # The following creates the main window, fields and buttons
        ##################################################
        # Start - Tab 1 (Dashboard)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(124, 40, 91, 24))
        self.pushButton.setObjectName("pushButton")

        self.t1_title = QtWidgets.QLabel(self.tab)
        self.t1_title.setGeometry(QtCore.QRect(130, 10, 81, 21))
        self.t1_title.setObjectName("t1_title")

        self.Computer_label = QtWidgets.QLabel(self.tab)
        self.Computer_label.setGeometry(QtCore.QRect(40, 90, 41, 41))
        self.Computer_label.setText("")
        self.Computer_label.setPixmap(QtGui.QPixmap("images/Computer.png"))
        self.Computer_label.setScaledContents(True)
        self.Computer_label.setObjectName("Computer_label")

        self.Gateway_Label = QtWidgets.QLabel(self.tab)
        self.Gateway_Label.setGeometry(QtCore.QRect(160, 90, 41, 41))
        self.Gateway_Label.setText("")
        self.Gateway_Label.setPixmap(QtGui.QPixmap("images/Gateway.png"))
        self.Gateway_Label.setScaledContents(True)
        self.Gateway_Label.setObjectName("Gateway_Label")

        self.Internet_Label = QtWidgets.QLabel(self.tab)
        self.Internet_Label.setGeometry(QtCore.QRect(280, 90, 41, 41))
        self.Internet_Label.setText("")
        self.Internet_Label.setPixmap(QtGui.QPixmap("images/Internet.png"))
        self.Internet_Label.setScaledContents(True)
        self.Internet_Label.setObjectName("Internet_Label")

        self.Computer_Name_Label = QtWidgets.QLabel(self.tab)
        self.Computer_Name_Label.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.Computer_Name_Label.setObjectName("Computer_Name_Label")

        self.Gateway_Name_Label = QtWidgets.QLabel(self.tab)
        self.Gateway_Name_Label.setGeometry(QtCore.QRect(130, 70, 101, 20))
        self.Gateway_Name_Label.setObjectName("Gateway_Name_Label")

        self.Internet_Name_Label = QtWidgets.QLabel(self.tab)
        self.Internet_Name_Label.setGeometry(QtCore.QRect(280, 70, 61, 16))
        self.Internet_Name_Label.setObjectName("Internet_Name_Label")

        self.IP_TextEdit = QtWidgets.QTextEdit(self.tab)
        self.IP_TextEdit.setGeometry(QtCore.QRect(10, 140, 101, 41))
        self.IP_TextEdit.setObjectName("IP_TextEdit")

        self.Gateway_LineEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.Gateway_LineEdit_2.setGeometry(QtCore.QRect(130, 140, 101, 41))
        self.Gateway_LineEdit_2.setObjectName("Gateway_LineEdit_2")

        self.Internet_LineEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.Internet_LineEdit_3.setGeometry(QtCore.QRect(250, 140, 101, 41))
        self.Internet_LineEdit_3.setObjectName("Internet_LineEdit_3")

        # Create an icon `qta-browser`
        icon1 = self.get_awesome_icon_states("mdi.speedometer", icon_color, 90)
        self.tabWidget.addTab(self.tab, icon1, "")

        # End - Tab 1 (Dashboard)
        ##################################################

        ##################################################
        # Start - TAB 2 (Network Details)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(110, 10, 131, 21))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_11.setObjectName("label_11")

        self.Network_Details_Result = QtWidgets.QTextBrowser(self.tab_2)
        self.Network_Details_Result.setGeometry(QtCore.QRect(10,100, 341, 201))
        # self.Network_Details_Result.setGeometry(QtCore.QRect(10, 100, 341, 201))
                                                            #10,100, 341, 201 Original
                                                            #10, 100, 161, 201
        self.Network_Details_Result.setObjectName("Network_Details_Result")

        self.Get_Network_Details = QtWidgets.QPushButton(self.tab_2)
        self.Get_Network_Details.setGeometry(QtCore.QRect(250, 60, 101, 24))
        self.Get_Network_Details.setObjectName("Get_Network_Details")

        self.Redo = QtWidgets.QLabel(self.tab_2)
        self.Redo.setGeometry(QtCore.QRect(220, 60, 21, 21))
        self.Redo.setText("")
        self.Redo.setPixmap(QtGui.QPixmap("images/Redo.png"))
        self.Redo.setScaledContents(True)
        self.Redo.setObjectName("Redo")

        # Create an icon `qta-browser`
        icon2 = self.get_awesome_icon_states("mdi.ethernet", icon_color2, 90)
        self.tabWidget.addTab(self.tab_2, icon2, "")

        # End - Tab 2 (Network Details)
        ##################################################

        ##################################################
        # Start - Tab 3 (Network Scanning)
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.network_scan_btn = QtWidgets.QPushButton(self.tab_3)
        self.network_scan_btn.setGeometry(QtCore.QRect(260, 60, 95, 24))
        self.network_scan_btn.setObjectName("network_scan_btn")

        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 111, 31))
        self.label_2.setObjectName("label_2")
        self.network_lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.network_lineEdit.setGeometry(QtCore.QRect(10, 60, 221, 22))
        self.network_lineEdit.setObjectName("lineEdit")
        self.Network_Scan_Result = QtWidgets.QTextBrowser(self.tab_3)
        self.Network_Scan_Result.setGeometry(QtCore.QRect(10, 100, 341, 192))
        self.Network_Scan_Result.setObjectName("Network_Scan_Result")
        self.Network_Scan_Result.setText("Please be patient this will take some time to complete.")

        # Create an icon `qta-browser`
        icon3 = self.get_awesome_icon_states("fa5s.network-wired", icon_color, 90)
        self.tabWidget.addTab(self.tab_3,  icon3, "")

        # End - Tab 3 (Network Scanning)
        ##################################################

        ##################################################
        # Start - Tab 4 (Port Scanning)
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.host_lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.host_lineEdit_2.setGeometry(QtCore.QRect(50, 40, 211, 22))
        self.host_lineEdit_2.setObjectName("host_lineEdit_2")

        self.port_lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.port_lineEdit_3.setGeometry(QtCore.QRect(50, 70, 101, 22))
        self.port_lineEdit_3.setObjectName("port_lineEdit_3")

        self.port_lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.port_lineEdit_4.setGeometry(QtCore.QRect(160, 70, 101, 22))
        self.port_lineEdit_4.setObjectName("port_lineEdit_4")

        self.port_scan_btn = QtWidgets.QPushButton(self.tab_4)
        self.port_scan_btn.setGeometry(QtCore.QRect(280, 70, 75, 24))
        self.port_scan_btn.setObjectName("port_scan_btn")

        self.Port_Scan_Result = QtWidgets.QTextBrowser(self.tab_4)
        self.Port_Scan_Result.setGeometry(QtCore.QRect(10, 100, 341, 201))
        self.Port_Scan_Result.setObjectName("Port_Scan_Result")

        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(130, 11, 71, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(11, 39, 25, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(11, 68, 35, 16))
        self.label_5.setObjectName("label_5")

        # Create an icon `qta-browser`
        icon4 = self.get_awesome_icon_states("mdi6.plus-network-outline", icon_color2, 90)
        self.tabWidget.addTab(self.tab_4, icon4, "")

        # End - Tab 4 (Port Scanning)
        ##################################################

        ##################################################
        # Start - Tab 5 (Ping Destinatior)
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.Ping_Status_Result = QtWidgets.QTextBrowser(self.tab_5)
        self.Ping_Status_Result.setGeometry(QtCore.QRect(10, 110, 341, 192))
        self.Ping_Status_Result.setObjectName("Ping_Status_Result")

        self.port_lineEdit_5 = QtWidgets.QLineEdit(self.tab_5)
        self.port_lineEdit_5.setGeometry(QtCore.QRect(81, 43, 181, 20))
        self.port_lineEdit_5.setObjectName("port_lineEdit_5")

        self.ip_scan_btn_5 = QtWidgets.QPushButton(self.tab_5)
        self.ip_scan_btn_5.setGeometry(QtCore.QRect(279, 40, 71, 26))
        self.ip_scan_btn_5.setObjectName("ip_scan_btn_5")

        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(109, 10, 131, 21))
        self.label_8.setObjectName("label_8")

        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(11, 37, 25, 16))
        self.label_6.setObjectName("label_6")
        
        # Create an icon `qta-browser`
        icon5 = self.get_awesome_icon_states("mdi6.ear-hearing", icon_color, 90)
        self.tabWidget.addTab(self.tab_5, icon5, "")
        # Start - Tab 5 (Ping Destinatior)
        ##################################################

        ##################################################
        # Start - Tab 6 (Network Map)
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")

        self.t6_title = QtWidgets.QLabel(self.tab_6)
        self.t6_title.setGeometry(QtCore.QRect(125, 7, 120, 21))
        self.t6_title.setObjectName("t6_title")

        self.get_ip_6 = QtWidgets.QLineEdit(self.tab_6)
        self.get_ip_6.setGeometry(QtCore.QRect(30, 40, 181, 26))
        self.get_ip_6.setObjectName("get_ip_6")

        self.get_map_6 = QtWidgets.QPushButton(self.tab_6)
        self.get_map_6.setGeometry(QtCore.QRect(250, 40, 91, 26))
        self.get_map_6.setObjectName("get_map_6")

        # Get the current figure
        self.figure = plt.gcf()

        # Create an icon `qta-browser`
        icon6 = self.get_awesome_icon_states("fa5s.map-marked", icon_color2, 90)
        self.tabWidget.addTab(self.tab_6, icon6,  "")
        # Start - Tab 6 (Network Map)
        ##################################################

        ##################################################
        # Start - Tab 7 (Security Log)
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")

        self.t7_title = QtWidgets.QLabel(self.tab_7)
        self.t7_title.setGeometry(QtCore.QRect(75, 2, 221, 25))
        self.t7_title.setObjectName("t7_title")

        self.HostName_Label = QtWidgets.QLabel(self.tab_7)
        self.HostName_Label.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.HostName_Label.setObjectName("HostName_Label")

        self.HostName_LineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.HostName_LineEdit.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.HostName_LineEdit.setObjectName("HostName_LineEdit")

        self.UserName_Label = QtWidgets.QLabel(self.tab_7)
        self.UserName_Label.setGeometry(QtCore.QRect(120, 30, 91, 17))
        self.UserName_Label.setObjectName("UserName_Label")

        self.UserName_LineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.UserName_LineEdit.setGeometry(QtCore.QRect(120, 50, 91, 21))
        self.UserName_LineEdit.setObjectName("UserName_LineEdit")

        self.Return_Label = QtWidgets.QLabel(self.tab_7)
        self.Return_Label.setGeometry(QtCore.QRect(230, 30, 51, 17))
        self.Return_Label.setObjectName("Return_Label")

        self.Return_LineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.Return_LineEdit.setGeometry(QtCore.QRect(230, 50, 51, 21))
        self.Return_LineEdit.setObjectName("Return_LineEdit")

        self.ID_Label = QtWidgets.QLabel(self.tab_7)
        self.ID_Label.setGeometry(QtCore.QRect(300, 30, 51, 17))
        self.ID_Label.setObjectName("ID_Label")

        self.ID_LineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.ID_LineEdit.setGeometry(QtCore.QRect(300, 50, 51, 21))
        self.ID_LineEdit.setObjectName("ID_LineEdit")

        # If you are using Linux disable that field
        # using linux change the tag
        if os_name == 'Linux':
            self.ID_Label.setStyleSheet("QLabel { text-decoration: line-through; }")
            self.ID_LineEdit.setEnabled(False)

        ## adding a password field that I will hide later.
        self.Password_Label = QtWidgets.QLabel(self.tab_7)
        self.Password_Label.setGeometry(QtCore.QRect(80, 91, 71, 20))
        self.Password_Label.setObjectName("PassWord_Label")

        self.PassWord_LineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.PassWord_LineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.PassWord_LineEdit.setGeometry(QtCore.QRect(170, 90, 113, 25))
        self.PassWord_LineEdit.setObjectName("PassWord_LineEdit")

        self.showSecurityLog_TextBrowser = QtWidgets.QTextBrowser(self.tab_7)
        self.showSecurityLog_TextBrowser.setGeometry(QtCore.QRect(10, 131, 341, 141))#10, 80, 341, 192))
        self.showSecurityLog_TextBrowser.setObjectName("showSecurityLog_TextBrowser")

        self.getSecurityLog_Button = QtWidgets.QPushButton(self.tab_7)
        self.getSecurityLog_Button.setGeometry(QtCore.QRect(260, 280, 81, 25))
        self.getSecurityLog_Button.setObjectName("getSecurityLog_Button")

        self.resetSecurityLog_Button = QtWidgets.QPushButton(self.tab_7)
        self.resetSecurityLog_Button.setGeometry(QtCore.QRect(10, 280, 81, 25))
        self.resetSecurityLog_Button.setObjectName("resetSecurityLog_Button")

        # Create an icon `qta-browser`
        icon7 = self.get_awesome_icon_states("mdi6.server-security", icon_color, 90)
        self.tabWidget.addTab(self.tab_7, icon7, "")
        
        # Start - Tab 7 (Security Log)
        ##################################################

        ##################################################
        # Start - Tab 8 (Backup over network)
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")

        self.t8_title = QtWidgets.QLabel(self.tab_8)
        self.t8_title.setGeometry(QtCore.QRect(75, 2, 221, 25))
        self.t8_title.setObjectName("t8_title")

        self.HostName_Label2 = QtWidgets.QLabel(self.tab_8)
        self.HostName_Label2.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.HostName_Label2.setObjectName("HostName_Label2")

        self.HostName_LineEdit2 = QtWidgets.QLineEdit(self.tab_8)
        self.HostName_LineEdit2.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.HostName_LineEdit2.setObjectName("HostName_LineEdit2")

        self.UserName_Label2 = QtWidgets.QLabel(self.tab_8)
        self.UserName_Label2.setGeometry(QtCore.QRect(120, 30, 91, 17))
        self.UserName_Label2.setObjectName("UserName_Label2")

        self.UserName_LineEdit2 = QtWidgets.QLineEdit(self.tab_8)
        self.UserName_LineEdit2.setGeometry(QtCore.QRect(120, 50, 91, 21))
        self.UserName_LineEdit2.setObjectName("UserName_LineEdit2")

        ## adding a password field that I will hide later.
        self.Password_Label2 = QtWidgets.QLabel(self.tab_8)
        self.Password_Label2.setGeometry(QtCore.QRect(230, 30, 55, 17))
        self.Password_Label2.setObjectName("PassWord_Label2")

        self.PassWord_LineEdit2 = QtWidgets.QLineEdit(self.tab_8)
        self.PassWord_LineEdit2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.PassWord_LineEdit2.setGeometry(QtCore.QRect(230, 50, 101, 21))
        self.PassWord_LineEdit2.setObjectName("PassWord_LineEdit2")

        self.showRetrievedFiles_TextBrowser = QtWidgets.QTextBrowser(self.tab_8)
        self.showRetrievedFiles_TextBrowser.setGeometry(QtCore.QRect(10, 131, 341, 141))#10, 80, 341, 192))
        self.showRetrievedFiles_TextBrowser.setObjectName("showRetrievedFiles_TextBrowser")

        self.getNetworkFiles_Button2 = QtWidgets.QPushButton(self.tab_8)
        self.getNetworkFiles_Button2.setGeometry(QtCore.QRect(260, 280, 81, 25))
        self.getNetworkFiles_Button2.setObjectName("getSecurityLog_Button")

        # Create an icon `qta-browser`
        icon8 = self.get_awesome_icon_states("mdi6.database-arrow-down", icon_color2, 90)
        self.tabWidget.addTab(self.tab_8, icon8, "")
        
        # Start - Tab 8 (Backup over network)
        ##################################################

        ### Button Connections to methods
        self.pushButton.clicked.connect(self.update_dasboard)                   # Tab 1
        self.Get_Network_Details.clicked.connect(self.update_field)             # Tab 2
        self.network_scan_btn.clicked.connect(self.update_network_scan)         # Tab 3
        self.port_scan_btn.clicked.connect(self.update_port_scan)               # Tab 4
        self.ip_scan_btn_5.clicked.connect(self.ping_destination)               # Tab 5
        self.get_map_6.clicked.connect(self.get_network_picture)                # Tab 6
        self.getSecurityLog_Button.clicked.connect(self.get_security_log)       # Tab 7
        self.resetSecurityLog_Button.clicked.connect(self.reset_security_log)   # Tab 7
        self.getNetworkFiles_Button2.clicked.connect(self.get_network_files)    # Tab 8

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)  # Show the first tab when the program starts.
        QtCore.QMetaObject.connectSlotsByName(Form)

    # Function: get_awesome_icon_states
    # Purpose: Function changes and returns an icon with the correct color and rotation.
    # Inputs: self, qtawesome icon name, icon color, new icon angle
    # Returns: Returns an icon, with the correct color and rotation.
    def get_awesome_icon_states(self, icon_name, color, angle):
        icon = qtawesome.icon(icon_name, color=color)
        transform = QTransform().rotate(angle)
        size = icon.actualSize(QtCore.QSize(32, 32))
        pixmap = icon.pixmap(size, QIcon.Mode.Normal, QIcon.State.On).transformed(transform)
        return QIcon(pixmap)

    # Function: retranslateUi
    # Purpose: Function to update the look and text for each button, text field, and labels.
    # Inputs: self, Form
    # Returns: GUI will look different
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowTitle('CYBR-260-40 Final Project')
        Form.setWindowIcon(QIcon("images/me.png"))

        # Icon fix so it displays correctly on Windows 10 systems.
        if os_name == 'Windows':
            # Taskbar Icon fix from: https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
            myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # Extra styling for labels, buttons, and tabs
        self.pushButton.setText(_translate("Form", "Get Local IP\'s"))
        self.t1_title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Dashboard</span></p></body></html>"))
        self.Computer_Name_Label.setText(_translate("Form", "Computer"))
        self.Gateway_Name_Label.setText(_translate("Form", "Gateway / Router"))
        self.Internet_Name_Label.setText(_translate("Form", "Internet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", ""))

        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Network Details</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "Details"))
        self.Get_Network_Details.setText(_translate("Form", "Get Local Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", ""))

        self.network_scan_btn.setText(_translate("Form", "Scan Network"))
        self.label.setText(_translate("Form", "IP Range"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Network Scan</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", ""))

        self.port_scan_btn.setText(_translate("Form", "Scan Ports"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Port Scan</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "Host"))
        self.label_5.setText(_translate("Form", "Port(s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", ""))

        self.ip_scan_btn_5.setText(_translate("Form", " Ping IP "))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Ping Destination</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "Host"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", ""))

        self.get_map_6.setText(_translate("Form", "Get Map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", ""))
        self.t6_title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Network Map</span></p></body></html>"))
        
        self.HostName_Label.setText(_translate("Form", "HostName (IP)"))
        self.UserName_Label.setText(_translate("Form", "User Name"))
        self.Return_Label.setText(_translate("Form", "Line Qty"))
        self.ID_Label.setText(_translate("Form", "ID #"))
        self.getSecurityLog_Button.setText(_translate("Form", "Search"))
        self.resetSecurityLog_Button.setText(_translate("Form", "Reset"))
        self.Password_Label.setText(_translate("Form", "Password: "))
        self.t7_title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Show Logon Events</span></p></body></html>"))

        self.HostName_Label2.setText(_translate("Form", "HostName (IP)"))
        self.UserName_Label2.setText(_translate("Form", "User Name"))
        self.getNetworkFiles_Button2.setText(_translate("Form", "Search"))
        self.Password_Label2.setText(_translate("Form", "Password: "))
        self.t8_title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Backup Remote files</span></p></body></html>"))

    ##################################################
    # Start - Get the current time

    # Function: get_current_time
    # Purpose: Returns the time in a usable format
    # Inputs: self
    # Returns: returns the time in a specific format.
    def get_current_time(self):
        return datetime.now().strftime('%H:%M:%S')  # system only likes this format.
    # Stop - Get the current time
    ##################################################

    ##################################################
    # Start - Logging with XML
    
    # Function: add_to_xml_file
    # Purpose: Creates and / or adds to an XML file that is used for logging
    # Inputs: self, file name, data to be added
    # Returns: None, but adds new data from the called function to the XML file
    def add_to_xml_file(self, filename, data):
        # Load the XML file if it exists, or create a new one if it doesn't
        try:
            # parse the file into element tree and get the root element
            root = ElementTree.parse(filename).getroot()
        except (FileNotFoundError, ElementTree.ParseError):
            # the file doesn't exists, create a root node
            root = Element('computers')
            
        # Create a new computer element for the data
        computer_elem = Element('computer') # parent element
        root.append(computer_elem)  # appends the parent to the root
        
        # Add the data to the computer element
        for key, value in data.items():
            if isinstance(value, list):
                # If the value is a list, create a new element for each item in the list
                for item in value:
                    item_elem = Element(key)
                    computer_elem.append(item_elem)
                    for subkey, subvalue in item.items():
                        sub_elem = Element(subkey)
                        sub_elem.text = str(subvalue)
                        item_elem.append(sub_elem)
            else:
                # Otherwise, create a single element for the key/value pair
                elem = Element(key)
                elem.text = str(value)
                computer_elem.append(elem)

        # Write the updated XML to the file
        with open(filename, 'w') as f:
            xml_str = tostring(root, encoding='unicode')
            xml_str = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="    ")
            xml_str = self.clean_up_xml_output_data(xml_str)
            # print(f"{xml_str}")
            f.write(xml_str)

    # Function: clean_up_xml_output_data
    # Purpose: Removes all empty lines
    # Inputs: self, current XML file (all lines)
    # Returns: returns an XML file with all empty lines '\n' removed
    def clean_up_xml_output_data(self, xml_str):
        # Strip out any empty new lines, return the new xml_str
        lines = xml_str.splitlines()
        xml_str = ''
        # if the line is empty or only contains whitespace, skip it
        for line in lines:
            if line.strip() == '' or line.strip() == '\n':
                continue
            else:
                xml_str += line + '\n'
        return xml_str
    # Stop - Logging with XML
    ##################################################

    ##################################################
    # Start - Tab 1 - FUNCTION (update_dasboard)

    # Function: update_dasboard
    # Purpose: Function to display IP addresses
    # Inputs: self
    # Returns: send internal, external and gateway to text fields
    def update_dasboard(self):
        try:
            # os_name
            # os_version
            if os_name == 'Windows':
                # ip_addr = socket.gethostbyname_ex(socket.getfqdn())[2][1]
                ip_addr = socket.gethostbyname(socket.gethostname())
                gateway = ni.gateways()['default'][ni.AF_INET][0]#[2][0][0]
                ip_external = requests.get("https://api.ipify.org").text
            elif os_name == 'Linux':
                ip_addr = subprocess.check_output("ip addr show | grep 'inet ' | awk '{print $2}' | cut -d/ -f1", shell=True).decode()
                gateway = subprocess.check_output("ip addr show | grep 'inet ' | awk '{print $4}' | cut -d/ -f1", shell=True).decode()

                # on systems that don't have internet access this will crash without a try / except
                try:
                    ip_external = requests.get("https://api.ipify.org").text
                except:
                    ip_external = 'Unreachable'
            else:
                ip_addr = ''
                gateway = ''
                ip_external = ''

            self.IP_TextEdit.setText(str(ip_addr))
            self.Gateway_LineEdit_2.setText(str(gateway))
            self.Internet_LineEdit_3.setText(ip_external)

            # Update log file
            data = {
                'Name': 'Dashboard',
                'IP': str(ip_addr),
                'gateway': str(gateway),
                'IP_External': str(ip_external),
                'Time': self.get_current_time()
            }
            self.add_to_xml_file(self.my_file, data)

        except (socket.gaierror, requests.exceptions.RequestException, subprocess.CalledProcessError) as e:
            # grab all other errors
            self.IP_TextEdit.setText('')
            self.Gateway_LineEdit_2.setText('')
            self.Internet_LineEdit_3.setText('Unreachable')

    # Start - Tab 1 - FUNCTION (update_dasboard)
    ##################################################

    ##################################################
    # Start - Tab 2 - FUNCTION (update_field)

    # Function: update_field
    # Purpose: Function to display network card configurations
    # Inputs: self
    # Returns: send network details to text fields
    def update_field(self):
        try:
            # Update the greetings field
            # Grab the name filed and update label
            if os_name == 'Windows':
                # Get windows IP
                data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')
            elif os_name == 'Linux':
                # Get Linux IP
                data = subprocess.check_output(['ip', 'route', 'show']).decode().split('\n')
            else:
                data = ''
            return_data = ''
            for item in data:
                # Update the network details
                self.Network_Details_Result.append(item[:58])
                return_data = return_data + item[:58] + '\n'
            
            # Update log file
            data = {
                'Name': 'Network Config',
                'IP': item[:58],
                'Time': self.get_current_time()
            }
            self.add_to_xml_file(self.my_file, data)

        except subprocess.CalledProcessError as e:
            # grab all other errors
            self.Network_Details_Result.setText(f"Error {e}")

    # Start - Tab 2 - FUNCTION (update_field)
    ##################################################

    ##################################################
    # Start - Tab 3 - FUNCTION (update_network_scan)

    # Function: update_network_scan
    # Purpose: Function to trace network to IP address
    # Inputs: self
    # Returns: send trace results to text field
    def update_network_scan(self):
        try:
            # if the address is empty ask the user to update it.
            if self.network_lineEdit.text() == "":
                self.Network_Scan_Result.setPlainText("Address field is empy.\nTry google.com")
            else:
                # Run the trace command
                self.Network_Scan_Result.setPlainText("running trace")
                self.network_scan_btn.setEnabled(False)
                if os_name == 'Windows':
                    output = subprocess.run(['tracert', self.network_lineEdit.text()], capture_output=True)
                elif os_name == 'Linux':
                    output = subprocess.run(['traceroute', self.network_lineEdit.text()], capture_output=True)
                else:
                    output = ''

                # Display the output of the trace command
                self.Network_Scan_Result.setPlainText(output.stdout.decode())
                # allow for another scan
                self.network_scan_btn.setEnabled(True)
            
                # Update log file
                data = {
                    'Name': 'Network Scan',
                    'Output': output.stdout[:10],
                    'Time': self.get_current_time()
                }
                self.add_to_xml_file(self.my_file, data)

        except subprocess.CalledProcessError as e:
            # grab up errors
            self.Network_Details_Result.setPlainText(f"Error: {e}")
            # allow for another scan
            self.network_scan_btn.setEnabled(True)


    # Start - Tab 3 - FUNCTION (update_network_scan)
    ##################################################

    ##################################################
    # Start - Tab 4 - FUNCTION (update_port_scan)

    # Function: update_port_scan
    # Purpose: Function to scan network ports for IP address
    # Inputs: self
    # Returns: send port scan result to text field
    def update_port_scan(self):
        # get the ip address
        IP = self.host_lineEdit_2.text()
        # get the port
        from_PORT = int(self.port_lineEdit_3.text())
        to_PORT = int(self.port_lineEdit_4.text())
        # pass
        # Clear the screen
        self.Port_Scan_Result.setText("\nPlease wait, scanning remote host " + self.host_lineEdit_2.text())

        time_start = datetime.now()

        try: 
            # Scan the port range
            for port in range(from_PORT, to_PORT):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((IP, port))

                if result == 0:
                    try:
                        # scan the port
                        serviceName = socket.getservbyport(port, "tcp")
                        self.Port_Scan_Result.append("Port: {: >5} Open -|- Service is: {: >2}".format(port, serviceName))
                    except:
                        # backup scan if the other doesn't have a service
                        self.Port_Scan_Result.append("Port: {: >5} Open -|- Service is: UNKNOWN".format(port, " "))
            
                    # Update log file
                    data = {
                        'Name': 'Port Scan',
                        'Run_Time': "Port: {: >5} Open -|- Service is: {: >2}".format(port, serviceName),
                        'Time': self.get_current_time()
                    }
                    self.add_to_xml_file(self.my_file, data)

        # Error handling
        except socket.error as e:
            self.Port_Scan_Result.setText(f"Error {e}")
            return

        run_time = str(datetime.now() - time_start)
        self.Port_Scan_Result.append("Scanning completed in: " + run_time)

    # Start - Tab 4 - FUNCTION (update_port_scan)
    ##################################################

    ##################################################
    # Start - Tab 5 - FUNCTION (ping_destination)
    
    # Function: ping_destination
    # Purpose: Function to ping IP address
    # Inputs: self
    # Returns: send ping result to text field
    def ping_destination(self):
        try:
            # Clear fields and disable the button so we don't have double runs
            self.Ping_Status_Result.setPlainText("")
            self.ip_scan_btn_5.setEnabled(False)
            
            # If the address is empty tell the user
            if self.port_lineEdit_5.text() == "":
                self.Ping_Status_Result.setPlainText("Address field is empty.")
            else:
                # Ready to run the ping command
                self.network_scan_btn.setEnabled(False)
                # Test for the OS type and run the command
                if os_name == 'Windows':
                    output = subprocess.run(['ping ', self.port_lineEdit_5.text()], capture_output=True)
                elif os_name == 'Linux':
                    # print("ping -c 3 " + self.port_lineEdit_5.text())
                    output = subprocess.run(['ping', '-c', '3', self.port_lineEdit_5.text()], capture_output=True)
                else:
                    output = ''
            # show the results and enable the button so the ping can be run again.
            self.Ping_Status_Result.setPlainText(output.stdout.decode())
            self.ip_scan_btn_5.setEnabled(True)
            
            # Update log file
            data = {
                'Name': 'Ping',
                'Destination': self.port_lineEdit_5.text(),
                'Output': output.stdout[:10],
                'Time': self.get_current_time()
            }
            self.add_to_xml_file(self.my_file, data)

        # Error handling
        except subprocess.CalledProcessError as e:
            # grab up errors
            self.Ping_Status_Result.setPlainText(f'Error: {e}')
            self.ip_scan_btn_5.setEnabled(True)

    # Start - Tab 5 - FUNCTION (ping_destination)
    ##################################################

    ##################################################
    # Start - Tab 6 - FUNCTION (Network Map)
    
    # Function: get_network_picture
    # Purpose: Function to retrieve and show network connections
    # Inputs: self
    # Returns: show network connection diagram
    def get_network_picture(self):
        ################################################
        # self.figure = Figure()
        # self.ax = self.figure.add_subplot(111)
        # self.ax.plot([1,2,3,4], [30, 25, 20, 10], 'r')

        # self.canvas = FigureCanvas(self.figure)
        # self.canvas.setParent(self.tab_6)
        # self.canvas.setGeometry(10, 70, 341, 231)
        # self.canvas.setVisible(True)
        # self.canvas.draw()
        ################################################

        # Just in case clear everything so we don't have double images.
        self.figure.clear()

        try:
            # Scan for network connections
            nm = nmap.PortScanner()
            ip = self.get_ip_6.text() + "/24"
            # Scan the local network
            nm.scan(hosts=ip, arguments='-sn')

            # Create a graph object
            G = nx.Graph()

            # Add nodes to the graph
            previousHost = ''
            for host in nm.all_hosts():
                
                G.add_node(host)

                # Add edges were needed
                if len(previousHost) != 0:
                    # print("found an edge")
                    G.add_edge(host, previousHost)

                if previousHost == '':
                    # print("update previousHost")
                    previousHost = host
                else:
                    # print("update previousHost again")
                    previousHost = host

            # Add nodes and edges to G
            nx.draw(G, with_labels=True)
            plt.tight_layout()

            self.canvas = FigureCanvas(self.figure)
            self.canvas.setParent(self.tab_6)
            self.canvas.setGeometry(10, 70, 341, 231)
            self.canvas.setVisible(True)
            self.canvas.draw()
            
            # Update log file
            data = {
                'Name': 'Network Picture',
                'note': 'Created network picture',
                'Time': self.get_current_time()
            }
            self.add_to_xml_file(self.my_file, data)
        
        # Error handling
        except Exception as e:
            # this will show up in the console but I don't have a label or something else to put it at that would look ok.
            print(f"NMap not found {e}")

    # Start - Tab 6 - FUNCTION (Network Map)
    ##################################################

    ##################################################
    # Start - Tab 7 - FUNCTION (security_log)

    # Function: get_security_log
    # Purpose: Call the correct function based on the OS
    # Inputs: self
    # Returns: none, calls the correct function
    def get_security_log(self):
        # test for windows or linux run the appropriate version
        if os_name == 'Windows':
            self.get_windows_log()
        elif os_name == 'Linux':
            self.get_linux_log()
        else:
            self.showSecurityLog_TextBrowser.setText("COULD NOT FIND YOUR OPERATING SYSTEM")
            
        # Update log file
        data = {
            'Name': 'Security Log',
            'note': 'Complted getting security log',
            'Time': self.get_current_time()
        }
        self.add_to_xml_file(self.my_file, data)

    # Function: reset_security_log
    # Purpose: reset all the fields and adjust the TextBrowser
    # Inputs: self
    # Returns: none, it adjust TextBrowser to the original size
    def reset_security_log(self):
        # reset all the fields and adjust the TextBrowser
        # clear all the things
        self.HostName_LineEdit.setText("")
        self.UserName_LineEdit.setText("")
        self.Return_LineEdit.setText("")
        self.Return_LineEdit.setText("")
        self.ID_LineEdit.setText("")
        # clear the text browser
        self.showSecurityLog_TextBrowser.setText("")
        # clear password
        self.PassWord_LineEdit.setText("")

        self.showSecurityLog_TextBrowser.setGeometry(QtCore.QRect(10, 131, 341, 141))

    # Function: get_windows_log
    # Purpose: Gets the security logs from a Windows machine
    # Inputs: self
    # Returns: updates TextBrowser with the security logs
    def get_windows_log(self):
        # Setup IP/Name

        # Make sure all fields have something in them
        if not all([self.HostName_LineEdit.text(), self.UserName_LineEdit.text(), self.Return_LineEdit.text(), self.ID_LineEdit.text(), self.PassWord_LineEdit.text()]):
            self.showSecurityLog_TextBrowser.setText("One or more fields are empty.")
            self.showSecurityLog_TextBrowser.append("Please fill in all the required fields.")

            # clear all the things
            self.HostName_LineEdit.setText("")
            self.UserName_LineEdit.setText("")
            self.Return_LineEdit.setText("")
            self.Return_LineEdit.setText("")
            self.ID_LineEdit.setText("")
            # clear password
            self.PassWord_LineEdit.setText("")

            return
        # check if the value is an integer
        try:
            int(self.Return_LineEdit.text())
            int(self.ID_LineEdit.text())
        except ValueError:
            self.showSecurityLog_TextBrowser.setText("Return value and ID must be a valid integer.")
            # clear all the things
            self.Return_LineEdit.setText("")
            self.ID_LineEdit.setText("")
            # clear password
            self.PassWord_LineEdit.setText("")

            return

        # assuming everything is ready to go at this point.
        host_name = str(self.HostName_LineEdit.text())
        user_name = str(self.UserName_LineEdit.text())
        return_no = int(self.Return_LineEdit.text())
        ID_number = int(self.ID_LineEdit.text())
        # adjust Text Browser for more room
        self.showSecurityLog_TextBrowser.setGeometry(QtCore.QRect(10, 80, 341, 192))


        # preform ssh, and scan security file
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host_name, username=user_name, password=self.PassWord_LineEdit.text())

        command = "powershell.exe Get-WinEvent -FilterHashtable @{{logname='security'; id={}}} -MaxEvents {}".format(ID_number, return_no)
        _, stdout, _ = ssh.exec_command(command)

        result = stdout.read().decode()
        lines = result.split("\n")
        # make sure the browser is empty
        if lines:
            self.showSecurityLog_TextBrowser.setText("")
        for line in lines:
            if line.strip():
                line_split = line.strip().split(" ", maxsplit=1)
                self.showSecurityLog_TextBrowser.append(line_split[-1])
                # print(line_split[-1])
        ssh.close()

        # clear password
        self.PassWord_LineEdit.setText("")

    # Function: get_linux_log
    # Purpose: Gets the security logs from a Linux machine
    # Inputs: self
    # Returns: updates TextBrowser with the security logs
    def get_linux_log(self):

        # make sure all fields have something in them
        if not all([self.HostName_LineEdit.text(), self.UserName_LineEdit.text(), self.Return_LineEdit.text(), self.PassWord_LineEdit.text()]):
            self.showSecurityLog_TextBrowser.setText("One or more fields are empty.")
            self.showSecurityLog_TextBrowser.append("Please fill in all the required fields.")

            # clear all the things
            self.HostName_LineEdit.setText("")
            self.UserName_LineEdit.setText("")
            self.Return_LineEdit.setText("")
            self.Return_LineEdit.setText("")
            self.ID_LineEdit.setText("")
            # clear password
            self.PassWord_LineEdit.setText("")

            return
        # check if the value is an integer
        try:
            int(self.Return_LineEdit.text())
        except ValueError:
            self.showSecurityLog_TextBrowser.setText("Return value and ID must be a valid integer.")
            # clear all the things
            self.Return_LineEdit.setText("")
            self.ID_LineEdit.setText("")
            # clear password
            self.PassWord_LineEdit.setText("")

            return

        # assuming everything is ready to go at this point.
        host_name = str(self.HostName_LineEdit.text())
        user_name = str(self.UserName_LineEdit.text())
        return_no = int(self.Return_LineEdit.text())
        # adjust Text Browser for more room
        self.showSecurityLog_TextBrowser.setGeometry(QtCore.QRect(10, 80, 341, 192))

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host_name, port=22, username=user_name, password=self.PassWord_LineEdit.text())
        except Exception as e:
            print(f"Error connecting to the host: {e}")

        command = "last -n {} | grep \"logged in\"".format(return_no)
        # print(f"1: {command}")

        _, stdout, _ = ssh.exec_command(command)
        # print(f"2: {stdout}")

        result = stdout.readlines()
        result = "".join(result)
        # print(f"3: {result}")

        self.showSecurityLog_TextBrowser.setText(result)

        ssh.close()

        # clear password
        self.PassWord_LineEdit.setText("")

    # Start - Tab 7 - FUNCTION (security_log)
    ##################################################

    ##################################################
    # Start - Tab 8 - FUNCTION (Backup over network)
    
    # Function: get_network_files
    # Purpose: Calls the correct function based on the OS
    #          performs inital setup and checks
    # Inputs: self
    # Returns: none, calls a function based on operating system
    def get_network_files(self):
        if not all([self.HostName_LineEdit2.text(), self.UserName_LineEdit2.text(), self.PassWord_LineEdit2.text()]):
            self.showRetrievedFiles_TextBrowser.setText("One or more fields are empty.")
            self.showRetrievedFiles_TextBrowser.append("Please fill in all the required fields.")

            # clear all the things
            self.HostName_LineEdit2.setText("")
            self.UserName_LineEdit2.setText("")
            self.PassWord_LineEdit2.setText("")

            return
        # setup
        current_dir = os.getcwd()
        files = os.listdir(current_dir)
        # show what files are currently in your directory
        self.showRetrievedFiles_TextBrowser.setText(f"{files}")

        try:
            # Connect to the hostname - windows or linux
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.HostName_LineEdit2.text(), username=self.UserName_LineEdit2.text(), password=self.PassWord_LineEdit2.text())
            # clear the password field
            self.PassWord_LineEdit2.setText("")

            # get the hosts pc name and os name
            _, stdout, _ = client.exec_command("hostname")
            pcHostName = stdout.read().decode().strip()
            _, stdout, _ = client.exec_command("uname")
            os_name = stdout.read().decode().strip()
            # make a new folder for a new pc if it doesn't exits
            if not os.path.exists(pcHostName):
                os.makedirs(pcHostName)

            if os_name == 'Windows':
                self.backup_windows_files(client, pcHostName)
            elif os_name == 'Linux':
                self.backup_linux_files(client, pcHostName)
            else:
                self.showRetrievedFiles_TextBrowser.setText("COULD NOT FIND YOUR OPERATING SYSTEM")
            # Make sure the connnect is closed
            client.close()

            files = os.listdir(current_dir)
            # show what files are currently in your directory
            self.showRetrievedFiles_TextBrowser.append("="*20)
            self.showRetrievedFiles_TextBrowser.append(f"{files}")
            
            # Update log file
            data = {
                'Name': 'Backup network files',
                'note': 'Complted getting network files',
                'Time': self.get_current_time()
            }
            self.add_to_xml_file(self.my_file, data)

        except Exception as e:
            # Grab up the errors
            print(f"Error connecting to the host: {e}")
            # clear the password field
            self.PassWord_LineEdit2.setText("")

    # Function: backup_windows_files
    # Purpose: Function to backup important files over the network
    # Inputs: self
    # Returns: none, but files are saved locally under the name of the PC
    def backup_windows_files(self, client, pcHostName):
        try:
            # setup scp
            # scp = client.open_sftp()
            scp = SCPClient(client.get_transport())
            # scp.get(remote_file, filename)
            # scp.get(log_location + filename, filename)

            # copy over the files
            scp.get("C:/Windows/System32/winevt/Logs/Application.evtx", pcHostName)
            scp.get("C:/Windows/System32/winevt/Logs/System.evtx", pcHostName)
            scp.get("C:/Windows/System32/winevt/Logs/Security.evtx", pcHostName)
        except Exception as e:
            # grab the error
            print(f"Error orrucred: {e}")
        finally:
            # close the connection
            scp.close()

    # Function: backup_linux_files
    # Purpose: Function to backup important files over the network
    # Inputs: self
    # Returns: none, but files are saved locally under the name of the PC
    def backup_linux_files(self, client, pcHostName):
        try:
            # setup scp
            scp = SCPClient(client.get_transport())
            # copy over the files
            scp.get("/etc/passwd", pcHostName)
            scp.get("/etc/fstab", pcHostName)
            scp.get("/etc/hosts", pcHostName)
        except Exception as e:
            # grab the error
            print(f"Error orrucred: {e}")
        finally:
            # close the connection
            scp.close()

    # Start - Tab 8 - FUNCTION (Backup over network)
    ##################################################

# Name: Main entry point
# Purpose: Tell python it is running as a stand alone program
# Inputs: None
# Returns: None
if __name__ == "__main__":
    # Creates a new QApplication - manages the GUI
    app = QtWidgets.QApplication(sys.argv)
    # Creates a new QWidget - dialog box top level
    Form = QtWidgets.QWidget()
    # Creates a new object of the Ui_Form class (starts the ball rolling)
    ui = Ui_Form()
    # Starts the UI and places everthing
    ui.setupUi(Form)
    # Displays the UI form to the screen
    Form.show()
    # lets the program exit properly
    sys.exit(app.exec())
