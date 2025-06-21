import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from controllers.transaction_controller import TransactionManager


if __name__ =="__main__":
    app = QApplication(sys.argv)
    controller = TransactionManager()
    window = MainWindow(controller)
    window.show()

    sys.exit(app.exec())