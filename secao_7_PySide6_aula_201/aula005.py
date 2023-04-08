# o básico sobre signal e solts (eventos e documentações)
import sys

from PySide6.QtCore import Slot
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

@Slot()
def first_slot_example(status_bar):
    status_bar.showMessage('Slot executed')

@Slot()
def second_slot_example(checked):
    print("it's marked?", checked)

@Slot()
def third_slot_example(action):
    def inner():
        second_slot_example(action.isChecked())
    return inner


#menubar
menu = window.menuBar()
first_menu = menu.addMenu('first menu')

first_action = first_menu.addAction('Fist action')
first_action.triggered.connect(
    lambda: first_slot_example(status_bar)
)

second_action = first_menu.addAction('Second action')
second_action.setCheckable(True)
second_action.toggled.connect(second_slot_example)
second_action.hovered.connect(third_slot_example(second_action))
# second_action.hovered.connect(lambda a ='test': print(a))

button1.clicked.connect(third_slot_example(second_action))

window.show()
app.exec()