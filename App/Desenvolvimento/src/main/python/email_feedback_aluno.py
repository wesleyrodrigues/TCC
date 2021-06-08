# https://humberto.io/pt-br/blog/enviando-e-recebendo-emails-com-python/
# https://medium.com/vacatronics/como-enviar-email-com-python-e43a9af7f672
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PyQt5 import QtWidgets


class EmailFeedback():

    def __init__(self) -> None:
        # Configuração
        # conexão com os servidores do google
        self.host = 'smtp.gmail.com'
        self.port = 465

        # username ou email para logar no servidor
        self.user = 'alfaedu001@gmail.com'
        # TODO criptografar senha

        # TODO Acessar BD
        # print("Colocar senha ao executar.")
        self.password = ''

        self._dict_aluno = {}

    def set_dict_aluno(self, dictA):
        self._dict_aluno = dictA

    def send_email(self):
        try:
            # Criando objeto
            # print('Criando objeto servidor...')
            # conectando de forma segura usando SSL
            server = smtplib.SMTP_SSL(self.host, self.port)

            # server.ehlo()
            # server.starttls()

            # Login com servidor
            # print('Login...')
            server.login(self.user, self.password)

            # Criando mensagem
            message = f'Feedback do aluno(a) {self._dict_aluno["nome_aluno"]}'
            # print('Criando mensagem...')
            email_msg = MIMEMultipart()
            email_msg['From'] = self.user

            # TODO acessar BD
            email_msg['To'] = self._dict_aluno["email_professor"]
            email_msg['Subject'] = f'Feedback {self._dict_aluno["nome_aluno"]}'
            # print('Adicionando texto...')
            email_msg.attach(MIMEText(message, 'plain'))

            # print('Obtendo arquivo...')
            # TODO verificar localização do arquivo depois
            filename = 'feedback.bmp'
            filepath = 'feedback.bmp'
            attachment = open(filepath, 'rb')

            # print('Lendo arquivo...')
            att = MIMEBase('application', 'octet-stream')
            att.set_payload(attachment.read())
            encoders.encode_base64(att)
            att.add_header('Content-Disposition',
                           f'attachment; filename= {filename}')

            attachment.close()
            # print('Adicionando arquivo ao email...')
            email_msg.attach(att)

            # Enviando mensagem
            # print('Enviando mensagem...')
            server.sendmail(email_msg['From'],
                            email_msg['To'], email_msg.as_string())
            # print('Mensagem enviada!')
            server.quit()

        except Exception as e:
            e = str(e)
            internetError = "[Errno 11001] getaddrinfo failed"
            passwordError = "Username and Password not accepted."

            # if internetError in e:
            #     QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Sem internet!!"),
            #                                QtWidgets.qApp.tr(
            #     f"Não foi possivel enviar o e-email.\nVerifique se o computador tem internet!!"),
            #     QtWidgets.QMessageBox.Cancel)
            #     # print("Erro de internet")
            # elif passwordError in e:
            #     QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Erro na conta!!"),
            #                                QtWidgets.qApp.tr(
            #     f"Não foi possivel enviar o e-email.\nErro na conta AlfaEdu, contate suporte!!"),
            #     QtWidgets.QMessageBox.Cancel)
            #     # print("Erro na conta AlfaEdu, contate suporte")
            # else:
            #     QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Erro desconhecido!!"),
            #                                QtWidgets.qApp.tr(
            #     f"Erro desconhecido, contate suporte!!\n{e}"),
            #     QtWidgets.QMessageBox.Cancel)
            #     print(e)
            #     # print("outro erro")
