from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtCore import Qt, QPointF, QTimer
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen

from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QPieSeries, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt6.QtGui import QPainter, QPen, QBrush, QFont
from PyQt6.QtCore import Qt, QPointF

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

    ############################################################################################################
    # SQL FUNCTION
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
    
    ############################################################################################################
    # DASHBOARD FUNCTIONS
    def switch_page(self, widget, title):
        self.stackedWidget.setCurrentWidget(widget)
        self.title_label.setText(title)

    def resizeEvent(self, event):
        # print("frame_16 size:", self.size())  # Print the size of frame_16
        # self.canvas.setGeometry(self.dashboard_frame_left.rect())
        if event:
            event.accept()
        if hasattr(self, 'dashBoardSeries'):
            self.dashBoardSeries.resize(self.dashboard_frame_left.size())
        if hasattr(self, 'topChartview'):
            self.topChartview.resize(self.chart_top.size())
        if hasattr(self, 'bottomChartview'):
            self.bottomChartview.resize(self.chart_bottom.size())
        super().resizeEvent(event)

    ############################################################################################################
    # Helper Function
    def create_bar_set(self, label, value):
        barSet = QBarSet(label)
        barSet.append(value)
        return barSet
    
    def display_sample_bar_chart(self):
        # use QBarSeries for bar chart sample
        dashBoardBarSeries = QBarSeries(self)
        dashBoardBarSeries.append(self.create_bar_set("A", 10))
        dashBoardBarSeries.append(self.create_bar_set("B", 5))
        dashBoardBarSeries.append(self.create_bar_set("C", 8))
        dashBoardBarSeries.append(self.create_bar_set("D", 12))
        dashBoardBarSeries.append(self.create_bar_set("E", 3))

        dashBoardSeries = QChart()
        dashBoardSeries.addSeries(dashBoardBarSeries)
        dashBoardSeries.createDefaultAxes()

        self.dashBoardChartView = QChartView()
        self.dashBoardChartView.setChart(dashBoardSeries)
        self.dashBoardChartView.setRenderHint(QPainter.Antialiasing)

        self.dashBoardChartView.setParent(self.dashboard_frame_left)
        self.dashBoardChartView.resize(self.dashboard_frame_left.size())
        # print("Frame width: ", self.dashboard_frame_left.width())
        # print("Frame height: ", self.dashboard_frame_left.height())
        # print("Chart width: ", self.dashBoardChartView.width())
        # print("Chart height: ", self.dashBoardChartView.height())



    ############################################################################################################
    # TABS
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
        tech_cost_data = self.execute_query("CALL GetTechSummary()")

        print(type(tech_cost_data))

        # set the number of rows
        self.cost_upper_table.setRowCount(len(tech_cost_data))
        # hide row numbers
        self.cost_upper_table.verticalHeader().setVisible(False)

        # push data into the table
        for i, record in enumerate(tech_cost_data):
            self.cost_upper_table.setItem(i, 0, QtWidgets.QTableWidgetItem(record[0]))      # tech name
            self.cost_upper_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(record[1]))) # total cost
            self.cost_upper_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(record[1]))) # total hours

        #########################
        ## LOWER TABLE
        parts_data = self.execute_query("CALL show_parts_data()")
        # set the number of rows
        self.cost_lower_table.setRowCount(len(parts_data))
        # hide row numbers
        self.cost_lower_table.verticalHeader().setVisible(False)
        # push data into the table
        for i, record in enumerate(parts_data):
            self.cost_lower_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(record[0])))  # item name
            self.cost_lower_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(record[1])))  # cost per item
            self.cost_lower_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(record[2])))  # due date
            self.cost_lower_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(record[3])))  # priority

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
                priority_item.setBackground(QtGui.QColor(255, 0, 0))  # Red background
                priority_item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))  # White text color
            elif priority == "2":
                priority_item.setBackground(QtGui.QColor(255, 255, 0))  # Yellow background
                priority_item.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 0)))  # Black text color
            elif priority == "3":
                priority_item.setBackground(QtGui.QColor(0, 255, 0))  # Green background
                priority_item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))  # White text color

    def load_inventory_data(self):
        # Execute the query to fetch the data       
        inventory_data = self.execute_query("CALL GetInventoryData()")

        # set the number of rows
        self.inventory_table.setRowCount(len(inventory_data))
        # hide row numbers
        self.inventory_table.verticalHeader().setVisible(False)
        # set all column widths evenly between all columns
        for column in range(self.inventory_table.columnCount()):
            self.inventory_table.setColumnWidth(column, 100)

        # push data into the table
        for i, inventory in enumerate(inventory_data):
            self.inventory_table.setItem(i, 0, QtWidgets.QTableWidgetItem(inventory[1]))  # item_name
            self.inventory_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(inventory[0])))  # stock_on_hand
            self.inventory_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(inventory[2])))  # minimum_stock_number
            self.inventory_table.setItem(i, 3, QtWidgets.QTableWidgetItem(inventory[3]))  # stock_location
            self.inventory_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(inventory[4])))  # cost_per_item
            self.inventory_table.setItem(i, 5, QtWidgets.QTableWidgetItem(inventory[5]))  # username

        # if the inventory amount is less than the minimum stock, set the background color of that cell to light red
        for row in range(self.inventory_table.rowCount()):
            stock_on_hand_item = self.inventory_table.item(row, 1)
            stock_on_hand = stock_on_hand_item.text()
            minimum_stock_number_item = self.inventory_table.item(row, 2)
            minimum_stock_number = minimum_stock_number_item.text()
            if int(stock_on_hand) < int(minimum_stock_number):
                stock_on_hand_item.setBackground(QtGui.QColor(255, 0, 0))
                minimum_stock_number_item.setBackground(QtGui.QColor(255, 0, 0))

    #############################################################################################################
    # LOAD CHARTS DATA     
    def load_charts_data(self):
        topSeries = QLineSeries(self)
        topSeries.append(0, 6)
        topSeries.append(2, 4)
        topSeries.append(3, 8)
        topSeries.append(7, 4)
        topSeries.append(10, 5)
        # topSeries << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) \
        #        << QPointF(18, 3) << QPointF(20, 2)

        topChart = QChart()
        topChart.addSeries(topSeries)
        topChart.createDefaultAxes()

        self.topChartview = QChartView()
        self.topChartview.setChart(topChart)
        self.topChartview.setRenderHint(QPainter.Antialiasing)

        self.topChartview.setParent(self.chart_top)
        self.topChartview.resize(self.chart_top.size())


        ## Bottom chart
        bottomSeries = QPieSeries()
        bottomSeries.append("Shift 1", 2)
        bottomSeries.append("Shift 2", 3)
        bottomSeries.append("Shift 3", 1)

        bottomChart = QChart()
        bottomChart.addSeries(bottomSeries)
        bottomChart.setTitle("Work load by shift")

        self.bottomChartview = QChartView()
        self.bottomChartview.setChart(bottomChart)
        self.bottomChartview.setRenderHint(QPainter.Antialiasing)

        self.bottomChartview.setParent(self.chart_bottom)
        self.bottomChartview.resize(self.chart_bottom.size())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
