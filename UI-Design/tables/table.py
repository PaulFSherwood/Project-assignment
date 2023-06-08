import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("table.ui", self)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,350)
        self.load_data()

    # function to load all the Data
    # Note: this could be dangerous for two reasons:
        # 1. If the file is too big, it will take a long time to load
        # 2. User input could be corrupted
    def load_data(self):
        # sample data
        people = [{"name": "John", "age": 30, "address": "New York"},\
                  {"name": "Marie", "age": 25, "address": "Paris"},\
                  {"name": "Carl", "age": 40, "address": "London"},\
                  {"name": "Helen", "age": 21, "address": "Berlin"},\
                  {"name": "Peter", "age": 29, "address": "Rome"},\
                  {"name": "Elisabeth", "age": 38, "address": "Brussels"}]
        
        # set the table row count
        self.tableWidget.setRowCount(len(people))

        # Hide row numbers
        self.tableWidget.verticalHeader().setVisible(False)

        # insert data into the table
        for person in people:
            self.tableWidget.setItem(people.index(person), 0, QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(people.index(person), 1, QtWidgets.QTableWidgetItem(str(person["age"])))
            self.tableWidget.setItem(people.index(person), 2, QtWidgets.QTableWidgetItem(person["address"]))
        # self.tableWidget.setRowCount(0)
        # with open('data.txt') as f:
        #     for row_number, line in enumerate(f):
        #         self.tableWidget.insertRow(row_number)
        #         for column_number, cell in enumerate(line.split('\t')):
        #             self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(cell))
        # self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1120)
widget.setFixedHeight(850)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")
