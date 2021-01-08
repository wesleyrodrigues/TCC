from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication
from os import environ
from mainUi import Ui_MainWindow

import sys


class AlfaEdu(QMainWindow):
    def __init__(self):
        super(AlfaEdu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stack = self.ui.stackedWidget
        self.ui.btnsair2.hide()
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.btnProfessor
    
    def hide_buttons(self, index):
        if(index == 0):
            self.ui.btnsair2.hide()
        else:
            self.ui.btnsair2.show()
    
    def mudar_pagina(self, index):
        self.stack.setCurrentIndex(index)
        self.hide_buttons(index)


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def returnstylesheet():
    # TODO acessar banco de dados salvar, stylesheet no mesmo.
    
    return """
        QMainWindow {
            background-image: url("MainWindow.png");
        border-image: url("MainWindow.png") 0 0 0 0 stretch stretch; 
            background-repeat: no-repeat; 
            background-position: center;
        }
    """


def buttons(alfa_edu):
    alfa_edu.ui.btnProfessor.clicked.connect(lambda: alfa_edu.mudar_pagina(1))
    alfa_edu.ui.btnsair2.clicked.connect(lambda: alfa_edu.mudar_pagina(0))


if __name__ == '__main__':
    suppress_qt_warnings()
    
    app = QApplication(sys.argv)
    app.setStyleSheet(returnstylesheet())
    
    alfa_edu_app = AlfaEdu()
    buttons(alfa_edu_app)

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    

    alfa_edu_app.showFullScreen()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
