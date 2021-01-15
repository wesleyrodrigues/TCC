from PyQt5 import QtGui
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QWidget
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
        self.ui.label_2.setPixmap(QtGui.QPixmap("src/main/app_imagens/dialog1.png"))
    
    # Abre caixa de dialogo para voltar para tela inicial
    def open_dialog(self):
        self.exec_()

    # TODO mudar depois para melhorar
    # verifica a senha do professor ou pai do aluno para poder sair das atividades
    def verifica_password(self, alfa_edu):
        text = str(self.ui.lineEdit.text())
        
        # TODO buscar senha no BD, pedi senha apenas em atividades e feedback.
        if(text == "123"):
            alfa_edu.mudar_tela("tela_inicial")
            self.ui.lineEdit.clear()
            self.ui.lerror.hide()
            self.accept()
        else:
            self.ui.lineEdit.clear()
            self.ui.lerror.show()



class AlfaEdu(QMainWindow):
    def __init__(self):
        super(AlfaEdu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stack = self.ui.stackedWidget
        self.ui.btn_sair2.hide()

        self.background_imagem = "MainWindow.png"
        self.background_cor = "#ADD8E6"
        self.stack.setCurrentWidget(self.stack.findChild(QWidget, "tela_inicial"))
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.btnProfessor
        self.pular = 1
    
    def pularfun(self):
        self.stack.setCurrentIndex(self.pular)
        self.pular += 1
        if(self.pular == self.stack.count()):
            self.pular = 0

    def hide_button(self, stack_name):
        if(stack_name == "tela_inicial"):
            self.ui.btn_sair2.hide()
        else:
            self.ui.btn_sair2.show()

    def mudar_tela(self, stack_name):
        # TODO Melhorar 
        stack_passado = self.stack.findChild(QWidget, stack_name)
        self.stack.setCurrentWidget(stack_passado)
        # self.stack.setCurrentIndex(index)
        self.hide_button(stack_name)


    # TODO melhorar depois
    def return_stylesheet(self):

        return """
            QMainWindow {
                background-image: url("src/main/app_imagens/%s");
                background-color: "%s";
            border-image: url("src/main/app_imagens/%s") 0 0 0 0 stretch stretch; 
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
    alfa_edu.ui.btn_tela_cadastro.clicked.connect(lambda: alfa_edu.mudar_tela("tela_cadastro"))
    alfa_edu.ui.btn_sair2.clicked.connect(lambda: volt_p_t_i.open_dialog())
    alfa_edu.ui.btn_pular.clicked.connect(lambda: alfa_edu.pularfun())
    
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
