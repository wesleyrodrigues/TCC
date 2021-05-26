from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QRunnable, QThreadPool
from PyQt5.QtGui import QPixmap, QFontDatabase
from mainUi import Ui_MainWindow
from alfaeduDB import AlfaEduDB
from criptografia import Cript
from atividades import Atividades
from mensagens import mensagens_erros_cadastro
from imagem_feedback import Feedback
from email_feedback_aluno import EmailFeedback
from random import shuffle
from os import environ
import sys
import traceback
import time
# import time


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()  # Done


class AlfaEdu(QMainWindow):
    """
    Aplicação principal...
    """

    def __init__(self):
        super(AlfaEdu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("Colocar senha ao executar, email ao executar.")

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.stack = self.ui.stackedWidget  # paginas das interface
        self.ui.btn_voltar_tela_inicial.hide()
        self.ui.lcd_atvtempo.setNumDigits(5)
        self._text = "00:00"
        self.lcd_setText(self._text)
        self._timer = QtCore.QTimer(self)
        self._timer.setInterval(1000)
        self._seconds = 60
        self._timer.timeout.connect(self.onTimeout)
        self.ui.lcd_atvtempo.hide()
        self.tempo_proposto = ""
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
        #TODO 
        self.alfa_edu_db.createDB()
        # adiciona os nomes no combo box de login
        self.ui.cb_nome_aluno.addItems(self.alfa_edu_db.seleciona_nomes())

        self.usuario = ""
        # self.senha_cript = ""
        # self.ui.label_3.setPixmap(QPixmap(ApplicationContext().get_resource("dialog1.png")))

        # TODO mover depois para mudar tela ações
        # self.atv_nome_imagem = DigiteNomeDaImagem()
        self.atividades = Atividades()
        self.email = EmailFeedback()
        self.atv_imagens_bd = self.atividades.get_imagens_nomes()
        shuffle(self.atv_imagens_bd)
        # self.atv_nome_imagem.set_max_contador(len(self.atv_imagens_bd))
        self.total_atividades = len(self.atv_imagens_bd)
        self.atividades.set_max_atividades(self.total_atividades)

        self.appctxt = None
        # imagem = self.atv_imagens_bd[0]
        # pixmap = self.get_QPixmap_image(imagem)
        # self.ui.latv_digt_nome_imagem.setPixmap(pixmap)
        self.ui.btn_pular.hide()
        self.buttons()
        self.line_edits()


    def set_appctxt(self, appctxt):
        self.appctxt = appctxt

    def upper_text(self, arg):
        arg.setText(str(arg.text()).upper())

    def tela_feedback(self):
        aluno = self.alfa_edu_db.seleciona_aluno_por_nome(self.usuario)
        self.email.set_dict_aluno(aluno)
        self.ui.lcd_atvtempo.hide()
        self.feedback = Feedback()
        self.feedback.set_feedback_imagem(
            {
                "nome_aluno": aluno["nome_aluno"],
                "nome_professor": aluno["nome_professor"],
                "tempo_proposto": time.strftime('%M:%S', time.gmtime(self.tempo_proposto)),
                "tempo_executado": time.strftime('%M:%S', time.gmtime(self.tempo_proposto - self._seconds)),
                "total_questoes": str(self.atividades.get_contador()),
                "acertos": str(self.atividades.get_acertos()),
                "erros": str(self.atividades.get_erros()),
            }
        )
        imagem = self.feedback.get_imagem()
        pixmap = self.get_QPixmap_image(imagem)
        self.ui.l_img_feedback.setPixmap(pixmap)
        self._timer.stop()
        self.mudar_tela("tela_feedback")
        # TODO travando a tela de feedback usar thread.
        # QApplication.processEvents()
        feedbackWorker = Worker(self.email.send_email)
        self.threadpool.start(feedbackWorker)
        
        # QApplication.processEvents()

    def get_QPixmap_image(self, image):
        return QPixmap(self.appctxt.get_resource(image))

    def change_label_image(self, label):
        # imagem = self.atv_imagens_bd[self.atv_nome_imagem.get_contador()]
        print(self.atividades.get_contador())
        imagem = self.atv_imagens_bd[self.atividades.get_contador()]
        nome_imagem = imagem[:-4]
        print(nome_imagem)
        pixmap = self.get_QPixmap_image(imagem)
        label.setPixmap(pixmap)
        return nome_imagem

    def change_btn_image(self, btn, contador: int):
        # imagem = self.atv_imagens_bd[self.atv_nome_imagem.get_contador()]
        imagem = self.atv_imagens_bd[contador]
        nome_imagem = imagem[:-4]
        # print(nome_imagem)
        # TODO na aplicação final alterar caminho dessa pasta
        print("Mudar pasta na aplicação final")
        btn.setStyleSheet(f"border-image: url('{imagem}');")
        #btn.setStyleSheet(
        #    f"border-image: url('src/main/resources/base/{imagem}');")
        return nome_imagem

    def onTimeout(self):
        self._seconds -= 1
        self.displayTime()

    def displayTime(self):
        self.lcd_setText(time.strftime('%M:%S', time.gmtime(self._seconds)))

        if(time.gmtime(self._seconds).tm_min == 0 and time.gmtime(self._seconds).tm_sec == 0):
            self.tela_feedback()
            self._timer.stop()

    def lcd_setText(self, texto: str) -> None:
        self._text = texto
        self.ui.lcd_atvtempo.display(texto)

    def lcd_getText(self) -> str:
        return self._text

    def fazer_atividade(self) -> None:
        tela = self.atividades.get_atividade_escolhida()

        if(tela != ""):
            self.ui.lcd_atvtempo.show()
            self._seconds = int(self.ui.timeEdit.text()) * 60
            self.tempo_proposto = self._seconds
            self.mudar_tela(tela)
            self._timer.start()

    def pularfun(self):  # TODO APAGAR
        self.stack.setCurrentIndex(self.pular)
        self.pular += 1
        if(self.pular == self.stack.count()):
            self.pular = 0

    def hide_widgets(self, stack_name: str):
        if(stack_name == "tela_inicial"):
            self.atv_escolhida("")
            # self.atividades.atividade_escolhida_fun(self, "")
            self.ui.btn_voltar_tela_inicial.hide()
            self.usuario = ""
            self.ui.lnome_aluno_logado.setText("")
            self.ui.lcd_atvtempo.hide()
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
            self.ui.input_atv_digt_nome_imagem.setText("")
            self.ui.btn_cadastrar.setText("Cadastrar")
            self.ui.btn_excluir.hide()

    def editar_aluno(self):
        # print(self.usuario)
        aluno = self.alfa_edu_db.seleciona_aluno_por_nome(self.usuario)
        self.ui.input_nome_aluno.setText(aluno["nome_aluno"])
        self.ui.input_senha.setText(aluno["senha"])
        self.ui.input_conf_senha.setText(aluno["senha"])
        self.ui.input_nome_professor.setText(aluno["nome_professor"])
        self.ui.input_email.setText(aluno["email_professor"])
        self.ui.input_conf_email.setText(aluno["email_professor"])

    def deletar_aluno(self):
        aluno = self.alfa_edu_db.seleciona_aluno_por_nome(self.usuario)
        self.alfa_edu_db.deleta_conta(aluno["id_conta_aluno"])
        index = self.ui.cb_nome_aluno.currentIndex()
        self.ui.cb_nome_aluno.removeItem(index)
        self.mudar_tela("tela_inicial")
        self.ui.lnome_aluno_logado.setText("")

    def mudar_telas_acoes(self, stack_name):
        self.atividades.reset_atividades(self)
        self.atividades.set_max_atividades(self.total_atividades)
        # self.atividades.atividade_escolhida_fun(self, "")

        if(stack_name == "tela_atividade_digt_nome_imagem"):
            self.atividades.atv_digite_nome(self)
        elif(stack_name == "tela_atividade_clique_na_imagem"):
            self.atividades.set_posic_imagem()
            self.atividades.atv_clique_na_imagem(self, 0)
        elif(stack_name == "tela_atividade_clique_na_letra"):
            self.atividades.set_posic_letra()
            self.atividades.atv_clique_na_letra(self, 0)

        elif(stack_name == "tela_cadastro" and self.usuario):
            self.ui.btn_excluir.show()
            self.ui.btn_cadastrar.setText("Editar")
            self.editar_aluno()
            # print("Here")

    def atv_escolhida(self, nome_atividade):
        style = """
        QPushButton:hover {
            border: 2px solid rgb(0, 0, 0);
        }
        QPushButton{
            border-image: url(:/atvimg/app_imagens/"""

        # TODO verificar isso
        # QApplication.processEvents()
        # Gambiarra
        self.ui.btn_tela_atividade_clique_na_imagem.setStyleSheet(
            style + "clique na figura off.png);}")
        QApplication.processEvents()
        self.ui.btn_tela_atividade_clique_na_letra.setStyleSheet(
            style + "clique na letra que falta off.png);}")
        QApplication.processEvents()
        self.ui.btn_tela_atividade_digt_nome_imagem.setStyleSheet(
            style + "digite o nome da figura off.png);}")
        QApplication.processEvents()

        self.atividades.atividade_escolhida_fun(self, nome_atividade)

    def mudar_tela(self, stack_name):
        # TODO Melhorar
        if(stack_name != ""):
            stack_passado = self.stack.findChild(QWidget, stack_name)
            self.stack.setCurrentWidget(stack_passado)
            self.hide_widgets(stack_name)
            self.mudar_telas_acoes(stack_name)
        # self.stack.setCurrentIndex(index)

    def get_input_cadastro(self, nome_line="tudo"):
        nomes_dict = {
            "nome_aluno": str(self.ui.input_nome_aluno.text()).strip(),
            "senha": str(self.ui.input_senha.text()).strip(),
            "conf_senha": str(self.ui.input_conf_senha.text()).strip(),
            "nome_professor": str(self.ui.input_nome_professor.text()).strip(),
            "email_professor": str(self.ui.input_email.text()).strip(),
            "conf_email": str(self.ui.input_conf_email.text()).strip()
        }

        if (nome_line == "tudo"):
            return nomes_dict
        else:
            return nomes_dict[nome_line]

    def login(self):
        self.ui.lerro_login.setText("")
        nome = str(self.ui.cb_nome_aluno.currentText())
        senha = str(self.ui.input_senha_login.text())
        senha_cript = self.alfa_edu_db.seleciona_aluno_por_nome(nome)[
            "senha"]
        retorno = Cript.verifica_usuario_e_senha(senha_cript, senha)

        if(retorno):
            self.mudar_tela("tela_escolher_atividades")
            self.usuario = nome
            self.ui.lnome_aluno_logado.setText(self.usuario)
            # self.senha = senha
        else:
            self.ui.lerro_login.setText("Senha errada digite novamente!!")

    def input_conta(self):
        line_input_cadastro = self.get_input_cadastro()

        campos = True

        msg_erros = mensagens_erros_cadastro(
            self, "nome_aluno") and mensagens_erros_cadastro(
            self, "conf_senha") and mensagens_erros_cadastro(
            self, "conf_email")

        for i in line_input_cadastro:
            if(not(line_input_cadastro[i])):
                msg = "Verifique se todos dados estão preenchidos\n"
                self.ui.lcampos.setText(msg)
                campos = False
                break

        if(msg_erros and campos):
            print("adicionado")
            t = False
            aluno = self.alfa_edu_db.seleciona_aluno_por_nome(self.usuario)

            if(not(aluno["senha"] == line_input_cadastro["senha"])):
                line_input_cadastro["senha"] = Cript.criptografa_senha(
                    line_input_cadastro["senha"])

            if(self.usuario):
                t = self.alfa_edu_db.atualiza_conta(
                    line_input_cadastro, aluno["id_conta_aluno"])
                index = self.ui.cb_nome_aluno.currentIndex()
                self.ui.cb_nome_aluno.removeItem(index)
            else:
                t = self.alfa_edu_db.add_conta(line_input_cadastro)

            if(t):
                self.ui.cb_nome_aluno.addItem(
                    line_input_cadastro["nome_aluno"])
                self.mudar_tela("tela_escolher_atividades")
                self.usuario = line_input_cadastro["nome_aluno"]
                # self.senha = line_input_cadastro["senha"]
                self.ui.lnome_aluno_logado.setText(self.usuario)
            else:
                msg = "Dados não salvos erro Banco de dados\n"
                self.ui.lcampos.setText(msg)

    def buttons(self):
        # telas
        print("Passou aqui")
        self.ui.btn_tela_cadastro.clicked.connect(
            lambda: self.mudar_tela("tela_cadastro"))
        self.ui.btn_excluir.clicked.connect(
            lambda: self.deletar_aluno())
        self.ui.btn_tela_editar_aluno.clicked.connect(
            lambda: self.mudar_tela("tela_cadastro"))
        self.ui.btn_tela_login.clicked.connect(
            lambda: self.mudar_tela("tela_login"))
        self.ui.btn_login.clicked.connect(lambda: self.login())
        self.ui.btn_voltar_tela_inicial.clicked.connect(
            lambda: self.mudar_tela("tela_inicial"))

        self.ui.btn_tela_atividade_digt_nome_imagem.clicked.connect(
            lambda: self.atv_escolhida("tela_atividade_digt_nome_imagem"))
        self.ui.btn_tela_atividade_clique_na_imagem.clicked.connect(
            lambda: self.atv_escolhida("tela_atividade_clique_na_imagem")
        )
        self.ui.btn_tela_atividade_clique_na_letra.clicked.connect(
            lambda: self.atv_escolhida("tela_atividade_clique_na_letra")
        )

        self.ui.btn_pular.clicked.connect(lambda: self.pularfun())
        self.ui.btn_cadastrar.clicked.connect(lambda: self.input_conta())
        self.ui.btn_fazer_atividade.clicked.connect(
            lambda: self.fazer_atividade())

        self.ui.btn_atv_digt_nome_imagem.clicked.connect(
            lambda: self.atividades.atv_digite_nome(self))
        self.ui.btn_imagem_1.clicked.connect(
            lambda: self.atividades.atv_clique_na_imagem(self, 1))
        self.ui.btn_imagem_2.clicked.connect(
            lambda: self.atividades.atv_clique_na_imagem(self, 2))
        self.ui.btn_imagem_3.clicked.connect(
            lambda: self.atividades.atv_clique_na_imagem(self, 3))

        self.ui.btn_letra_1.clicked.connect(
            lambda: self.atividades.atv_clique_na_letra(self, 1)
        )
        self.ui.btn_letra_2.clicked.connect(
            lambda: self.atividades.atv_clique_na_letra(self, 2)
        )
        self.ui.btn_letra_3.clicked.connect(
            lambda: self.atividades.atv_clique_na_letra(self, 3)
        )
        self.ui.btn_letra_4.clicked.connect(
            lambda: self.atividades.atv_clique_na_letra(self, 4)
        )

    def line_edits(self):
        self.ui.input_conf_email.returnPressed.connect(
            self.ui.btn_cadastrar.click)
        self.ui.input_senha_login.returnPressed.connect(
            self.ui.btn_login.click)
        self.ui.input_atv_digt_nome_imagem.returnPressed.connect(
            lambda: self.atividades.atv_digite_nome(self))

        self.ui.input_atv_digt_nome_imagem.textChanged.connect(
            lambda: self.upper_text(self.ui.input_atv_digt_nome_imagem))
        self.ui.input_nome_aluno.textChanged.connect(
            lambda: mensagens_erros_cadastro(self, "nome_aluno"))
        self.ui.input_senha.textChanged.connect(
            lambda: mensagens_erros_cadastro(self, "senha"))
        self.ui.input_conf_senha.textChanged.connect(
            lambda: mensagens_erros_cadastro(self, "conf_senha"))
        self.ui.input_conf_email.textChanged.connect(
            lambda: mensagens_erros_cadastro(self, "conf_email"))
        self.ui.input_email.textChanged.connect(
            lambda: mensagens_erros_cadastro(self, "email"))

    # TODO melhorar depois

    def return_stylesheet(self):
        return """
            QMainWindow {
                background-image: url("MainWindow.png");
                background-color: "#add8e6";
            border-image: url("MainWindow.png") 0 0 0 0 stretch stretch;
                background-repeat: no-repeat;
                background-position: center;
            }"""


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == '__main__':
    suppress_qt_warnings()

    app = QApplication(sys.argv)

    alfa_edu_app = AlfaEdu()
    # app.setStyleSheet("""
    #         QMainWindow {
    #             background-image: url("MainWindow.png");
    #         }""")

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    alfa_edu_app.set_appctxt(appctxt)

    QFontDatabase.addApplicationFont(
        appctxt.get_resource("Schoolwork-Regular.ttf"))

    alfa_edu_app.show()
    # alfa_edu_app.showFullScreen()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
