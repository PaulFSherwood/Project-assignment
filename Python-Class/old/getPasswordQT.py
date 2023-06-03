from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        # create the password label
        password_label = QLabel("Password:")
        
        # create the password line edit
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        
        # create the OK button
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        
        # layout the widgets
        layout = QVBoxLayout()
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(ok_button)
        
        self.setLayout(layout)
        self.setWindowTitle("Password")

app = QApplication([])
dialog = PasswordDialog()
result = dialog.exec()

if result == QDialog.Accepted:
    password = dialog.password_edit.text()
    # use the password for ssh

app.exit()
