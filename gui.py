import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import exec_random_list
class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("My App")

      # Widget central para usar layouts
      central_widget = QWidget(self)
      self.setCentralWidget(central_widget)

      # Layout
      layout = QGridLayout()
      central_widget.setLayout(layout)

      # Botão
      button = QPushButton("Aperte-me")
      button.setCheckable(True)
      button.clicked.connect(self.get_filme)
      button.setFixedSize(200, 80)


      # Adiciona o botão ao layout
      layout.addWidget(button, 0, 0)
   def get_filme(self):
      exec_random_list._get_filme()
app= QApplication(sys.argv)

windows = MainWindow()
windows.resize(775, 340)
windows.show()
app.exec()