from PyQt6 import QtWidgets, QtGui

app = QtWidgets.QApplication([])
tab_widget = QtWidgets.QTabWidget()
tab_widget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)

# Create an icon from an SVG file
# icon1 = QtGui.QIcon("speedometer2.svg")
icon1 = QtGui.QIcon(QtGui.QPixmap("speedometer2.svg").transformed(QtGui.QTransform().rotate(90)))
icon2 = QtGui.QIcon(QtGui.QPixmap("hdd-network-fill.svg").transformed(QtGui.QTransform().rotate(90)))
icon3 = QtGui.QIcon(QtGui.QPixmap("chat-right-dots.svg").transformed(QtGui.QTransform().rotate(90)))

# Add tab with icon
tab_widget.addTab(QtWidgets.QWidget(), icon1, "")
tab_widget.addTab(QtWidgets.QWidget(), icon2, "")
tab_widget.addTab(QtWidgets.QWidget(), icon3, "")


tab_widget.show()
app.exec()
