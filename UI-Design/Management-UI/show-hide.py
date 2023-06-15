from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtCore import Qt

from PyQt6.QtCore import QTimer
import qtawesome as qta
import sys

import os
# import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np


import mysql.connector


# import random

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi('show-hide-test.ui', self)

        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host='localhost',
            user='sherwood',
            password='sherwood',
            database='flight_simulator_db'
        )

        ############################################################################################################
        # ICON SETUP
        # Setting up icons for each button (couldn't find another way to show icons but with buttons)
        self.right_menu_button.setIcon(qta.icon('fa5s.sign-out-alt', color='orange'))
        self.left_menu_button.setIcon(qta.icon('fa5s.sign-in-alt', color='orange', hflip=True))
        self.pushButton_7.setIcon(qta.icon('ri.pie-chart-line', color='orange'))
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))  # Rezise the icon to 32x32

        self.dashboard_pushButton.setIcon(qta.icon('mdi.monitor-dashboard', color='orange'))
        self.cost_pushButton.setIcon(qta.icon('fa5s.money-bill', color='orange'))
        self.work_orders_pushButton.setIcon(qta.icon('ri.list-unordered', color='orange'))
        self.inventory_pushButton.setIcon(qta.icon('mdi.warehouse', color='orange'))
        self.work_orders_pushButton.setIcon(qta.icon('fa.bar-chart-o', color='orange'))
        self.charts_pushButton.setIcon(qta.icon('mdi6.chart-areaspline', color='orange'))

        self.display_sample_bar_chart()
        QTimer.singleShot(0, lambda: self.resizeEvent(None)) # force resize on start
        self.set_awaiting_approval()

        # set right_menu_widget as hidden when starting the application
        self.right_menu_widget.setHidden(True)

        ############################################################################################################
        # BUTTON CONNECTIONS
        # show and hide the right_menu_widget when menu_button is clicked
        self.right_menu_button.clicked.connect(lambda: self.right_menu_widget.setHidden(not self.right_menu_widget.isHidden()))
        self.left_menu_button.clicked.connect(lambda: self.left_menu_widget.setHidden(not self.left_menu_widget.isHidden()))
        self.dashboard_pushButton.clicked.connect(lambda: self.switch_page(self.dashboard_view, "DASHBOARD"))
        self.cost_pushButton.clicked.connect(lambda: self.switch_page(self.cost_view, "COST"))
        self.work_orders_pushButton.clicked.connect(lambda: self.switch_page(self.work_orders_view, "WORK ORDERS"))
        self.inventory_pushButton.clicked.connect(lambda: self.switch_page(self.inventory_view, "INVENTORY"))
        self.charts_pushButton.clicked.connect(lambda: self.switch_page(self.charts_view, "CHARTS"))

        ############################################################################################################
        # TABLE SETUP / TAB SETUP
        self.load_table_data()
        self.load_work_order_data()
        self.load_inventory_data()
        self.load_charts_data()

        self.set_priority_counts()

    def execute_query(self, query):
        # Connection to the flight sim database
        db = mysql.connector.connect(
            host='localhost',
            user='sherwood',
            password='sherwood',
            database='flight_simulator_db'
        )
        # Create the cursor for the look in the db
        cursor = db.cursor()
        # Execute the query passed in by the user / function
        cursor.execute(query)
        # save the result
        result = cursor.fetchall()
        # close the connection
        cursor.close()
        db.close()
        return result
    
    def switch_page(self, widget, title):
        self.stackedWidget.setCurrentWidget(widget)
        self.title_label.setText(title)

    def resizeEvent(self, event):
        # print("frame_16 size:", self.size())  # Print the size of frame_16
        self.canvas.setGeometry(self.dashboard_frame_left.rect())
        if event:
            event.accept()

    def display_sample_bar_chart(self):
        # Generate sample data for the bar chart
        self.labels = ['A', 'B', 'C', 'D', 'E']
        self.data = [10, 5, 8, 12, 3]

        # Create a figure and axis for the bar chart
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # Set the positions of the bars on the x-axis
        self.x = np.arange(len(self.labels))

        # Plot the bar chart
        self.ax.bar(self.x, self.data)

        # Set labels and title
        self.ax.set_xlabel('Categories')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Sample Bar Chart')

        # Create a FigureCanvas widget for the plot
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.dashboard_frame_left)
        # self.canvas.setGeometry(self.rect())
        self.canvas.setGeometry(self.dashboard_frame_left.rect())
        

        # Show the canvas and redraw
        self.canvas.setVisible(True)
        self.canvas.draw()

    def set_priority_counts(self):
        query = "SELECT priority, COUNT(*) FROM WorkOrders GROUP BY priority"
        result = self.execute_query(query)

        # Store the counts
        priority_totals = {}
        for priority_count in result:
            priority = priority_count[0]
            count = priority_count[1]
            priority_totals[priority] = count

        # set pri_1_count
        self.pri_1_count.setText(str(priority_totals[1]))
        # set pri_2_count
        self.pri_2_count.setText(str(priority_totals[2]))
        # set pri_3_count
        self.pri_3_count.setText(str(priority_totals[3]))
        
    def set_awaiting_approval(self):
        query = "SELECT creation_reason FROM WorkOrders ORDER BY creation_date DESC LIMIT 5"
        result = self.execute_query(query)

        for i, work_order in enumerate(result):
            label_name = f"set_{i+1}_count"  # Assuming the QLabel attribute names follow the pattern set_1_count, set_2_count, etc.
            label = getattr(self, label_name, None)
            if label is not None:
                label.setText(str(work_order[0]))
        # # set pri_1_count label
        # self.set_1_count.setText(str("HDD needs to be replaced"))
        # self.set_2_count.setText(str("Preflight"))
        # self.set_3_count.setText(str("Purchase request"))
        # self.set_4_count.setText(str("Awaiting Engineering"))
        # self.set_5_count.setText(str("..."))

    ############################################################################################################
    # LOAD TABLE DATA
    def load_table_data(self):
        #########################
        ## UPPER TABLE
        # Sample data for the man hours table (User, Hours Worked, Cost)
        man_hours_data = [{"user": "John", "hours_worked": 4, "cost": 100},\
                          {"user": "Jane", "hours_worked": 2, "cost": 50},\
                          {"user": "Bob", "hours_worked": 1, "cost": 25},\
                          {"user": "Mary", "hours_worked": 5, "cost": 125},\
                          {"user": "Mike", "hours_worked": 3, "cost": 75}]
        # set the number of rows
        self.cost_upper_table.setRowCount(len(man_hours_data))
        # hide row numbers
        self.cost_upper_table.verticalHeader().setVisible(False)
        # push data into the table
        for user in man_hours_data:
            self.cost_upper_table.setItem(man_hours_data.index(user), 0, QtWidgets.QTableWidgetItem(user["user"]))
            self.cost_upper_table.setItem(man_hours_data.index(user), 1, QtWidgets.QTableWidgetItem(str(user["hours_worked"])))
            self.cost_upper_table.setItem(man_hours_data.index(user), 2, QtWidgets.QTableWidgetItem(str(user["cost"])))
        
        #########################
        ## LOWER TABLE
        # Sample data for the parts table (User, Part, Price, Date)
        parts_data = [{"user": "John", "part": "HDD", "price": 100, "date": "2021-01-01"},\
                        {"user": "Jane", "part": "RAM", "price": 50, "date": "2021-01-02"},\
                        {"user": "Bob", "part": "CPU", "price": 25, "date": "2021-01-03"},\
                        {"user": "Mary", "part": "GPU", "price": 125, "date": "2021-01-04"},\
                        {"user": "Mike", "part": "PSU", "price": 75, "date": "2021-01-05"}]
        # set the number of rows
        self.cost_lower_table.setRowCount(len(parts_data))
        # hide row numbers
        self.cost_lower_table.verticalHeader().setVisible(False)
        # push data into the table
        for user in parts_data:
            self.cost_lower_table.setItem(parts_data.index(user), 0, QtWidgets.QTableWidgetItem(user["user"]))
            self.cost_lower_table.setItem(parts_data.index(user), 1, QtWidgets.QTableWidgetItem(user["part"]))
            self.cost_lower_table.setItem(parts_data.index(user), 2, QtWidgets.QTableWidgetItem(str(user["price"])))
            self.cost_lower_table.setItem(parts_data.index(user), 3, QtWidgets.QTableWidgetItem(user["date"]))
        
    def load_work_order_data(self):

        # Execute the query to fetch the data
        query = "SELECT jcn, creation_reason, reported_by_name, priority, notes FROM WorkOrders"


        # Fetch all the rows returned by the query
        work_order_data = self.execute_query(query)

        # set the number of rows
        self.work_order_table.setRowCount(len(work_order_data))
        # hide row numbers
        self.work_order_table.verticalHeader().setVisible(False)
        # set column widths
        self.work_order_table.setColumnWidth(0, 100) # JCN
        self.work_order_table.setColumnWidth(1, 200) # Reason
        self.work_order_table.setColumnWidth(2, 100) # User
        self.work_order_table.setColumnWidth(3, 100) # Priority
        # resize "Notes" column to fill remaining space
        self.work_order_table.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        # push data into the table
        row_index = 0  # Initialize the row index
        # push data into the table
        for work_order in work_order_data:
            self.work_order_table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(str(work_order[0])))  # jcn
            self.work_order_table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(work_order[1]))  # creation_reason
            self.work_order_table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(work_order[2]))  # reported_by_name
            
            # Center the priority number
            priority_item = QtWidgets.QTableWidgetItem(str(work_order[3]))  # priority
            priority_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the content
            self.work_order_table.setItem(row_index, 3, priority_item)
            
            self.work_order_table.setItem(row_index, 4, QtWidgets.QTableWidgetItem(work_order[4]))  # notes
            row_index += 1  # Increment the row index


        # if the priority is 1, set the background color of that priority cell to red
        for row in range(self.work_order_table.rowCount()):
            priority_item = self.work_order_table.item(row, 3)
            priority = priority_item.text()
            if priority == "1":
                priority_item.setBackground(QtGui.QColor(255, 0, 0))
            elif priority == "2":
                priority_item.setBackground(QtGui.QColor(255, 255, 0))
            elif priority == "3":
                priority_item.setBackground(QtGui.QColor(0, 255, 0))



    def load_inventory_data(self):
        # Sample data for the inventory table (Amount, Name, Min Stock, Location, Cost, Employee)
        inventory_data = [{"amount": 5, "name": "HDD", "min_stock": 5, "location": "61A", "cost": 100, "employee": "John"},\
                            {"amount": 1, "name": "RAM", "min_stock": 10, "location": "4", "cost": 50, "employee": "Jane"},\
                            {"amount": 15, "name": "CPU", "min_stock": 15, "location": "66F", "cost": 25, "employee": "Bob"},\
                            {"amount": 2, "name": "GPU", "min_stock": 5, "location": "12D", "cost": 125, "employee": "Mary"},\
                            {"amount": 10, "name": "PSU", "min_stock": 10, "location": "1", "cost": 75, "employee": "Mike"}]
        # set the number of rows
        self.inventory_table.setRowCount(len(inventory_data))
        # hide row numbers
        self.inventory_table.verticalHeader().setVisible(False)
        # set all column widths evenly between all columns
        for column in range(self.inventory_table.columnCount()):
            self.inventory_table.setColumnWidth(column, 100)

        # push data into the table
        for inventory in inventory_data:
            self.inventory_table.setItem(inventory_data.index(inventory), 0, QtWidgets.QTableWidgetItem(str(inventory["amount"])))
            self.inventory_table.setItem(inventory_data.index(inventory), 1, QtWidgets.QTableWidgetItem(inventory["name"]))
            self.inventory_table.setItem(inventory_data.index(inventory), 2, QtWidgets.QTableWidgetItem(str(inventory["min_stock"])))
            self.inventory_table.setItem(inventory_data.index(inventory), 3, QtWidgets.QTableWidgetItem(inventory["location"]))
            self.inventory_table.setItem(inventory_data.index(inventory), 4, QtWidgets.QTableWidgetItem(str(inventory["cost"])))
            self.inventory_table.setItem(inventory_data.index(inventory), 5, QtWidgets.QTableWidgetItem(inventory["employee"]))

        # if the inventory amount is less than the minimum stock, set the background color of that cell to light red
        ## TODO: This is not working

    def load_charts_data(self):
        # Load a sample bar chart into chart_top (sun,mon,tue, wed, thu, fri, sat) (0, scale to highest value) label Operating cost

        # Generate sample data for the bar chart
        labels = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
        data = [0, 250, 1500, 2500, 250, 1000, 0]

        # Create a figure and axis for the bar chart
        fig = Figure()
        ax = fig.add_subplot(111)

        # Set the positions of the bars on the x-axis
        x = np.arange(len(labels))

        # Plot the bar chart
        ax.bar(x, data)

        # Set labels and title
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.set_title('Sample Bar Chart')

        # Create a FigureCanvas widget for the plot
        canvas = FigureCanvas(fig)
        canvas.setParent(self.chart_top)
        canvas.setGeometry(self.chart_top.rect())
        # canvas.setGeometry(self.rect())

        # Show the canvas and redraw
        canvas.setVisible(True)
        canvas.draw()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
