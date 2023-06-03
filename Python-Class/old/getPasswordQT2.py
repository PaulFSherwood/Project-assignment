from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
import paramiko

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

    def accept(self):
        password = self.password_edit.text()
        print("The password entered is:", password)


        hostname = '192.168.56.109'
        username = 'Administrator'
        input_value = 10
        id_name = 4624

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname=hostname, username=username, password=password)

        command = "powershell.exe Get-WinEvent -FilterHashtable @{{logname='security'; id={}}} -MaxEvents {}".format(id_name, input_value)
        stdin, stdout, stderr = ssh.exec_command(command)


        result = stdout.read().decode()
        lines = result.split("\n")
        for line in lines:
            if line.strip():
                line_split = line.strip().split(" ", maxsplit=1)
                print(line_split[-1])
        ssh.close()



        super().accept()

app = QApplication([])
dialog = PasswordDialog()
result = dialog.exec()

app.exit()






