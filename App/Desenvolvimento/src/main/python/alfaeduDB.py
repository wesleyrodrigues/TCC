from PyQt5 import QtSql, QtWidgets
from os import environ
import sys

# class WorkerSignals(QObject):
#     '''
#     Defines the signals available from a running worker thread.

#     Supported signals are:

#     finished
#         No data

#     error
#         tuple (exctype, value, traceback.format_exc() )

#     result
#         object data returned from processing, anything

#     progress
#         int indicating % progress

#     '''
#     finished = QtCore.pyqtSignal()
#     error = QtCore.pyqtSignal(tuple)
#     result = QtCore.pyqtSignal(object)
#     progress = QtCore.pyqtSignal(int)


# class Worker(QRunnable):
#     '''
#     Worker thread

#     Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

#     :param callback: The function callback to run on this worker thread. Supplied args and
#                      kwargs will be passed through to the runner.
#     :type callback: function
#     :param args: Arguments to pass to the callback function
#     :param kwargs: Keywords to pass to the callback function

#     '''

#     def __init__(self, fn, *args, **kwargs):
#         super(Worker, self).__init__()

#         # Store constructor arguments (re-used for processing)
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs
#         self.signals = WorkerSignals()

#         # Add the callback to our kwargs
#         # self.kwargs['progress_callback'] = self.signals.progress

#     @QtCore.pyqtSlot()
#     def run(self):
#         '''
#         Initialise the runner function with passed args, kwargs.
#         '''

#         # Retrieve args/kwargs here; and fire processing using them
#         try:
#             result = self.fn(*self.args, **self.kwargs)
#         except:
#             traceback.print_exc()
#             exctype, value = sys.exc_info()[:2]
#             self.signals.error.emit((exctype, value, traceback.format_exc()))
#         else:
#             # Return the result of the processing
#             self.signals.result.emit(result)
#         finally:
#             self.signals.finished.emit()  # Done

class AlfaEduDB(QtSql.QSqlDatabase):

    def __init__(self) -> None:
        super(AlfaEduDB, self).__init__()
        self.db = self.addDatabase('QSQLITE')
        self.db.setDatabaseName('alfa_edu.db')
        self.query = QtSql.QSqlQuery()

    def createDB(self) -> bool:

        if not self.db.open():
            erro = str(self.db.lastError().text())
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Não é possível abrir o banco de dados"),
                                           QtWidgets.qApp.tr(
                f"Erro: {erro}\nNão foi possível estabelecer uma conexão com o banco de dados.\n"
                "Este exemplo precisa de suporte SQLite. Por favor leia "
                "a documentação do driver Qt SQL para informações "
                "como faze-lo.\n\n" "Click Cancelar para sair."),
                QtWidgets.QMessageBox.Cancel)

            return False

        # # TODO BLOB não funciona salvar pasta imagens, por enquanto.
        # self.query.exec(
        #     """CREATE TABLE IF NOT EXISTS imagens_atividades(
        #         id_imagem INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        #         nome_imagem varchar UNIQUE NOT NULL
        #         )"""
        # )

        print(self.query.lastError().text())

        self.query.exec(
            """CREATE TABLE IF NOT EXISTS contas_alunos(
                id_conta_aluno INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                nome_aluno varchar NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                nome_professor varchar NOT NULL,
                email_professor varchar NOT NULL
                )"""
        )

        # query = QtSql.QSqlQuery(
        #     f"SELECT id_imagem FROM imagens_atividades WHERE id_imagem = 1")
        # t = query.next()

        # if(not(t)):
        #     self.workerdb = Worker(self.add_imagens)
        #     self.threadpool.start(self.workerdb)
        #     # self.add_imagens()

        self.db.close()
        return True

    # def add_imagem(self, input_conta):

    #     self.db.open()
    #     t = self.query.exec(
    #         f"""INSERT INTO imagens_atividades (nome_imagem)
    #          VALUES ('{input_conta["nome_imagem"]}')"""
    #     )
    #     # self.query.prepare("INSERT INTO imagens_atividades (nome_imagem) VALUES :nome_imagem")

    #     # self.query.bindValue("?nome_imagem", input_conta["nome_imagem"])
    #     # t = self.query.exec_()

    #     print(f"""Resultado {input_conta["nome_imagem"]} = {t}""")
    #     print(self.query.lastError().text())
    #     self.db.close()
    #     return t

    # # TODO verificar o que fazer com essa função depois
    # def add_imagens(self):
    #     # import pathlib
    #     # pasta = str(pathlib.Path().absolute())

    #     # caminhos = [path.join(pasta, nome) for nome in listdir(pasta)]
    #     # arquivos = [arq for arq in caminhos if path.isfile(
    #     #     arq) and arq.lower().endswith(".png")]
    #     # # pngs = [arq for arq in arquivos if arq.lower().endswith(".png")]
    #     # arquivos_nomes = [arq[77:][:-4] for arq in arquivos]
    #     arquivos = ['ABELHA.png',
    #                 'ARCO-ÍRIS.png',
    #                 'AVIÃO.png',
    #                 'BICICLETA.png',
    #                 'BOLA.png',
    #                 'BOLO.png',
    #                 'BORRACHA.png',
    #                 'CACHORRO.png',
    #                 'CADEADO.png',
    #                 'CAIXA.png',
    #                 'CAMA.png',
    #                 'CANECA.png',
    #                 'CARRO.png',
    #                 'CASA.png',
    #                 'CAVALO.png',
    #                 'CHINELO.png',
    #                 'COCO.png',
    #                 'COELHO.png',
    #                 'COLHER.png',
    #                 'COROA.png',
    #                 'DADO.png',
    #                 'BIGODE.png',
    #                 'FLOR.png',
    #                 'FOLHA.png',
    #                 'GALO.png',
    #                 'GARFO.png',
    #                 'GATO.png',
    #                 'JANELA.png',
    #                 'LIVRO.png',
    #                 'LIXO.png',
    #                 'LUA.png',
    #                 'LÁPIS.png',
    #                 'MACACO.png',
    #                 'MAÇÃ.png',
    #                 'MESA.png',
    #                 'MOEDA.png',
    #                 'PORTA.png',
    #                 'PRATO.png',
    #                 'PÃO.png',
    #                 'SALADA.png',
    #                 'SAPO.png',
    #                 'SOL.png',
    #                 'SORVETE.png',
    #                 'TESOURA.png',
    #                 'TREM.png',
    #                 'TÊNIS.png',
    #                 'URSO.png',
    #                 'ÁRVORE.png']
    #     #TODO tentar adicionar por meio de thread 
    #     for arq in arquivos:
    #         # TODO not working
    #         self.add_imagem(
    #             {"nome_imagem": arq})
    #         # print(arq[77:][:-4])

    # # def seleciona_imagem_por(self, id_i):
    # #     self.db.open()
    # #     query = QtSql.QSqlQuery(
    # #         f"SELECT * FROM imagens_atividades WHERE id_imagem = '{id_i}'")
    # #     query.next()
    # #     imagem = {
    # #         "nome_imagem": query.value("nome_imagem")}
    # #     self.db.close()
    # #     return imagem

    def add_conta(self, input_conta):

        self.db.open()
        t = self.query.exec(
            f"""INSERT INTO contas_alunos(
                nome_aluno,
                senha,
                nome_professor,
                email_professor
            ) values(
                '{input_conta["nome_aluno"]}',
                '{input_conta["senha"]}', 
                '{input_conta["nome_professor"]}', 
                '{input_conta["email_professor"]}'
                )"""
        )
        print(f"Resultado adicionado = {t}")
        self.db.close()
        return t

    def atualiza_conta(self, input_conta, id_aluno):
        self.db.open()
        t = self.query.exec(

            f"""UPDATE contas_alunos SET nome_aluno = '{input_conta["nome_aluno"]}',
                senha = '{input_conta["senha"]}',
                nome_professor = '{input_conta["nome_professor"]}',
                email_professor = '{input_conta["email_professor"]}'               
                WHERE id_conta_aluno = '{id_aluno}'"""
        )
        print(f"Resultado atualizado = {t}")
        print(self.query.lastError().text())
        self.db.close()
        return t

    def deleta_conta(self, id_aluno):
        self.db.open()
        t = self.query.exec(
            f"DELETE FROM contas_alunos WHERE id_conta_aluno = '{id_aluno}'")
        print(self.query.lastError().text())
        self.db.close()
        return t

    def seleciona_aluno_por_nome(self, nome_usuario):
        self.db.open()
        usuario = {}
        query = QtSql.QSqlQuery(
            f"SELECT * FROM contas_alunos WHERE nome_aluno = '{nome_usuario}'")
        t = query.next()
        if(t):
            usuario = {
                "id_conta_aluno": query.value("id_conta_aluno"),
                "nome_aluno": query.value("nome_aluno"),
                "senha": query.value("senha"),
                "nome_professor": query.value("nome_professor"),
                "email_professor": query.value("email_professor")}
        else:
            usuario = {
                "id_conta_aluno": None,
                "nome_aluno": None,
                "senha": None,
                "nome_professor": None,
                "email_professor": None}
        self.db.close()
        return usuario

    # TODO salvar nome e sobrenome junto mesmo aaargh
    def seleciona_nomes(self):
        self.db.open()
        # TODO alterar esse query
        query = QtSql.QSqlQuery(f"SELECT * FROM contas_alunos")
        nomes = []
        # query.next()
        # print(query.value("nome_aluno"))
        while(query.next()):
            nomes.append(query.value("nome_aluno"))
        self.db.close()
        return nomes
        # print(query.value(0))

    # def seleciona_tudo_imagens(self):
    #     self.db.open()
    #     query = QtSql.QSqlQuery("SELECT * FROM imagens_atividades")
    #     # print("contas")
    #     imagens = []
    #     while(query.next()):
    #         imagens.append(query.value("nome_imagem"))
    #     # print(query.value(0))
    #     self.db.close()
    #     return imagens


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == '__main__':
    import sys

    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    alfaedu = AlfaEduDB()
    alfaedu.createDB()
    # contas.add_imagens()
    # contas.seleciona_imagem_por_id(1)
    # alfaedu.seleciona_tudo()
    # contas.seleciona_usuario("Mabel1234")
