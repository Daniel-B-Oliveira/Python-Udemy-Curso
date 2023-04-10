import sys

from main_window import MainWindow
from display import Display
from styles import setupTheme
from info import Info
from buttons import Button, ButtonGrid

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    #Define a icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    info = Info('Operation')
    window.addWidgetToVLayout(info)

    #Display
    display = Display()
    window.addWidgetToVLayout(display)

    #Grid
    buttonsGrid= ButtonGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # window.setWindowTitle('Calculator')
    window.adjusFixedSize()
    window.show()
    app.exec()