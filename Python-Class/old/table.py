from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_2 = QWidget()
        self.tab_2_layout = QVBoxLayout()
        self.tab_2.setLayout(self.tab_2_layout)
        
        # Create a QTableWidget with 2 columns and 1 row
        table = QTableWidget(1, 2)

        # Set the variables
        var1 = "Node Type"
        var2 = "Hybrid"

        # Insert the variables in the first and second column respectively
        table.setItem(0, 0, QTableWidgetItem(var1))
        table.setItem(0, 1, QTableWidgetItem(var2))

        self.tab_2_layout.addWidget(table)

if __name__ == '__main__':
    app = QApplication([])
    ex = MyApp()
    ex.show()
    app.exec()