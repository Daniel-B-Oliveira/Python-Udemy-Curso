from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, *kwargs)

        #Basic layout configurate
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw) 

        #Window title
        self.setWindowTitle('Calculator')


    def adjusFixedSize(self):
        #last thing done
        self.adjustSize()
        self.setFixedSize(self.width(), self.height()+15)

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)