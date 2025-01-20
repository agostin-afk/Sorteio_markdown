import sys
from PyQt5.QtWidgets import *  # type: ignore
import exec_random_list

film = exec_random_list.Filme()
caminho = film.caminho

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        # Aplica estilo geral à janela principal
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #FFDEE9, stop: 1 #B5FFFC
                );
            }
        """)

        # Texto (QTextEdit)
        self.textEdit = QTextEdit("Qual é o filme de hoje...")
        self.textEdit.setFixedHeight(75)  # Define a altura inicial para 75
        self.textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("""
            QTextEdit {
                font-size: 18px;
                color: #333333;
                background-color: #F9F9F9;
                border: 1px solid #CCCCCC;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        self.textEdit.textChanged.connect(self.adjust_text_edit_height)

        # Widget central para usar layouts
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QGridLayout()
        central_widget.setLayout(layout)

        # Botões
        self.button = QPushButton("Sorteio", self)
        self.button.clicked.connect(self.get_filme)
        self.button.setMinimumSize(150, 80)
        self.button.setStyleSheet(self.button_style())

        self.button_assistir = QPushButton("Selecionar filme", self)
        self.button_assistir.clicked.connect(self.set_filme)
        self.button_assistir.setMinimumSize(150, 80)
        self.button_assistir.setStyleSheet(self.button_style())

        self.button_assistiu = QPushButton("Já assisti", self)
        self.button_assistiu.clicked.connect(self.remove_filme)
        self.button_assistiu.setMinimumSize(150, 80)
        self.button_assistiu.setStyleSheet(self.button_style())

        # Adiciona widgets ao layout
        layout.addWidget(self.textEdit, 0, 1, 1, 3)
        layout.addWidget(self.button, 1, 0)
        layout.addWidget(self.button_assistir, 1, 2)
        layout.addWidget(self.button_assistiu, 1, 4)

        # Ajusta espaçamento e alinhamento
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 1)

    def button_style(self):
        """Define o estilo dos botões."""
        return """
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #007BFF;
                border: 1px solid #0056b3;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #003d80;
            }
        """

    def adjust_text_edit_height(self):
        """Ajusta a altura do QTextEdit com base no conteúdo."""
        document_height = self.textEdit.document().size().height() # type: ignore
        self.textEdit.setFixedHeight(max(75, int(document_height) + 30))

    def get_filme(self):
        try:
            novo_texto = film.main()  # Obtenha o texto da função
            self.textEdit.setText(novo_texto)  # Atualiza o QTextEdit
            self.button.setText("Novo Sorteio")
        except Exception as e:
            self.textEdit.setText(f"Erro ao sortear o filme: {str(e)}")

    def set_filme(self):
        try:
            film.save_filme() 
            aviso = f"Filme selecionado: {film.get_filme()}"
            self.textEdit.setText(aviso)
        except Exception as e:
            self.textEdit.setText(f"Erro ao selecionar o filme: {str(e)}")

    def remove_filme(self):
        try:
            film.remove_filme()
            aviso = f"Selecione um novo filme para assistir!"
            self.textEdit.setText(aviso)
            self.button.setText("Novo Sorteio")
        except Exception as e:
            self.textEdit.setText(f"Erro ao remover o filme: {str(e)}")

# Executa a aplicação
app = QApplication(sys.argv)
windows = MainWindow()
windows.resize(775, 340)
windows.show()
app.exec()
