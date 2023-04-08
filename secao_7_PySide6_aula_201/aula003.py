# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget 
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout


app = QApplication(sys.argv)

button1 = QPushButton('first button text')
button1.setStyleSheet('font-size: 40px; color: red; margin: 5px; padding:10px')

button2 = QPushButton('second button text')
button2.setStyleSheet('font-size: 40px; color: blue; margin: 5px; padding:10px')

button3 = QPushButton('third button text')
button3.setStyleSheet('font-size: 40px; color: yellow; margin: 5px; padding:10px')

# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout()
layout.addWidget(button1, 1, 1, 1, 1) # row , col, row-span, col-span
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

central_widget = QWidget()
central_widget.setLayout(layout)
central_widget.show()
 
app.exec()