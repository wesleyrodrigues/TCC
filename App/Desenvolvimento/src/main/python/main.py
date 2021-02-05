from PyQt5 import QtGui
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QWidget
from os import environ
from mainUi import Ui_MainWindow
from dialogpassword import Ui_Dialog
from contasDB import Contas
from criptografia import Cript
import sys


class VoltarParaTelaInicial(QDialog):
    """
        TODO melhorar descrição
        Descrição:
            Esta clase será chamada por meio do botão btn_sair2,
            que irá aparecer nas telas de atividades, ela é uma tela
            de Dialog para poder voltar para tela inicial.

        Parâmetros:
            QDialog
                Tela do tipo Dialogo
    """

    def __init__(self) -> None:
        super(VoltarParaTelaInicial, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lerror.hide()
        self.ui.label_2.setPixmap(QtGui.QPixmap(
            "src/main/app_imagens/dialog1.png"))

    # Abre caixa de dialogo para voltar para tela inicial
    def open_dialog(self):
        """ Descrição: 
            Executa a tela de Diálogo
        """
        self.exec()

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
        self.stack.setCurrentWidget(
            self.stack.findChild(QWidget, "tela_inicial"))
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.btnProfessor
        self.pular = 1
        self.contas = Contas()
        self.contas.createDB()

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

    def get_text(self, nome_line="tudo"):
        nomes_dict = {
            "nome_aluno": str(self.ui.input_nome_aluno.text()),
            "sobrenome_aluno": str(self.ui.input_sobrenome.text()),
            "senha": str(self.ui.input_senha.text()),
            "conf_senha": str(self.ui.input_conf_senha.text()),
            "nome_professor": str(self.ui.input_nome_professor.text()),
            "email_professor": str(self.ui.input_email.text()),
            "conf_email": str(self.ui.input_conf_email.text())
        }

        if (nome_line == "tudo"):
            return nomes_dict
        else:
            return nomes_dict[nome_line]

    def input_conta(self):
        texto_lines = self.get_text()
        message = ""
        if(texto_lines["senha"] != texto_lines["conf_senha"]):
            message += "As senhas não são iguais. Tente novamente.\n"
        if(texto_lines["email_professor"] != texto_lines["conf_email"]):
            message += "Os emails não são iguais. Tente novamente.\n"


        campos = True
        for i in texto_lines:
            if(not(texto_lines[i])):
                message += "Verifique se todos dados estão preenchidos"
                campos = False
                break

        self.ui.lverifica_senha_email.setText(message)
        if(not(message) and campos):
            print("adicionado")
            self.contas.add_conta(texto_lines)

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
    alfa_edu.ui.btn_tela_cadastro.clicked.connect(
        lambda: alfa_edu.mudar_tela("tela_cadastro"))
    alfa_edu.ui.btn_sair2.clicked.connect(lambda: volt_p_t_i.open_dialog())
    alfa_edu.ui.btn_pular.clicked.connect(lambda: alfa_edu.pularfun())
    alfa_edu.ui.btn_cadastrar.clicked.connect(lambda: alfa_edu.input_conta())
    volt_p_t_i.ui.btnOk.clicked.connect(
        lambda: volt_p_t_i.verifica_password(alfa_edu))


if __name__ == '__main__':
    suppress_qt_warnings()

    app = QApplication(sys.argv)

    alfa_edu_app = AlfaEdu()
    # app.setStyleSheet(alfa_edu_app.return_stylesheet())

    voltar_para_tela_inicial = VoltarParaTelaInicial()

    buttons(alfa_edu_app, voltar_para_tela_inicial)

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    alfa_edu_app.showFullScreen()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
