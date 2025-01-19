import sys
from PyQt5.QtCore import * #type: ignore
from PyQt5.QtGui import * #type: ignore
from PyQt5.QtWidgets import * #type: ignore
import exec_random_list
caminho = "C:\\Users\\agost\\OneDrive\\Documentos\\Obsidian Vault\\Filmes - insta_1.md"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        # Texto
        self.textEdit = QTextEdit("Qual é o filme de hoje...")
        self.textEdit.setFixedSize(400, 60)
        self.textEdit.setReadOnly(True)

        # Widget central para usar layouts
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QGridLayout()
        central_widget.setLayout(layout)

        # Botão
        self.button = QPushButton("Sorteio", self)
        self.button.clicked.connect(self.get_filme)
        self.button.setFixedSize(150, 80)
        self.button_assistir = QPushButton("Selecionar filme", self)
        self.button_assistir.clicked.connect(self.set_filme)
        self.button_assistir.setFixedSize(150, 80)
        self.button_assistiu = QPushButton("Já assisti", self)
        self.button_assistiu.clicked.connect(self.remove_filme)
        self.button_assistiu.setFixedSize(150, 80)

        # Adiciona widgets ao layout
        layout.addWidget(self.textEdit, 0, 1, 1, 3)  
        layout.addWidget(self.button, 1, 0)          
        layout.addWidget(self.button_assistir, 1, 2) 
        layout.addWidget(self.button_assistiu, 1, 4) 

        layout.setColumnStretch(0, 1) 
        # layout.setColumnStretch(1, 1)
        # layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 1)  

    def get_filme(self):
        # Atualiza o texto do QTextEdit
        novo_texto = exec_random_list.test.main()  # Obtenha o texto da função
        self.textEdit.setText(novo_texto)  # Atualiza o QTextEdit
        self.button.setText("Novo Sorteio")
    def set_filme(self):
        exec_random_list.test.save_filme() 
        aviso = f"filme selecionado: {exec_random_list.test.get_filme()}"
        self.textEdit.setText(aviso)
    def remove_filme(self):
        exec_random_list.test.remove_filme()
        aviso = f"Selecione um novo filme para assistir!"
        self.textEdit.setText(aviso)

# Executa a aplicação
app = QApplication(sys.argv)
windows = MainWindow()
windows.resize(775, 340)
windows.show()
app.exec()


