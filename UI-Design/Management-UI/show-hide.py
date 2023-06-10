from PyQt6 import QtWidgets, uic, QtCore
import qtawesome as qta
import sys

# Python QT Charts
# https://www.youtube.com/watch?v=20ed0Ytkxuw&list=PLJ8t3BKaQLhPltjWNb0QApviqiXSqHeb6
import os
# import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np

import random

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi('show-hide-test.ui', self)

        # Set the icon for your QPushButton
        # ri.pie-chart-line     # QT Charts
        ## mdi.equalizer         # percent
        ## ri.temp-hot-fill      # temperature
        ## mdi.bullseye          # Nested Donut Chart
        ## fa.code-fork          # Line Chart
        ## fa.bar-chart-o        # Bar Chart
        ## fa5.smile-wink        # Support
        # mdi6.patreon          # Patreon
        # mdi6.youtube-studio   # Youtube
        # fa.paypal             # Paypal
        # fa5.window-restore    # Maximize
        # mdi.close-thick     # Close

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

        # set right_menu_widget as hidden when starting the application
        self.right_menu_widget.setHidden(True)

        ############################################################################################################
        # BUTTON CONNECTIONS
        # show and hide the right_menu_widget when menu_button is clicked
        self.right_menu_button.clicked.connect(lambda: self.right_menu_widget.setHidden(not self.right_menu_widget.isHidden()))
        self.left_menu_button.clicked.connect(lambda: self.left_menu_widget.setHidden(not self.left_menu_widget.isHidden()))
        self.dashboard_pushButton.clicked.connect(self.show_dashboard)
        self.cost_pushButton.clicked.connect(self.show_cost)
        self.work_orders_pushButton.clicked.connect(self.show_work_orders_view)
        self.inventory_pushButton.clicked.connect(self.show_inventory_view)
        self.charts_pushButton.clicked.connect(self.show_charts_view)

    def resizeEvent(self, event):
        # print("frame_16 size:", self.size())  # Print the size of frame_16
        self.canvas.setGeometry(self.frame_16.rect())
        event.accept()

    ############################################################################################################
    # SWAP STACKED WIDGETS (SCREENS)
    def show_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard_view)
    def show_cost(self):
        self.stacked_widget.setCurrentWidget(self.cost_view)
    def show_work_orders_view(self):
        self.stacked_widget.setCurrentWidget(self.work_orders_view)
    def show_inventory_view(self):
        self.stacked_widget.setCurrentWidget(self.inventory_view)
    def show_charts_view(self):
        self.stacked_widget.setCurrentWidget(self.charts_view)

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
        self.canvas.setParent(self.frame_16)
        self.canvas.setGeometry(self.rect())

        # # Create a QVBoxLayout for frame_16
        # layout = QtWidgets.QVBoxLayout(self.frame_16)
        # layout.addWidget(self.canvas)

        # # Set the QVBoxLayout as the layout for frame_16
        # self.frame_16.setLayout(layout)

        # # Set a tight layout for the frame
        # layout.setContentsMargins(0, 0, 0, 0)  # Set layout margins to zero
        # layout.setSpacing(0)  # Set spacing between widgets to zero
        # layout.addStretch(1)  # Add a stretchable space at the end of the layout

        # Show the canvas and redraw
        self.canvas.setVisible(True)
        self.canvas.draw()








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
