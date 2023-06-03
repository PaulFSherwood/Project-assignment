import sys
import ctypes
from PyQt6 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QMainWindow()
Form.resize(400, 300)

Form.setWindowIcon(QtGui.QIcon("images/me.png"))

# Taskbar Icon fix from: https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

Form.show()
sys.exit(app.exec())
