import json
from pathlib import Path
from models.transaction import Transaction

DATA_FILE = Path("data/transaction.json")

def save_transaction(transactions:list[Transaction]) -> None:
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump([t.to_dict for t in transactions], f, indent=4 )

def load_transactions() -> list[Transaction]:
    if not DATA_FILE.exists():
        return[]
    
    with open(DATA_FILE,'r', encoding='utf-8') as file:
        data= json.load(file)
        return [Transaction.from_dict(entry) for entry in data]
    