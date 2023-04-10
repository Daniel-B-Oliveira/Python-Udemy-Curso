from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal

from utils import isEmpty, isNumOrDot

class Display(QLineEdit):
    equalPressed = Signal()
    deletePressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text= event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter =  key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete =  key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
            KEYS.Key_P,
        ]
        
        if isEnter:
            self.equalPressed.emit()
            return event.ignore()
            
        if isDelete:
            self.deletePressed.emit()
            return event.ignore()
            
        if isEsc:
            self.clearPressed.emit()
            return event.ignore()
        
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()
        
        # keys exec only with text:
        if isEmpty(text):
            return event.ignore()


        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
