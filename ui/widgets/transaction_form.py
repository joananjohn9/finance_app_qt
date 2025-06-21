from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QComboBox, QPushButton,QMessageBox
from PySide6.QtCore import Slot,Signal
from controllers.transaction_controller import TransactionManager
from models.transaction import Transaction
from logs.logger import logger


TRANSACTION_ITEMS = ["-- Select Category --","Income", "Expense", "Investment"]

class TransactionForm(QWidget):
    transaction_added = Signal()

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
        amount_text = self.amount_input.text()
        category = self.category_input.currentText()
        description = self.description_input.text()

        #Validating transaction
        try:
            amount = float(amount_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Amount must be a number")
            logger.warning("Invalid amount input")
            return #Don't proceed if invalid
        
        if category == "-- Select Category --":
            QMessageBox.warning(self, "Invalid Input", "Please select a valid category.")
            logger.warning("Invalid Category")
            return
        
        if not description.strip():
            QMessageBox.warning(self,"Description cannot be empty")
            logger.warning("Empty Description")
            return
        
        if amount <= 0:
            QMessageBox.warning(self,"Amount should be greater than 0")
            logger.warning("Invalid amount input")
            return
            
        #Making transaction object
        transaction = Transaction(
            amount = amount,
            category = category,
            description = description
        )

        # Save it using controller
        self.controller.add_transaction(transaction)
    

        #Clear fields
        self.amount_input.clear()
        self.category_input.setCurrentIndex(0)
        self.description_input.clear()

        #Print Message
        QMessageBox.information(self,"Success", "Transaction Added Successfully")

        self.transaction_added.emit()



        


    



    
