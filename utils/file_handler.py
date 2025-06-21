import json
from pathlib import Path
from models.transaction import Transaction
from logs.logger import logger

DATA_FILE = Path("data/transaction.json")

def save_transactions(transactions:list[Transaction]) -> None:
    try :
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump([t.to_dict() for t in transactions], file, indent=4 )
    except (OSError, TypeError) as e:
        logger.error(f"Failed to save data: {e}")


def load_transactions() -> list[Transaction]:
    if not DATA_FILE.exists():
        return[]
    
    try:
        with open(DATA_FILE,'r', encoding='utf-8') as file:
            data= json.load(file)
            return [Transaction.from_dict(entry) for entry in data]
        
    except(OSError, json.JSONDecodeError) as e:
        logger.error(f"Failed to load transactions: {e}")
        return[]
    

