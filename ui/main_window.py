from PySide6.QtWidgets import  QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QSize
from ui.widgets.transaction_form import TransactionForm
from ui.widgets.transaction_list import TransactionTable
from ui.widgets.summary_panel import Summary_Panel
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
        self.transaction_form.transaction_added.connect(self.transaction_table.load_transaction) #auto refreshing  transaction list
        self.summary_panel = Summary_Panel(self.controller)
        self.transaction_form.transaction_added.connect(self.summary_panel.update_summary) #auto refreshing summary panel
        layout = QVBoxLayout()
        layout.addWidget(self.transaction_form)
        layout.addWidget(self.transaction_table)
        layout.addWidget(self.summary_panel)
        central_widget.setLayout(layout)
 