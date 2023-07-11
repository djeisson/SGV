""""
*criar ambiente virtual
python -m venv venv

*ativar o ambiente virtual
venv\scripts\activate

*caso der um erro abrir console do powershel e digitar
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
-apos isso digitar "S" e clicar no botao enter

*para instalar o PySide6 foi nescessario
pip install Pyside6
*para instalar o qt desygner foi nescessario
pip install PyQt5 PyQt5 --tools

*traduzir o .ui
Pyside6-uic gerar_ticket.ui -o gerar_ticket.ui.py


import sys //Importar sistema
from PySide6.QtWidgets import QApplication, QDialog
from PyQt5 import *
from PySide6.QtWidgets import QMainWindow

from main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
"""