from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot

import math

from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber
from variables import MEDIUM_FONT_SIZE

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info

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
    def __init__(self,display:'Display', info:'Info', window: 'MainWindow', *args, **kwargs
    )-> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.initialInfo = info.text()

        self.window = window

        self._equation = ''
        self.equation = self.initialInfo    # Setter

        self._leftTerm = None
        self._rightTerm = None
        self._op = None

        self._makeGrid()

    @property   #getter
    def equation(self):
        return self._equation
    
    @equation.setter    #setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.equalPressed.connect(self._equal)
        self.display.deletePressed.connect(self._backSpace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOperator)

        for rowNumber, row in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, colNumber)
                slot = self._makeSlot(self._insertToDisplay,buttonText)
                self._connectButtonCLicked(button, slot)

    def _connectButtonCLicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        if text == 'C':
            self._connectButtonCLicked(button, self._clear) 

        if text == 'D':
            self._connectButtonCLicked(button,self.display.backspace)

        if text == 'N':
            self._connectButtonCLicked(button, self._invertNumber)

        if text in '+-/*^':
            self._connectButtonCLicked(
                button,
                self._makeSlot(self._configLeftOperator, text)
            )
        
        if text == '=':
            self._connectButtonCLicked(button,self._equal)

        
    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        self.display.setFocus()
        return realSlot
    
    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self.display.setFocus()
            return
        
        number = convertToNumber(displayText) * -1

        self.display.setText(str(number))
        self.display.setFocus()

    
    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            self.display.setFocus()
            return
        
        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._leftTerm = None
        self._rightTerm = None
        self._op = None
        self.equation = self.initialInfo
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOperator(self,text):
        displayText = self.display.text()   # leftNumber
        self.display.clear()

        # if button has clicked with nothing in left term
        if not isValidNumber(displayText) and self._leftTerm is None:
            self._showError('Nothing to put on the left value')
            self.display.setFocus()
            return
        
        # if there's anything in the left term. 
        # Wait for a number in the right term

        if self._leftTerm is None:
            self._leftTerm = convertToNumber(displayText)

        self._op = text
        self.equation = f'{self._leftTerm} {self._op} ??'
        self.display.setFocus()

    @Slot()
    def _equal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._leftTerm is None:
            self._showError('Nothing in right side')
            self.display.setFocus()
            return

        self._rightTerm = convertToNumber(displayText)
        self.equation = f'{self._leftTerm} {self._op} {self._rightTerm}'
        result = 'error'
        try:
            if '^' in self.equation and isinstance(self._leftTerm, int | float):
                result = math.pow(self._leftTerm, self._rightTerm) #type:ignore
                result = convertToNumber(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Zero divion error')
        except OverflowError:
            self._showError('Over flow error')
        except:
            self._clear()
            self._showError('Unknown expression')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._leftTerm = result
        self._rightTerm = None

        if result == 'error':
            self._leftTerm = None
        
        self.display.setFocus()
            
    @Slot()
    def _backSpace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()