from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.uic import loadUi
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("Schedular.ui", self)

    
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

