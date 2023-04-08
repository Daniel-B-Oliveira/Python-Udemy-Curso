# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget , QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout


app = QApplication(sys.argv)

window = QMainWindow()
central_widget = QWidget()

window.setCentralWidget(central_widget)
window.setWindowTitle('My window')

button1 = QPushButton('first button text')
button1.setStyleSheet('font-size: 30px; color: red; margin: 5px; padding:10px')

button2 = QPushButton('second button text')
button2.setStyleSheet('font-size: 30px; color: blue; margin: 5px; padding:10px')

button3 = QPushButton('third button text')
button3.setStyleSheet('font-size: 30px; color: yellow; margin: 5px; padding:10px')

# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(button1, 1, 1, 1, 1) # row , col, row-span, col-span
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

#statusbar
status_bar = window.statusBar()
status_bar.showMessage('Show menssage')

#menubar
def slot_example(status_bar):
    status_bar.showMessage('Slot executed')

menu = window.menuBar()
first_menu = menu.addMenu('first menu')
first_action = first_menu.addAction('Fist action')
first_action.triggered.connect(
    lambda : slot_example(status_bar)
    )

window.show()
app.exec()