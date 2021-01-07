from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication
from os import environ
from mainUi import Ui_MainWindow

import sys

#
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


# Stylesheet para adicionar imagem de fundo da aplicação
stylesheet = """
    QMainWindow {
        background-image: url("MainWindow.png");
	border-image: url("MainWindow.png") 0 0 0 0 stretch stretch; 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == '__main__':
    suppress_qt_warnings()

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)

    window = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
