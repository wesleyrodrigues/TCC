import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# username ou email para logar no servidor
username = 'alfaedu001@gmail.com'
#TODO Acessar BD
password = ''

from_addr = 'alfaedu001@gmail.com'
# TODO acesso a BD e email do professor default 
to_addrs = ['default@gmail.com']


# a biblioteca email possuí vários templates
# para diferentes formatos de mensagem
# neste caso usaremos MIMEText para enviar
# somente texto
message = MIMEText('Hello World teste 1')
message['subject'] = 'Hello'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)


try:
    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)

    server.sendmail(from_addr, to_addrs, message.as_string())

    server.quit()
except Exception as e:
    e = str(e)
    internetError = "[Errno 11001] getaddrinfo failed"
    passwordError = "Username and Password not accepted."
    
    if internetError in e:
        print("Erro de internet")
    elif passwordError in e:
        print("Erro na conta AlfaEdu, contate suporte")
    else:
        print(e)
        print("outro erro")    