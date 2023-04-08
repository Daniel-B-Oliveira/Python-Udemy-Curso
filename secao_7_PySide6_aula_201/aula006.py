# Trabalhando com classes e heranças no PySide6

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget , QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('My window')

        self.button1 = self.make_button('text one', color='red')
        self.button2 = self.make_button('text two', color='blue')
        self.button3 = self.make_button('text three', color='yellow')
        
        self.button1.clicked.connect(self.second_action_marked)

        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button1, 1, 1, 1, 1) # row , col, row-span, col-span
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        #statusbar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Show menssage')

        #menubar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('first menu')

        self.first_action = self.first_menu.addAction('Fist action')
        self.first_action.triggered.connect(self.message_changer)

        self.second_action = self.first_menu.addAction('Second action')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_action_marked)
        self.second_action.hovered.connect(self.second_action_marked)

    @Slot()
    def message_changer(self):
        self.status_bar.showMessage('Slot executed')

    @Slot()
    def second_action_marked(self):
        print("it's marked?", self.second_action.isChecked())

    def make_button(self,
                    text: str = 'None',
                    font_size: int|float = 30,
                    color: str = 'black',
                    margin: int|float = 0, 
                    padding: int|float = 0,
                ):
        
        button = QPushButton(text)
        button.setStyleSheet(f'font-size: {font_size}px;'\
                             f'color: {color};'\
                             f'margin: {margin}px;'\
                             f'padding: {padding}px;'
                             )
        return button


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    app.exec()