from PyQt6 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create text fields
        self.text_field_1 = QtWidgets.QLineEdit(self)
        self.text_field_2 = QtWidgets.QLineEdit(self)

        # Create password field
        self.password_field = QtWidgets.QLineEdit(self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_field.show()

        # Create button
        self.button = QtWidgets.QPushButton("Get Password", self)
        self.button.clicked.connect(self.show_password_field)

        # Add fields and button to layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text_field_1)
        self.layout.addWidget(self.text_field_2)
        self.layout.addWidget(self.password_field)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def show_password_field(self):
        self.password_field.show()

app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
