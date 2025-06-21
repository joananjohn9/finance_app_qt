from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QComboBox, QPushButton
from PySide6.QtCore import Slots
from controllers.transaction_controller import TransactionManager
from models.transaction import Transaction


TRANSACTION_ITEMS = ["Income", "Expenses", "Investment"]

class TransactionForm(QWidget):
    def __init__(self,controller,parent=None):

        super().__init__(parent)
        self.controller = controller
        self.setup_ui()


    def setup_ui(self):
        layout = QFormLayout()

        
        self.amount_input = QLineEdit()
        self.category_input = QComboBox() # Making the combobox
        self.description_input = QLineEdit()
        self.category_input.addItems(TRANSACTION_ITEMS) # Populating the category inputs
        self.submit_button = QPushButton("Submit")

        layout.addRow("Amount", self.amount_input ) # Adding the amount 
        layout.addRow("Category", self.category_input) # Adding Category 
        layout.addRow("Description", self.description_input) #Adding description
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        self.submit_button.clicked.connect(self.handle_transaction)

    @Slot()
    def handle_transaction(self):

        #Getting inputs
        amount = self.amount_input.text()
        category = self.category_input.text()
        description = self.description_input.text()

        


    



    
