from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QFontDatabase
from mainUi import Ui_MainWindow
from alfaeduDB import AlfaEduDB
from criptografia import Cript
from atividades import Atividades
from imagem_feedback import Feedback
from random import shuffle
from os import environ
import sys
import time


class AlfaEdu(QMainWindow):
    def __init__(self):
        super(AlfaEdu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stack = self.ui.stackedWidget  # paginas das interface
        self.ui.btn_voltar_tela_inicial.hide()
        self.ui.lcd_atvtempo.setNumDigits(5)
        self._text = "00:00"
        self.lcd_setText(self._text)
        self._timer = QtCore.QTimer(self)
        self._timer.setInterval(1000)
        self._seconds = 60
        self._timer.timeout.connect(self.onTimeout)
        # TODO verificar depois background app
        # self.background_imagem = "MainWindow.png"
        # self.background_cor = "#add8e6"
        self.stack.setCurrentWidget(
            self.stack.findChild(QWidget, "tela_inicial"))
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.btnProfessor
        # TODO apagar depois essa linha pular.
        self.pular = 1
        self.alfa_edu_db = AlfaEduDB()
        self.alfa_edu_db.createDB()
        # adiciona os nomes no combo box de login
        self.ui.cb_nome_aluno.addItems(self.alfa_edu_db.seleciona_nomes())

        self.usuario = ""
        # self.senha_cript = ""
        # self.ui.label_3.setPixmap(QPixmap(ApplicationContext().get_resource("dialog1.png")))

        # TODO mover depois para mudar tela ações
        # self.atv_nome_imagem = DigiteNomeDaImagem()
        self.atividades = Atividades()
        self.atv_imagens_bd = self.alfa_edu_db.seleciona_tudo_imagens()
        shuffle(self.atv_imagens_bd)
        # self.atv_nome_imagem.set_max_contador(len(self.atv_imagens_bd))
        self.atividades.set_max_atividades(len(self.atv_imagens_bd))

        self.appctxt = None
        # imagem = self.atv_imagens_bd[0]
        # pixmap = self.get_QPixmap_image(imagem)
        # self.ui.latv_digt_nome_imagem.setPixmap(pixmap)
        self.buttons()
        self.line_edits()

    def set_appctxt(self, appctxt):
        self.appctxt = appctxt

    def upper_text(self, arg):
        arg.setText(str(arg.text()).upper())

    def tela_feedback(self):
        self.feedback = Feedback()
        self.feedback.set_feedback_imagem(
            {
                "nome_aluno": "Testando",
                "nome_professor": "Testando",
                "tempo_proposto": "Testando",
                "tempo_executado": "Testando",
                "total_questoes": "Testando",
                "acertos": "Testando",
                "erros": "Testando",
                "media": "Testando"
            }
        )
        imagem = self.feedback.get_imagem()
        pixmap = self.get_QPixmap_image(imagem)
        self.ui.l_img_feedback.setPixmap(pixmap)
        self._timer.stop()
        self.mudar_tela("tela_feedback")

    def get_QPixmap_image(self, image):
        return QPixmap(self.appctxt.get_resource(image))

    def change_label_image(self, label):
        # imagem = self.atv_imagens_bd[self.atv_nome_imagem.get_contador()]
        imagem = self.atv_imagens_bd[self.atividades.get_contador()]
        nome_imagem = imagem[:-4]
        print(nome_imagem)
        pixmap = self.get_QPixmap_image(imagem)
        label.setPixmap(pixmap)
        return nome_imagem
    
    def change_btn_image(self, btn):
        # imagem = self.atv_imagens_bd[self.atv_nome_imagem.get_contador()]
        imagem = self.atv_imagens_bd[self.atividades.get_contador()]
        nome_imagem = imagem[:-4]
        print(nome_imagem)
        # pixmap = self.get_QPixmap_image(imagem)

        btn.setStyleSheet(f"border-image: url(src/main/resources/base/{imagem});")
        return nome_imagem

    def reset_atividades(self):
        self.atividades = Atividades()
        shuffle(self.atv_imagens_bd)
        self.atividades.set_max_atividades(len(self.atv_imagens_bd))

    def atv_digite_nome(self):
        input_nome = str(self.ui.input_atv_digt_nome_imagem.text())
        self.fim_bool = self.atividades.get_fim()
        print(self.fim_bool)
        if (self.fim_bool):
            self.tela_feedback()
            self.reset_atividades()
        else:
            nome_imagem = self.change_label_image(
                self.ui.latv_digt_nome_imagem)
            if(nome_imagem == input_nome):
                self.atividades.set_contador_mais_um()
                self.change_label_image(self.ui.latv_digt_nome_imagem)
                self.ui.input_atv_digt_nome_imagem.setText("")
    
    def atv_clique_na_imagem(self):
        self.fim_bool = self.atividades.get_fim()
        print(self.fim_bool)
        if (self.fim_bool):
            self.tela_feedback()
            self.reset_atividades()
        else:
            self.atividades.set_contador_mais_um()
            self.change_btn_image(self.ui.btn_imagem_1)
            self.change_btn_image(self.ui.btn_imagem_2)
            self.change_btn_image(self.ui.btn_imagem_3)

    def onTimeout(self):
        self._seconds -= 1
        self.displayTime()

    def displayTime(self):
        self.lcd_setText(time.strftime('%M:%S', time.gmtime(self._seconds)))

        if(time.gmtime(self._seconds).tm_min == 0 and time.gmtime(self._seconds).tm_sec == 0):
            self.mudar_tela("tela_feedback")
            self._timer.stop()

    def lcd_setText(self, texto):
        self._text = texto
        self.ui.lcd_atvtempo.display(texto)

    def lcd_getText(self):
        return self._text

    def fazer_atividade(self):
        self._seconds = int(self.ui.timeEdit.text()) * 60
        self._timer.start()

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
            self.ui.input_nome_aluno.setText("")
            self.ui.input_senha.setText("")
            self.ui.input_conf_senha.setText("")
            self.ui.input_nome_professor.setText("")
            self.ui.input_email.setText("")
            self.ui.input_conf_email.setText("")

    def mudar_telas_acoes(self, stack_name):
        if(stack_name == "tela_atividade_digt_nome_imagem"):
            self.reset_atividades()
            self.atv_digite_nome()
        elif(stack_name == "tela_atividade_clique_na_imagem"):
            self.reset_atividades()
            self.atv_clique_na_imagem()

    def mudar_tela(self, stack_name):
        # TODO Melhorar
        stack_passado = self.stack.findChild(QWidget, stack_name)
        self.stack.setCurrentWidget(stack_passado)
        self.mudar_telas_acoes(stack_name)
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
        senha_cript = self.alfa_edu_db.seleciona_usuario_por_nome(nome)[
            "senha"]
        retorno = Cript.verifica_usuario_e_senha(senha_cript, senha)

        if(retorno):
            self.mudar_tela("tela_escolher_atividades")
            self.usuario = nome
            # self.senha = senha
        else:
            self.ui.lerro_login.setText("Senha errada digite novamente!!")

    # TODO melhorar depois
    def mensagens_erros(self, arg):
        texto_lines = self.get_text()
        self.ui.lcampos.setText("")
        if(arg == "nome_aluno"):
            for count in range(self.ui.cb_nome_aluno.count()):
                if(texto_lines["nome_aluno"] == self.ui.cb_nome_aluno.itemText(count)):
                    msg = "Nome do(a) aluno(a), já cadastrado\n"
                    self.ui.lverifica_nome.setText(msg)
                    return False
            self.ui.lverifica_nome.setText("")
            return True

        # TODO redundancia de ifs em senha e conf_senha
        elif(arg == "senha" or arg == "conf_senha"):
            if(texto_lines["conf_senha"] == ""
               or texto_lines["senha"] == ""):
                self.ui.lverifica_senha.setText("")

            if(texto_lines["conf_senha"] != ""):
                if(texto_lines["senha"] != texto_lines["conf_senha"]):
                    msg = "As senhas não são iguais. Tente novamente.\n"
                    self.ui.lverifica_senha.setText(msg)
                    return False
                self.ui.lverifica_senha.setText("")
                return True

        # TODO redundancia de ifs em email e conf email
        elif(arg == "email" or arg == "conf_email"):
            if(texto_lines["conf_email"] == ""
               or texto_lines["email_professor"] == ""):
                self.ui.lverifica_email.setText("")

            if(texto_lines["conf_email"] != ""):
                if(texto_lines["email_professor"] != texto_lines["conf_email"]):
                    msg = "Os emails não são iguais. Tente novamente.\n"
                    self.ui.lverifica_email.setText(msg)
                    return False
                self.ui.lverifica_email.setText("")
                return True

    def input_conta(self):
        texto_lines = self.get_text()

        campos = True

        msg_erros = self.mensagens_erros(
            "nome_aluno") and self.mensagens_erros(
            "conf_senha") and self.mensagens_erros(
            "conf_email")

        for i in texto_lines:
            if(not(texto_lines[i])):
                msg = "Verifique se todos dados estão preenchidos\n"
                self.ui.lcampos.setText(msg)
                campos = False
                break

        if(msg_erros and campos):
            print("adicionado")
            # TODO criptografia não funciona
            texto_lines["senha"] = Cript.criptografa_senha(
                texto_lines["senha"])
            t = self.alfa_edu_db.add_conta(texto_lines)
            if(t):
                self.ui.cb_nome_aluno.addItem(texto_lines["nome_aluno"])
                self.mudar_tela("tela_escolher_atividades")
                self.usuario = texto_lines["nome_aluno"]
                # self.senha = texto_lines["senha"]
                self.ui.lnome_aluno_logado.setText(self.usuario)
            else:
                msg = "Dados não salvos erro Banco de dados\n"
                self.ui.lcampos.setText(msg)

    def buttons(self):
        # telas
        print("Passou aqui")
        self.ui.btn_tela_cadastro.clicked.connect(
            lambda: self.mudar_tela("tela_cadastro"))
        self.ui.btn_tela_login.clicked.connect(
            lambda: self.mudar_tela("tela_login"))
        self.ui.btn_login.clicked.connect(lambda: self.login())
        self.ui.btn_voltar_tela_inicial.clicked.connect(
            lambda: self.mudar_tela("tela_inicial"))
        
        self.ui.btn_tela_atividade_digt_nome_imagem.clicked.connect(
            lambda: self.mudar_tela("tela_atividade_digt_nome_imagem"))
        self.ui.btn_tela_atividade_clique_na_imagem.clicked.connect(
            lambda: self.mudar_tela("tela_atividade_clique_na_imagem")
        )

        self.ui.btn_pular.clicked.connect(lambda: self.pularfun())
        self.ui.btn_cadastrar.clicked.connect(lambda: self.input_conta())
        self.ui.btnAtvidade.clicked.connect(lambda: self.fazer_atividade())
        
        self.ui.btn_atv_digt_nome_imagem.clicked.connect(
            lambda: self.atv_digite_nome())
        self.ui.btn_imagem_1.clicked.connect(
            lambda: self.atv_clique_na_imagem())
        self.ui.btn_imagem_2.clicked.connect(
            lambda: self.atv_clique_na_imagem())
        self.ui.btn_imagem_3.clicked.connect(
            lambda: self.atv_clique_na_imagem())

    def line_edits(self):
        self.ui.input_conf_email.returnPressed.connect(
            self.ui.btn_cadastrar.click)
        self.ui.input_senha_login.returnPressed.connect(
            self.ui.btn_login.click)
        self.ui.input_atv_digt_nome_imagem.returnPressed.connect(
            lambda: self.atv_digite_nome())

        self.ui.input_atv_digt_nome_imagem.textChanged.connect(
            lambda: self.upper_text(self.ui.input_atv_digt_nome_imagem))
        self.ui.input_nome_aluno.textChanged.connect(
            lambda: self.mensagens_erros("nome_aluno"))
        self.ui.input_senha.textChanged.connect(
            lambda: self.mensagens_erros("senha"))
        self.ui.input_conf_senha.textChanged.connect(
            lambda: self.mensagens_erros("conf_senha"))
        self.ui.input_conf_email.textChanged.connect(
            lambda: self.mensagens_erros("conf_email"))
        self.ui.input_email.textChanged.connect(
            lambda: self.mensagens_erros("email"))

    # TODO melhorar depois

    # def return_stylesheet(self):

    #     return """
    #         QMainWindow {
    #             background-image: url("src/main/app_imagens/%s");
    #             background-color: "%s";
    #         border-image: url("src/main/app_imagens/%s") 0 0 0 0 stretch stretch;
    #             background-repeat: no-repeat;
    #             background-position: center;
    #         }""" % (
    #         self.background_imagem,
    #         self.background_cor,
    #         self.background_imagem
    #     )


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == '__main__':
    suppress_qt_warnings()

    app = QApplication(sys.argv)

    alfa_edu_app = AlfaEdu()
    # app.setStyleSheet(alfa_edu_app.return_stylesheet())

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    alfa_edu_app.set_appctxt(appctxt)

    QFontDatabase.addApplicationFont(
        appctxt.get_resource("Schoolwork-Regular.ttf"))

    alfa_edu_app.show()
    # alfa_edu_app.showFullScreen()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
