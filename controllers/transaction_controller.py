from models.transaction import Transaction
from utils.file_handler import save_transactions, load_transactions

class TransactionManager:

    def __init__(self):
        self.transactions = load_transactions()

    def add_transaction(self,transaction:Transaction):
        self.transactions.append(transaction)
        save_transactions(self.transactions)

    def get_all_transactions(self) -> list[Transaction]:
        return self.transactions.copy()
    
    def delete_transaction(self, id:str) -> bool:
        for index, transaction in enumerate(self.transactions):
            if transaction.id == id:
                del self.transactions[index]
                save_transactions(self.transactions)
                return True
            
        return False
        
    def get_transaction_summary(self) -> dict:
        total_income = 0
        total_expense = 0
        total_investment = 0

        total_income = sum(t.amount for t in self.transactions  if t.category.lower() == "income")
        total_expense = sum(t.amount for t in self.transactions  if t.category.lower() == "expense")
        total_investment = sum(t.amount for t in self.transactions  if t.category.lower() == "investment")

        return {
            "Total Income" : total_income,
            "Total Expenses" : total_expense,
            "Total Investment": total_investment
            

        }

