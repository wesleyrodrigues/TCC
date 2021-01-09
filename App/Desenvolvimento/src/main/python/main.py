from PyQt5 import QtGui
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from os import environ
from mainUi import Ui_MainWindow
from dialogpassword import Ui_Dialog

import sys


class VoltarParaTelaInicial(QDialog):
    def __init__(self):
        super(VoltarParaTelaInicial, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lerror.hide()
    
    def open_dialog(self):
        # voltar_para_tela_inicial = VoltarParaTelaInicial()
        self.exec_()

    # TODO mudar depois para melhorar
    def verifica_password(self, alfa_edu):
        text = str(self.ui.lineEdit.text())
        
        # TODO buscar senha no BD.
        if(text == "123"):
            alfa_edu.mudar_pagina(0)
            self.accept()
        else:
            self.ui.lerror.show()
            print("senha errada")



class AlfaEdu(QMainWindow):
    def __init__(self):
        super(AlfaEdu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stack = self.ui.stackedWidget
        self.ui.btnsair2.hide()

        self.background_imagem = "MainWindow.png"
        self.background_cor = "#ADD8E6"
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.btnProfessor

    def hide_button(self, index):
        if(index == 0):
            self.ui.btnsair2.hide()
        else:
            self.ui.btnsair2.show()

    def mudar_pagina(self, index):
        self.stack.setCurrentIndex(index)
        self.hide_button(index)


    # TODO melhorar depois
    def return_stylesheet(self):

        return """
            QMainWindow {
                background-image: url("%s");
                background-color: "%s";
            border-image: url("%s") 0 0 0 0 stretch stretch; 
                background-repeat: no-repeat; 
                background-position: center;
            }""" % (
            self.background_imagem,
            self.background_cor,
            self.background_imagem
        )


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


# TODO tentar colocar dentro da class depois
def buttons(alfa_edu, volt_p_t_i):
    alfa_edu.ui.btnProfessor.clicked.connect(lambda: alfa_edu.mudar_pagina(1))
    alfa_edu.ui.btnsair2.clicked.connect(lambda: volt_p_t_i.open_dialog())
    
    volt_p_t_i.ui.btnOk.clicked.connect(lambda: volt_p_t_i.verifica_password(alfa_edu))



if __name__ == '__main__':
    suppress_qt_warnings()

    app = QApplication(sys.argv)

    alfa_edu_app = AlfaEdu()
    app.setStyleSheet(alfa_edu_app.return_stylesheet())

    voltar_para_tela_inicial = VoltarParaTelaInicial()

    buttons(alfa_edu_app, voltar_para_tela_inicial)

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    alfa_edu_app.showFullScreen()


    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
