from PySide6.QtWidgets import QWidget, QTableWidget, QVBoxLayout,QSizePolicy,QHeaderView,QTableWidgetItem
from models.transaction import Transaction
from controllers.transaction_controller import TransactionManager

LABELS = ["Date", "Id", "Amount","Category","Description"]

class TransactionTable(QWidget):
    def __init__(self,controller,parent=None):

        #Initializing parent class
        super().__init__(parent)
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.transaction_table = QTableWidget()
        self.transaction_table.setColumnCount(5) # For Date, id, amount, category,description 
        self.transaction_table.setHorizontalHeaderLabels(LABELS)

        layout.addWidget(self.transaction_table)
        self.transaction_table.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setLayout(layout)
        self.transaction_table.horizontalHeader().setStretchLastSection(True)
        self.transaction_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_transaction()

    def load_transaction(self):
        #clear the table
        self.transaction_table.setRowCount(0)

        #Get all transaction
        transactions = self.controller.get_all_transactions()
        
        #Looping through transaction
        for index,transaction in enumerate(transactions):
            self.transaction_table.insertRow(index)
            self.transaction_table.setItem(index,0,QTableWidgetItem(transaction.date))
            self.transaction_table.setItem(index,1,QTableWidgetItem(transaction.id))
            self.transaction_table.setItem(index,2,QTableWidgetItem(str(transaction.amount)))
            self.transaction_table.setItem(index,3,QTableWidgetItem(transaction.category))
            self.transaction_table.setItem(index,4,QTableWidgetItem(transaction.description))

                                           


        

