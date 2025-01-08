from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QMessageBox, QMainWindow
import os, sys

from GUI.ui_login import Ui_Dialog
from GUI.ui_principal import Ui_MainWindow


class tela_principal(QMainWindow):
    def __init__(self, *args, **kwargsargs):
        super(tela_principal, self).__init__(*args, **kwargsargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



class simpleApp(QDialog):
    def __init__(self, *args, **kwargsargs):
        super(simpleApp, self).__init__(*args, **kwargsargs)
        self.login = Ui_Dialog()
        self.login.setupUi(self)
        self.login.pushButton.clicked.connect(self.janela_principal)
        self.login.pushButton_2.clicked.connect(self.close_login_window)


    def janela_principal(self):
        self.window = tela_principal()
        self.window.show()
        # QMessageBox.information(QMessageBox(), "Mensagem", "Conexão ativa")

    def close_login_window(self):
        """Fecha a janela de login."""
        self.close()  # Método embutido do QMainWindow para fechar a janela



# Inicialização da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = simpleApp()
    window.show()  # Exibe a janela
    sys.exit(app.exec())