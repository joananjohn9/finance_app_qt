from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from models.transaction import Transaction
from controllers.transaction_controller import TransactionManager

class Summary_Panel(QWidget):

    def __init__(self,controller, parent=None):
        
        super().__init__(parent)
        self.controller = controller
        self.setup_ui()
    
    def setup_ui(self):
        layout = QHBoxLayout()

    

        self.income_label = QLabel()
        self.income_label.setText("Total Income :")
        self.expense_label = QLabel()
        self.expense_label.setText("Total Expense:")
        self.investment_label = QLabel()
        self.investment_label.setText("Investment Amount")

        self.update_summary()
        

        layout.addWidget(self.income_label)
        layout.addWidget(self.expense_label)
        layout.addWidget(self.investment_label)


        self.setLayout(layout)
    
    def update_summary(self):
        summary_dict = self.controller.get_transaction_summary()
    
        self.income_label.setText(f"Total Income: {summary_dict['Total Income']:.2f} €")
        self.expense_label.setText(f"Total Expense: {summary_dict['Total Expenses']:.2f} €")
        self.investment_label.setText(f"Investment Amount: {summary_dict['Total Investment']:.2f} €")

        