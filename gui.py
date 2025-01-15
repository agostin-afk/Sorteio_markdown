import sys
from PyQt5.QtCore import * #type: ignore
from PyQt5.QtGui import * #type: ignore
from PyQt5.QtWidgets import * #type: ignore
import exec_random_list

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        # Texto
        self.textEdit = QTextEdit("Qual é o filme de hoje...")
        self.textEdit.setFixedSize(400, 50)
        self.textEdit.setReadOnly(True)

        # Widget central para usar layouts
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QGridLayout()
        central_widget.setLayout(layout)

        # Botão
        self.button = QPushButton("Aperte-me", self)
        self.button.clicked.connect(self.get_filme)
        self.button.setFixedSize(150, 80)

        # Adiciona widgets ao layout
        layout.addWidget(self.button, 1, 0)
        layout.addWidget(self.textEdit, 0, 0)

    def get_filme(self):
        # Atualiza o texto do QTextEdit
        novo_texto = exec_random_list._get_filme()  # Obtenha o texto da função
        self.textEdit.setText(novo_texto)  # Atualiza o QTextEdit
        self.button.setText("Novo Sorteio")


# Executa a aplicação
app = QApplication(sys.argv)
windows = MainWindow()
windows.resize(775, 340)
windows.show()
app.exec()


