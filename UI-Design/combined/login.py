#!/usr/local/bin/python3.9
import sys
import json
import getpass
import subprocess
from cryptography.fernet import Fernet
from utilities import decrypt_config, Validator
from database_utilites import execute_query, execute_insert_query
from login_utilities import authenticate, get_user_role


from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import loadUi



# Decrypt and save the config
config = decrypt_config()

# Set db_host, db_user, db_password, and db_database for later use
db_host = config['host']
db_user = config['user']
db_password = config['password']
db_database = config['database']

# Get the username from the user
# username = input("Enter your username: ")

# Get the password securely
# password = getpass.getpass("Enter your password: ")

# print(f"username {username} password {password}")



# # Use the functions as needed
# result = execute_query("SELECT * FROM table_name", params=None)
# execute_insert_query("INSERT INTO table_name (column1, column2) VALUES (%s, %s)", params=(value1, value2))

# if authenticate("username", "password", db_host, db_user, db_password, db_database):
#     role = get_user_role("username", db_host, db_user, db_password, db_database)
#     print("User role:", role)

# if Validator.validate_email("example@example.com"):
#     print("Valid email")

# if Validator.validate_password("password123"):
#     print("Valid password")



class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui",self)
        self.LoginPushButton.clicked.connect(self.loginfunction)
        self.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.GetAccountPushButton.clicked.connect(self.gotocreateacc)

    def loginfunction(self):
        username = self.EmailLineEdit.text()
        password = self.PasswordLineEdit.text()
        if not Validator.validate_username(username):
            self.EmailLineEdit.setText("Invalid username")
            return
        elif not Validator.validate_password(password):
            self.PasswordLineEdit.setText("Invalid password")
            return
        else:
            # print("Successfully logged in with email ", email, " and password ", password)
            # switch to the appropriate screen based on the user's role 'MANAGER', 'MAINTENANCE', 'LOGISTICS'
            # Authenticate the user
            if authenticate(username, password):
                # Execute the appropriate script based on the user's role
                role = get_user_role(username)

                # Execute the appropriate script based on the user's role
                if role == 'MANAGER':
                    try:
                        print("MANAGER")
                        # subprocess.Popen(["python", "management/Management-UI.py"])
                        subprocess.Popen(["/usr/local/bin/python3.9", "Management-UI.py"])
                    except subprocess.CalledProcessError as e:
                        print("Error executing Management script: ", e)
                elif role == 'MAINTENANCE':
                    try:
                        print("MAINTENANCE")
                        subprocess.Popen(["/usr/local/bin/python3.9", "Maintenance-UI.py"])
                    except subprocess.CalledProcessError as e:
                        print("Error executing Maintenance script: ", e)
                elif role == 'LOGISTICS':
                    try:
                        print("LOGISTICS")
                        # subprocess.Popen(["/usr/local/bin/python3.9", "Logistics-UI.py"])
                    except subprocess.CalledProcessError as e:
                        print("Error executing Logistics script: ", e)
                else:
                    print("Default failure, no script found to run.")
                    sys.exit(1)
            sys.exit(0)

    # Switches from Login screen to Create Account screen
    def gotocreateacc(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("createaccount.ui",self)
        self.SignUpPushButton.clicked.connect(self.createaccfunction)
        self.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.ConfirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def createaccfunction(self):
        email = self.EmailLineEdit.text()
        print("pass: ", self.PasswordLineEdit.text(), " confirmpass: ", self.ConfirmPasswordLineEdit.text())
        if self.PasswordLineEdit.text() == self.ConfirmPasswordLineEdit.text():
            if not Validator.validate_email(email):
                print("Invalid email")
                return
            password = self.PasswordLineEdit.text()
            print("Successfully created account with email ", email, " and password ", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(480)
    widget.setFixedHeight(620)
    widget.show()
    app.exec()
