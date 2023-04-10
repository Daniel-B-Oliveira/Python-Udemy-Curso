from PySide6.QtWidgets import QPushButton, QGridLayout
from utils import isNumOrDot, isEmpty
from display import Display
from variables import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonGrid(QGridLayout):
    def __init__(self,display:Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.display = display

        self._makeGrid()

    def _makeGrid(self):
        for row_number, row in enumerate(self._gridMask):
            for col_number, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, row_number, col_number)
                button.clicked.connect(self._insertButtonTextDisplay)
                
    def _insertButtonTextDisplay(self, checked):
        self.display.setText('Clicked')
        print(123, checked)