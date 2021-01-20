# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_sair2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair2.setMaximumSize(QtCore.QSize(130, 25))
        self.btn_sair2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_sair2.setObjectName("btn_sair2")
        self.gridLayout.addWidget(self.btn_sair2, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.tela_inicial = QtWidgets.QWidget()
        self.tela_inicial.setObjectName("tela_inicial")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tela_inicial)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tela_inicial)
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
        self.btn_tela_cadastro = QtWidgets.QPushButton(self.tela_inicial)
        self.btn_tela_cadastro.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btn_tela_cadastro.setFont(font)
        self.btn_tela_cadastro.setObjectName("btn_tela_cadastro")
        self.verticalLayout_2.addWidget(self.btn_tela_cadastro)
        self.btn_tela_login = QtWidgets.QPushButton(self.tela_inicial)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btn_tela_login.setFont(font)
        self.btn_tela_login.setObjectName("btn_tela_login")
        self.verticalLayout_2.addWidget(self.btn_tela_login)
        self.btn_sair = QtWidgets.QPushButton(self.tela_inicial)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btn_sair.setFont(font)
        self.btn_sair.setAutoDefault(False)
        self.btn_sair.setObjectName("btn_sair")
        self.verticalLayout_2.addWidget(self.btn_sair)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout1.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout1, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.tela_inicial)
        self.tela_cadastro = QtWidgets.QWidget()
        self.tela_cadastro.setObjectName("tela_cadastro")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tela_cadastro)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        self.verticalLayout1 = QtWidgets.QVBoxLayout()
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.label1 = QtWidgets.QLabel(self.tela_cadastro)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.verticalLayout1.addWidget(self.label1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout1.addItem(spacerItem4)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout1.addItem(spacerItem5)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.lnome = QtWidgets.QLabel(self.tela_cadastro)
        self.lnome.setObjectName("lnome")
        self.verticalLayout_21.addWidget(self.lnome)
        self.input_nome_aluno = QtWidgets.QLineEdit(self.tela_cadastro)
        self.input_nome_aluno.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.input_nome_aluno.setObjectName("input_nome_aluno")
        self.verticalLayout_21.addWidget(self.input_nome_aluno)
        self.lsobrenome = QtWidgets.QLabel(self.tela_cadastro)
        self.lsobrenome.setObjectName("lsobrenome")
        self.verticalLayout_21.addWidget(self.lsobrenome)
        self.input_sobrenome = QtWidgets.QLineEdit(self.tela_cadastro)
        self.input_sobrenome.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.input_sobrenome.setObjectName("input_sobrenome")
        self.verticalLayout_21.addWidget(self.input_sobrenome)
        self.lsenha = QtWidgets.QLabel(self.tela_cadastro)
        self.lsenha.setObjectName("lsenha")
        self.verticalLayout_21.addWidget(self.lsenha)
        self.input_senha = QtWidgets.QLineEdit(self.tela_cadastro)
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha.setObjectName("input_senha")
        self.verticalLayout_21.addWidget(self.input_senha)
        self.lconfsenha = QtWidgets.QLabel(self.tela_cadastro)
        self.lconfsenha.setObjectName("lconfsenha")
        self.verticalLayout_21.addWidget(self.lconfsenha)
        self.input_conf_senha = QtWidgets.QLineEdit(self.tela_cadastro)
        self.input_conf_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_conf_senha.setObjectName("input_conf_senha")
        self.verticalLayout_21.addWidget(self.input_conf_senha)
        self.lnomeprofessor = QtWidgets.QLabel(self.tela_cadastro)
        self.lnomeprofessor.setObjectName("lnomeprofessor")
        self.verticalLayout_21.addWidget(self.lnomeprofessor)
        self.input_nome_professor = QtWidgets.QLineEdit(self.tela_cadastro)
        self.input_nome_professor.setObjectName("input_nome_professor")
        self.verticalLayout_21.addWidget(self.input_nome_professor)
        self.lemail = QtWidgets.QLabel(self.tela_cadastro)
        self.lemail.setObjectName("lemail")
        self.verticalLayout_21.addWidget(self.lemail)
        self.input_email = QtWidgets.QLineEdit(self.tela_cadastro)
        self.input_email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.input_email.setObjectName("input_email")
        self.verticalLayout_21.addWidget(self.input_email)
        self.lconfemail = QtWidgets.QLabel(self.tela_cadastro)
        self.lconfemail.setObjectName("lconfemail")
        self.verticalLayout_21.addWidget(self.lconfemail)
        self.input_conf_email = QtWidgets.QLineEdit(self.tela_cadastro)
        self.input_conf_email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.input_conf_email.setObjectName("input_conf_email")
        self.verticalLayout_21.addWidget(self.input_conf_email)
        self.btn_cadastrar = QtWidgets.QPushButton(self.tela_cadastro)
        self.btn_cadastrar.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.verticalLayout_21.addWidget(self.btn_cadastrar)
        self.horizontalLayout1.addLayout(self.verticalLayout_21)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout1.addItem(spacerItem6)
        self.verticalLayout1.addLayout(self.horizontalLayout1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout1.addItem(spacerItem7)
        self.gridLayout2.addLayout(self.verticalLayout1, 0, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout2, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.tela_cadastro)
        self.tela_login = QtWidgets.QWidget()
        self.tela_login.setObjectName("tela_login")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tela_login)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout3 = QtWidgets.QGridLayout()
        self.gridLayout3.setObjectName("gridLayout3")
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.label2 = QtWidgets.QLabel(self.tela_login)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.verticalLayout2.addWidget(self.label2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout2.addItem(spacerItem8)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(spacerItem9)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lnome_aluno = QtWidgets.QLabel(self.tela_login)
        self.lnome_aluno.setObjectName("lnome_aluno")
        self.verticalLayout_22.addWidget(self.lnome_aluno)
        self.input_nome_aluno_login = QtWidgets.QLineEdit(self.tela_login)
        self.input_nome_aluno_login.setObjectName("input_nome_aluno_login")
        self.verticalLayout_22.addWidget(self.input_nome_aluno_login)
        self.lsenha_login = QtWidgets.QLabel(self.tela_login)
        self.lsenha_login.setObjectName("lsenha_login")
        self.verticalLayout_22.addWidget(self.lsenha_login)
        self.input_senha_login = QtWidgets.QLineEdit(self.tela_login)
        self.input_senha_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha_login.setObjectName("input_senha_login")
        self.verticalLayout_22.addWidget(self.input_senha_login)
        self.btn_logar = QtWidgets.QPushButton(self.tela_login)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btn_logar.setFont(font)
        self.btn_logar.setObjectName("btn_logar")
        self.verticalLayout_22.addWidget(self.btn_logar)
        self.horizontalLayout2.addLayout(self.verticalLayout_22)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(spacerItem10)
        self.verticalLayout2.addLayout(self.horizontalLayout2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout2.addItem(spacerItem11)
        self.gridLayout3.addLayout(self.verticalLayout2, 0, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout3, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.tela_login)
        self.tela_escolher_atividades = QtWidgets.QWidget()
        self.tela_escolher_atividades.setObjectName("tela_escolher_atividades")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tela_escolher_atividades)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout4 = QtWidgets.QGridLayout()
        self.gridLayout4.setObjectName("gridLayout4")
        self.verticalLayout3 = QtWidgets.QVBoxLayout()
        self.verticalLayout3.setObjectName("verticalLayout3")
        self.label3 = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.verticalLayout3.addWidget(self.label3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout3.addItem(spacerItem12)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout3.addItem(spacerItem13)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_5 = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_23.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_23.addLayout(self.horizontalLayout_3)
        self.label_4 = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_23.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.tela_escolher_atividades)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_23.addWidget(self.spinBox)
        self.label_6 = QtWidgets.QLabel(self.tela_escolher_atividades)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_23.addWidget(self.label_6)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tela_escolher_atividades)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_23.addWidget(self.spinBox_2)
        self.btnProfessor = QtWidgets.QPushButton(self.tela_escolher_atividades)
        self.btnProfessor.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btnProfessor.setFont(font)
        self.btnProfessor.setObjectName("btnProfessor")
        self.verticalLayout_23.addWidget(self.btnProfessor)
        self.horizontalLayout3.addLayout(self.verticalLayout_23)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout3.addItem(spacerItem14)
        self.verticalLayout3.addLayout(self.horizontalLayout3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout3.addItem(spacerItem15)
        self.gridLayout4.addLayout(self.verticalLayout3, 0, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout4, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.tela_escolher_atividades)
        self.gridLayout.addWidget(self.stackedWidget, 3, 0, 1, 1)
        self.btn_pular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pular.setMaximumSize(QtCore.QSize(220, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.btn_pular.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(True)
        self.btn_pular.setFont(font)
        self.btn_pular.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_pular.setAutoFillBackground(False)
        self.btn_pular.setStyleSheet("color: rgb(255, 0, 0)")
        self.btn_pular.setObjectName("btn_pular")
        self.gridLayout.addWidget(self.btn_pular, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.btn_sair.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_sair2.setText(_translate("MainWindow", "voltar para página inicial"))
        self.label.setText(_translate("MainWindow", "PÁGINA INICIAL"))
        self.btn_tela_cadastro.setText(_translate("MainWindow", "Cadastrar"))
        self.btn_tela_login.setText(_translate("MainWindow", "Login"))
        self.btn_sair.setText(_translate("MainWindow", "Sair"))
        self.label1.setText(_translate("MainWindow", "PÁGINA DE CADASTRO"))
        self.lnome.setText(_translate("MainWindow", "Nome do Aluno"))
        self.lsobrenome.setText(_translate("MainWindow", "Sobrenome do Aluno"))
        self.lsenha.setText(_translate("MainWindow", "Senha"))
        self.lconfsenha.setText(_translate("MainWindow", "Confirme a senha"))
        self.lnomeprofessor.setText(_translate("MainWindow", "Nome do Professor"))
        self.lemail.setText(_translate("MainWindow", "E-mail do Professor"))
        self.lconfemail.setText(_translate("MainWindow", "Confirme o e-mail do Professor"))
        self.btn_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.label2.setText(_translate("MainWindow", "PÁGINA LOGIN"))
        self.lnome_aluno.setText(_translate("MainWindow", "Nome do Aluno"))
        self.lsenha_login.setText(_translate("MainWindow", "Senha"))
        self.btn_logar.setText(_translate("MainWindow", "Login"))
        self.label3.setText(_translate("MainWindow", "PÁGINA ESCOLHER ATIVIDADES"))
        self.label_5.setText(_translate("MainWindow", "Atividades"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "Digite o tempo"))
        self.label_6.setText(_translate("MainWindow", "Quantidade de exercicios"))
        self.btnProfessor.setText(_translate("MainWindow", "Professor"))
        self.btn_pular.setText(_translate("MainWindow", "Pular páginas (botão temporário)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
