from PySide6.QtWidgets import  QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QSize
from ui.widgets.transaction_form import TransactionForm
from ui.widgets.transaction_list import TransactionTable
from controllers.transaction_controller import TransactionManager


class MainWindow(QMainWindow):
    
    def __init__(self,controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("Fin Buddy")
        self.setFixedSize(QSize(800,600))
        self.setup_ui()


    def setup_ui(self):
        central_widget = QWidget()

        self.setCentralWidget(central_widget)
        self.transaction_form = TransactionForm(self.controller) 
        self.transaction_table = TransactionTable(self.controller)
        self.transaction_form.transaction_added.connect(self.transaction_table.load_transaction)
        layout = QVBoxLayout()
        layout.addWidget(self.transaction_form)
        layout.addWidget(self.transaction_table)
        central_widget.setLayout(layout)
 