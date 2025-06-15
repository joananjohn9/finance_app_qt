from datetime import datetime
from dataclasses import dataclass, asdict, field
import uuid


@dataclass
class Transaction:
    amount:float
    category:str
    description : str
    date : str = datetime.today().strftime('%Y-%m-%d')
    id : str = field(default_factory=lambda: uuid.uuid4().hex)

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            amount = data["amount"],
            category = data["category"],
            description = data["description"],
            date = data.get('date', datetime.today().strftime('%Y-%m-%d')),
            id = data.get("id", uuid.uuid4().hex)
        )

