from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QWidget
from os import environ
from mainUi import Ui_MainWindow
from contasDB import Contas
from criptografia import Cript

import sys

class AlfaEdu(QMainWindow):
    def __init__(self):
        super(AlfaEdu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stack = self.ui.stackedWidget
        self.ui.btn_voltar_tela_inicial.hide()

        self.background_imagem = "MainWindow.png"
        self.background_cor = "#add8e6"
        self.stack.setCurrentWidget(
            self.stack.findChild(QWidget, "tela_inicial"))
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.btnProfessor
        self.pular = 1
        self.contas = Contas()
        self.contas.createDB()
        self.ui.cb_nome_aluno.addItems(self.contas.seleciona_nomes())
        self.usuario = ""
        self.senha_cript = ""

    def pularfun(self):
        self.stack.setCurrentIndex(self.pular)
        self.pular += 1
        if(self.pular == self.stack.count()):
            self.pular = 0

    def hide_widgets(self, stack_name):
        if(stack_name == "tela_inicial"):
            self.ui.btn_voltar_tela_inicial.hide()
        else:
            self.ui.btn_voltar_tela_inicial.show()
            self.ui.lverifica_senha.setText("")
            self.ui.lverifica_email.setText("")
            self.ui.lcampos.setText("")
            self.ui.lverifica_nome.setText("")
            self.ui.lerro_login.setText("")
            self.ui.input_senha_login.setText("")

    def mudar_tela(self, stack_name):
        # TODO Melhorar
        stack_passado = self.stack.findChild(QWidget, stack_name)
        self.stack.setCurrentWidget(stack_passado)
        # self.stack.setCurrentIndex(index)
        self.hide_widgets(stack_name)

    def get_text(self, nome_line="tudo"):
        nomes_dict = {
            "nome_aluno": str(self.ui.input_nome_aluno.text()),
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

    def login(self):
        self.ui.lerro_login.setText("")
        nome = str(self.ui.cb_nome_aluno.currentText())
        senha = str(self.ui.input_senha_login.text())
        senha_cript = self.contas.seleciona_usuario_por_nome(nome)["senha"]
        retorno = Cript.verifica_usuario_e_senha(senha_cript, senha)

        if(retorno):
            self.mudar_tela("tela_escolher_atividades")
            self.usuario = nome
            self.senha = senha
        else:
            self.ui.lerro_login.setText("Senha errada digite novamente!!")

    def input_conta(self):
        texto_lines = self.get_text()

        message = True
        if(texto_lines["senha"] != texto_lines["conf_senha"]):
            msg = "As senhas não são iguais. Tente novamente.\n"
            self.ui.lverifica_senha.setText(msg)
            message = False
        if(texto_lines["email_professor"] != texto_lines["conf_email"]):
            msg = "Os emails não são iguais. Tente novamente.\n"
            self.ui.lverifica_email.setText(msg)
            message = False

        for i in texto_lines:
            if(not(texto_lines[i])):
                msg = "Verifique se todos dados estão preenchidos\n"
                self.ui.lcampos.setText(msg)
                message = False
                break

        for count in range(self.ui.cb_nome_aluno.count()):
            if(texto_lines["nome_aluno"] == self.ui.cb_nome_aluno.itemText(count)):
                msg = "Nome do(a) aluno(a), já cadastrado\n"
                self.ui.lverifica_nome.setText(msg)
                message = False
                break

        if(message):
            print("adicionado")
            # TODO criptografia não funciona
            texto_lines["senha"] = Cript.criptografa_senha(texto_lines["senha"])
            t = self.contas.add_conta(texto_lines)
            if(t):
                self.ui.cb_nome_aluno.addItem(texto_lines["nome_aluno"])
                self.mudar_tela("tela_escolher_atividades")
                self.usuario = texto_lines["nome_aluno"]
                self.senha = texto_lines["senha"]
                self.ui.lnome_aluno_logado.setText(self.usuario)
            else:
                msg = "Dados não salvos erro Banco de dados\n"
                self.ui.lcampos.setText(msg)

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
def buttons(alfa_edu):
    # telas
    alfa_edu.ui.btn_tela_cadastro.clicked.connect(
        lambda: alfa_edu.mudar_tela("tela_cadastro"))
    alfa_edu.ui.btn_tela_login.clicked.connect(
        lambda: alfa_edu.mudar_tela("tela_login"))
    alfa_edu.ui.btn_login.clicked.connect(lambda: alfa_edu.login())
    alfa_edu.ui.btn_voltar_tela_inicial.clicked.connect(
        lambda: alfa_edu.mudar_tela("tela_inicial"))

    alfa_edu.ui.btn_pular.clicked.connect(lambda: alfa_edu.pularfun())
    alfa_edu.ui.btn_cadastrar.clicked.connect(lambda: alfa_edu.input_conta())



if __name__ == '__main__':
    suppress_qt_warnings()

    app = QApplication(sys.argv)

    alfa_edu_app = AlfaEdu()
    app.setStyleSheet(alfa_edu_app.return_stylesheet())

    buttons(alfa_edu_app)

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    alfa_edu_app.show()
    # alfa_edu_app.showFullScreen()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
