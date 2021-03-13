# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 764)
        MainWindow.setStyleSheet("QMainWindow {\n"
"                \n"
"    background-image: url(:/tela/app_imagens/kawaii-1546834.png);\n"
"                background-repeat: no-repeat; \n"
"                background-position: center;\n"
" }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame {\n"
"selection-background-color: rgb(85, 255, 255);\n"
"background-color: rgb(85, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Cabecalho = QtWidgets.QFrame(self.frame)
        self.Cabecalho.setMinimumSize(QtCore.QSize(0, 90))
        self.Cabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cabecalho.setObjectName("Cabecalho")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Cabecalho)
        self.horizontalLayout_9.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(700)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.esquerda = QtWidgets.QFrame(self.Cabecalho)
        self.esquerda.setMaximumSize(QtCore.QSize(200, 100))
        self.esquerda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.esquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.esquerda.setObjectName("esquerda")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.esquerda)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.L_nome_aluno_logado = QtWidgets.QLabel(self.esquerda)
        self.L_nome_aluno_logado.setObjectName("L_nome_aluno_logado")
        self.verticalLayout_8.addWidget(self.L_nome_aluno_logado)
        self.lcd_atvtempo = QtWidgets.QLCDNumber(self.esquerda)
        self.lcd_atvtempo.setObjectName("lcd_atvtempo")
        self.verticalLayout_8.addWidget(self.lcd_atvtempo)
        self.horizontalLayout_9.addWidget(self.esquerda)
        self.direita = QtWidgets.QFrame(self.Cabecalho)
        self.direita.setMaximumSize(QtCore.QSize(200, 16777215))
        self.direita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.direita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.direita.setObjectName("direita")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.direita)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btn_voltar_tela_inicial = QtWidgets.QPushButton(self.direita)
        self.btn_voltar_tela_inicial.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_voltar_tela_inicial.setObjectName("btn_voltar_tela_inicial")
        self.verticalLayout_9.addWidget(self.btn_voltar_tela_inicial)
        self.btn_pular = QtWidgets.QPushButton(self.direita)
        self.btn_pular.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_pular.setObjectName("btn_pular")
        self.verticalLayout_9.addWidget(self.btn_pular)
        self.horizontalLayout_9.addWidget(self.direita)
        self.verticalLayout_4.addWidget(self.Cabecalho)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.tela_inicial = QtWidgets.QWidget()
        self.tela_inicial.setStyleSheet("")
        self.tela_inicial.setObjectName("tela_inicial")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tela_inicial)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.tela_inicial)
        self.frame_2.setMaximumSize(QtCore.QSize(350, 500))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_sair = QtWidgets.QPushButton(self.frame_2)
        self.btn_sair.setGeometry(QtCore.QRect(110, 290, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(26)
        self.btn_sair.setFont(font)
        self.btn_sair.setStyleSheet("QPushButton {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(181, 181, 181);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(71, 71, 71);\n"
"border: 2px solid rgb(117, 117, 117);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 255, 8);\n"
"border: 2px solid rgb(0, 255, 0);\n"
"\n"
"}")
        self.btn_sair.setObjectName("btn_sair")
        self.btn_tela_cadastro = QtWidgets.QPushButton(self.frame_2)
        self.btn_tela_cadastro.setGeometry(QtCore.QRect(110, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(26)
        self.btn_tela_cadastro.setFont(font)
        self.btn_tela_cadastro.setStyleSheet("QPushButton {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(181, 181, 181);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(71, 71, 71);\n"
"border: 2px solid rgb(117, 117, 117);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 255, 8);\n"
"border: 2px solid rgb(0, 255, 0);\n"
"\n"
"}")
        self.btn_tela_cadastro.setObjectName("btn_tela_cadastro")
        self.btn_tela_login = QtWidgets.QPushButton(self.frame_2)
        self.btn_tela_login.setGeometry(QtCore.QRect(110, 230, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(26)
        self.btn_tela_login.setFont(font)
        self.btn_tela_login.setStyleSheet("QPushButton {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(181, 181, 181);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(71, 71, 71);\n"
"border: 2px solid rgb(117, 117, 117);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 255, 8);\n"
"border: 2px solid rgb(0, 255, 0);\n"
"\n"
"}")
        self.btn_tela_login.setObjectName("btn_tela_login")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(75, 50, 200, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/tela/app_imagens/tentativa.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.tela_inicial)
        self.tela_cadastro = QtWidgets.QWidget()
        self.tela_cadastro.setObjectName("tela_cadastro")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tela_cadastro)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.tela_cadastro)
        self.frame_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMaximumSize(QtCore.QSize(350, 700))
        self.frame_4.setStyleSheet("background-color: rgb(190, 255, 234);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.input_nome_aluno = QtWidgets.QLineEdit(self.frame_4)
        self.input_nome_aluno.setMaximumSize(QtCore.QSize(16777215, 35))
        self.input_nome_aluno.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.input_nome_aluno.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhLatinOnly)
        self.input_nome_aluno.setObjectName("input_nome_aluno")
        self.verticalLayout_5.addWidget(self.input_nome_aluno)
        self.lverifica_nome = QtWidgets.QLabel(self.frame_4)
        self.lverifica_nome.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lverifica_nome.setFont(font)
        self.lverifica_nome.setStyleSheet("color: rgb(255, 0, 0)")
        self.lverifica_nome.setText("")
        self.lverifica_nome.setObjectName("lverifica_nome")
        self.verticalLayout_5.addWidget(self.lverifica_nome)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.input_senha = QtWidgets.QLineEdit(self.frame_4)
        self.input_senha.setMaximumSize(QtCore.QSize(16777215, 35))
        self.input_senha.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.input_senha.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha.setObjectName("input_senha")
        self.verticalLayout_5.addWidget(self.input_senha)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setEnabled(True)
        self.label_8.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.input_conf_senha = QtWidgets.QLineEdit(self.frame_4)
        self.input_conf_senha.setMaximumSize(QtCore.QSize(16777215, 35))
        self.input_conf_senha.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.input_conf_senha.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.input_conf_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_conf_senha.setClearButtonEnabled(False)
        self.input_conf_senha.setObjectName("input_conf_senha")
        self.verticalLayout_5.addWidget(self.input_conf_senha)
        self.lverifica_senha = QtWidgets.QLabel(self.frame_4)
        self.lverifica_senha.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lverifica_senha.setStyleSheet("color: rgb(255, 0, 0)")
        self.lverifica_senha.setText("")
        self.lverifica_senha.setObjectName("lverifica_senha")
        self.verticalLayout_5.addWidget(self.lverifica_senha)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.input_nome_professor = QtWidgets.QLineEdit(self.frame_4)
        self.input_nome_professor.setMaximumSize(QtCore.QSize(16777215, 35))
        self.input_nome_professor.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.input_nome_professor.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.input_nome_professor.setObjectName("input_nome_professor")
        self.verticalLayout_5.addWidget(self.input_nome_professor)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.input_email = QtWidgets.QLineEdit(self.frame_4)
        self.input_email.setMaximumSize(QtCore.QSize(16777215, 35))
        self.input_email.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.input_email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhLatinOnly)
        self.input_email.setObjectName("input_email")
        self.verticalLayout_5.addWidget(self.input_email)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.input_conf_email = QtWidgets.QLineEdit(self.frame_4)
        self.input_conf_email.setMaximumSize(QtCore.QSize(16777215, 35))
        self.input_conf_email.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.input_conf_email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhLatinOnly)
        self.input_conf_email.setObjectName("input_conf_email")
        self.verticalLayout_5.addWidget(self.input_conf_email)
        self.lverifica_email = QtWidgets.QLabel(self.frame_4)
        self.lverifica_email.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lverifica_email.setStyleSheet("color: rgb(255, 0, 0)")
        self.lverifica_email.setText("")
        self.lverifica_email.setObjectName("lverifica_email")
        self.verticalLayout_5.addWidget(self.lverifica_email)
        self.btn_cadastrar = QtWidgets.QPushButton(self.frame_4)
        self.btn_cadastrar.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setStyleSheet("QPushButton {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(181, 181, 181);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(71, 71, 71);\n"
"border: 2px solid rgb(117, 117, 117);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 255, 8);\n"
"border: 2px solid rgb(0, 255, 0);\n"
"\n"
"}")
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.verticalLayout_5.addWidget(self.btn_cadastrar)
        self.lcampos = QtWidgets.QLabel(self.frame_4)
        self.lcampos.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lcampos.setFont(font)
        self.lcampos.setStyleSheet("color: rgb(255, 0, 0)")
        self.lcampos.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lcampos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcampos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcampos.setText("")
        self.lcampos.setScaledContents(True)
        self.lcampos.setObjectName("lcampos")
        self.verticalLayout_5.addWidget(self.lcampos)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.tela_cadastro)
        self.tela_login = QtWidgets.QWidget()
        self.tela_login.setObjectName("tela_login")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tela_login)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.tela_login)
        self.frame_5.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(400, 400))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lnome_aluno = QtWidgets.QLabel(self.frame_6)
        self.lnome_aluno.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.lnome_aluno.setFont(font)
        self.lnome_aluno.setObjectName("lnome_aluno")
        self.verticalLayout_6.addWidget(self.lnome_aluno)
        self.cb_nome_aluno = QtWidgets.QComboBox(self.frame_6)
        self.cb_nome_aluno.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cb_nome_aluno.setFont(font)
        self.cb_nome_aluno.setStyleSheet("QComboBox {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.cb_nome_aluno.setObjectName("cb_nome_aluno")
        self.verticalLayout_6.addWidget(self.cb_nome_aluno)
        self.lsenha = QtWidgets.QLabel(self.frame_6)
        self.lsenha.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Schoolwork")
        font.setPointSize(36)
        self.lsenha.setFont(font)
        self.lsenha.setObjectName("lsenha")
        self.verticalLayout_6.addWidget(self.lsenha)
        self.input_senha_login = QtWidgets.QLineEdit(self.frame_6)
        self.input_senha_login.setMaximumSize(QtCore.QSize(16777215, 40))
        self.input_senha_login.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}")
        self.input_senha_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha_login.setObjectName("input_senha_login")
        self.verticalLayout_6.addWidget(self.input_senha_login)
        self.lerro_login = QtWidgets.QLabel(self.frame_6)
        self.lerro_login.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lerro_login.setFont(font)
        self.lerro_login.setStyleSheet("color: rgb(255, 0, 0)")
        self.lerro_login.setText("")
        self.lerro_login.setObjectName("lerro_login")
        self.verticalLayout_6.addWidget(self.lerro_login)
        self.btn_login = QtWidgets.QPushButton(self.frame_6)
        self.btn_login.setMaximumSize(QtCore.QSize(16777215, 60))
        self.btn_login.setStyleSheet("QPushButton {\n"
"\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:10px;\n"
"background-color: rgb(181, 181, 181);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(71, 71, 71);\n"
"border: 2px solid rgb(117, 117, 117);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 255, 8);\n"
"border: 2px solid rgb(0, 255, 0);\n"
"\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout_6.addWidget(self.btn_login)
        self.horizontalLayout_7.addWidget(self.frame_6)
        self.horizontalLayout_6.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.tela_login)
        self.tela_escolher_atividades = QtWidgets.QWidget()
        self.tela_escolher_atividades.setObjectName("tela_escolher_atividades")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tela_escolher_atividades)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_tela_atividade_digt_nome_imagem = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.btn_tela_atividade_digt_nome_imagem.setObjectName("btn_tela_atividade_digt_nome_imagem")
        self.horizontalLayout_3.addWidget(self.btn_tela_atividade_digt_nome_imagem)
        self.pushButton = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_4 = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.timeEdit = QtWidgets.QTimeEdit(self.tela_escolher_atividades)
        self.timeEdit.setMaximumTime(QtCore.QTime(0, 59, 59))
        self.timeEdit.setMinimumTime(QtCore.QTime(0, 1, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_2.addWidget(self.timeEdit)
        self.label_6 = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tela_escolher_atividades)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_2.addWidget(self.spinBox_2)
        self.btnAtvidade = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.btnAtvidade.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btnAtvidade.setFont(font)
        self.btnAtvidade.setObjectName("btnAtvidade")
        self.verticalLayout_2.addWidget(self.btnAtvidade)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.tela_escolher_atividades)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(240, 180, 321, 151))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page)
        self.tela_atividade_digt_nome_imagem = QtWidgets.QWidget()
        self.tela_atividade_digt_nome_imagem.setObjectName("tela_atividade_digt_nome_imagem")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tela_atividade_digt_nome_imagem)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_21 = QtWidgets.QFrame(self.tela_atividade_digt_nome_imagem)
        self.frame_21.setStyleSheet("background-color: rgb(247, 255, 208);")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.frame_31 = QtWidgets.QFrame(self.frame_21)
        self.frame_31.setMaximumSize(QtCore.QSize(450, 550))
        self.frame_31.setStyleSheet("")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.input_atv_digt_nome_imagem = QtWidgets.QLineEdit(self.frame_31)
        self.input_atv_digt_nome_imagem.setGeometry(QtCore.QRect(30, 400, 280, 55))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.input_atv_digt_nome_imagem.setFont(font)
        self.input_atv_digt_nome_imagem.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(107, 107, 107);\n"
"    border-radius: 5px;\n"
"    background-color:rgb(0, 127, 0)\n"
"}")
        self.input_atv_digt_nome_imagem.setText("")
        self.input_atv_digt_nome_imagem.setFrame(True)
        self.input_atv_digt_nome_imagem.setObjectName("input_atv_digt_nome_imagem")
        self.btn_atv_digt_nome_imagem = QtWidgets.QPushButton(self.frame_31)
        self.btn_atv_digt_nome_imagem.setGeometry(QtCore.QRect(335, 397, 61, 61))
        self.btn_atv_digt_nome_imagem.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    background-image: url(:/botao/button-156707_1280.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"\n"
"\n"
"}")
        self.btn_atv_digt_nome_imagem.setText("")
        self.btn_atv_digt_nome_imagem.setObjectName("btn_atv_digt_nome_imagem")
        self.latv_digt_nome_imagem = QtWidgets.QLabel(self.frame_31)
        self.latv_digt_nome_imagem.setGeometry(QtCore.QRect(45, 20, 360, 360))
        self.latv_digt_nome_imagem.setMaximumSize(QtCore.QSize(360, 360))
        self.latv_digt_nome_imagem.setText("")
        self.latv_digt_nome_imagem.setPixmap(QtGui.QPixmap(":/atvimg/imagens_atividades/ARVORE.png"))
        self.latv_digt_nome_imagem.setScaledContents(True)
        self.latv_digt_nome_imagem.setObjectName("latv_digt_nome_imagem")
        self.horizontalLayout1.addWidget(self.frame_31)
        self.horizontalLayout_5.addWidget(self.frame_21)
        self.stackedWidget.addWidget(self.tela_atividade_digt_nome_imagem)
        self.tela_atividade_clique_na_imagem = QtWidgets.QWidget()
        self.tela_atividade_clique_na_imagem.setObjectName("tela_atividade_clique_na_imagem")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tela_atividade_clique_na_imagem)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tela_fundo = QtWidgets.QFrame(self.tela_atividade_clique_na_imagem)
        self.tela_fundo.setStyleSheet("background-color: rgb(247, 255, 208);")
        self.tela_fundo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tela_fundo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tela_fundo.setObjectName("tela_fundo")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tela_fundo)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.centralizador = QtWidgets.QFrame(self.tela_fundo)
        self.centralizador.setMaximumSize(QtCore.QSize(610, 500))
        self.centralizador.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.centralizador.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.centralizador.setFrameShadow(QtWidgets.QFrame.Raised)
        self.centralizador.setObjectName("centralizador")
        self.l_texto = QtWidgets.QLabel(self.centralizador)
        self.l_texto.setGeometry(QtCore.QRect(50, 0, 271, 60))
        self.l_texto.setMaximumSize(QtCore.QSize(600, 70))
        self.l_texto.setObjectName("l_texto")
        self.btn_alter_1 = QtWidgets.QPushButton(self.centralizador)
        self.btn_alter_1.setGeometry(QtCore.QRect(40, 200, 150, 150))
        self.btn_alter_1.setObjectName("btn_alter_1")
        self.btn_alter_2 = QtWidgets.QPushButton(self.centralizador)
        self.btn_alter_2.setGeometry(QtCore.QRect(230, 200, 150, 150))
        self.btn_alter_2.setObjectName("btn_alter_2")
        self.btn_alter_3 = QtWidgets.QPushButton(self.centralizador)
        self.btn_alter_3.setGeometry(QtCore.QRect(420, 200, 150, 150))
        self.btn_alter_3.setObjectName("btn_alter_3")
        self.l_alter_txt = QtWidgets.QLabel(self.centralizador)
        self.l_alter_txt.setGeometry(QtCore.QRect(340, 0, 271, 60))
        self.l_alter_txt.setMaximumSize(QtCore.QSize(600, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.l_alter_txt.setFont(font)
        self.l_alter_txt.setObjectName("l_alter_txt")
        self.horizontalLayout_8.addWidget(self.centralizador)
        self.verticalLayout_7.addWidget(self.tela_fundo)
        self.stackedWidget.addWidget(self.tela_atividade_clique_na_imagem)
        self.tela_feedback = QtWidgets.QWidget()
        self.tela_feedback.setObjectName("tela_feedback")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tela_feedback)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_7 = QtWidgets.QFrame(self.tela_feedback)
        self.frame_7.setStyleSheet("background-color: rgb(225, 246, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.l_img_feedback = QtWidgets.QLabel(self.frame_7)
        self.l_img_feedback.setText("")
        self.l_img_feedback.setObjectName("l_img_feedback")
        self.horizontalLayout_10.addWidget(self.l_img_feedback)
        self.verticalLayout_10.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.tela_feedback)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.cb_nome_aluno.setCurrentIndex(-1)
        self.btn_sair.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.L_nome_aluno_logado.setText(_translate("MainWindow", "TextLabel"))
        self.btn_voltar_tela_inicial.setText(_translate("MainWindow", "tela inicial"))
        self.btn_pular.setText(_translate("MainWindow", "pular"))
        self.btn_sair.setText(_translate("MainWindow", "Sair"))
        self.btn_tela_cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.btn_tela_login.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Nome completo do aluno"))
        self.label_7.setText(_translate("MainWindow", "Senha"))
        self.label_8.setText(_translate("MainWindow", "Confirmar Senha"))
        self.label_9.setText(_translate("MainWindow", "Nome do Professor "))
        self.label_11.setText(_translate("MainWindow", "E-mail do Professor "))
        self.label_10.setText(_translate("MainWindow", "Confirme o e-mail"))
        self.btn_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.lnome_aluno.setText(_translate("MainWindow", "Nome do Aluno"))
        self.lsenha.setText(_translate("MainWindow", "Senha"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "PÁGINA ESCOLHER ATIVIDADES"))
        self.label_5.setText(_translate("MainWindow", "Atividades"))
        self.btn_tela_atividade_digt_nome_imagem.setText(_translate("MainWindow", "Digite nome da imagem"))
        self.pushButton.setText(_translate("MainWindow", "Clique na imagem"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "Digite o tempo"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "mm"))
        self.label_6.setText(_translate("MainWindow", "Quantidade de exercicios"))
        self.btnAtvidade.setText(_translate("MainWindow", "Atividade"))
        self.label_16.setText(_translate("MainWindow", "SEM NADA AQUI"))
        self.l_texto.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:24pt;\">Clique na :</span></p></body></html>"))
        self.btn_alter_1.setText(_translate("MainWindow", "PushButton"))
        self.btn_alter_2.setText(_translate("MainWindow", "PushButton"))
        self.btn_alter_3.setText(_translate("MainWindow", "PushButton"))
        self.l_alter_txt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">CASA</span></p></body></html>"))

import file_img_rc
import img_fixas_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

