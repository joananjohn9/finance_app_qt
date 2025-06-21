# 💸 FinBuddy – Personal Finance Tracker

FinBuddy is a lightweight desktop finance tracker built with PySide6 (Qt for Python).  
It helps you record, manage, and visualize your income, expenses, and investments.

---

## 🚀 Features

- ✅ Add new transactions with category, amount, and description
- ✅ View all transactions in a table
- ✅ Delete transactions with a single click
- ✅ Real-time summary of totals
- ✅ Input validation and error handling
- ✅ Logging to `logs/app.log` for debugging

---

## 📸 Screenshot

> _Add a screenshot here if you have one_

---

## 🛠️ Technologies Used

- [PySide6](https://doc.qt.io/qtforpython/) – UI Framework
- Python 3.10+
- JSON – For local data storage
- Built-in logging module

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/finance_app.git
cd finance_app
```

### 2. Create and activate a virtual environment
```bash
python -m venv myenv
source myenv/bin/activate  # on Linux/macOS
myenv\Scripts\activate     # on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python main.py
```

---

## 📁 Project Structure

```
finance_app/
├── main.py
├── controllers/
│   └── transaction_controller.py
├── models/
│   └── transaction.py
├── ui/
│   ├── main_window.py
│   └── widgets/
│       ├── transaction_form.py
│       ├── transaction_list.py
│       └── summary_panel.py
├── utils/
│   └── file_handler.py
├── logs/
│   └── logger.py
├── data/
│   └── transaction.json
```

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

Joanan John Jacob  
[Your GitHub/LinkedIn/email]
