from PyQt5 import QtSql, QtWidgets
from os import environ, path, listdir


class AlfaEduDB(QtSql.QSqlDatabase):

    def __init__(self) -> None:
        super(AlfaEduDB, self).__init__()
        self.db = self.addDatabase('QSQLITE')
        self.db.setDatabaseName('alfa_edu.db')
        self.query = QtSql.QSqlQuery()

    def createDB(self) -> bool:

        if not self.db.open():
            erro = str(self.query.lastError().text())
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Não é possível abrir o banco de dados"),
                                           QtWidgets.qApp.tr(
                f"{erro} Não foi possível estabelecer uma conexão com o banco de dados.\n"
                "Este exemplo precisa de suporte SQLite. Por favor leia "
                "a documentação do driver Qt SQL para informações "
                "como faze-lo.\n\n" "Click Cancelar para sair."),
                QtWidgets.QMessageBox.Cancel)
	   

            return False

        # TODO BLOB não funciona salvar pasta imagens, por enquanto.
        t = self.query.exec(
            """CREATE TABLE IF NOT EXISTS imagens_atividades(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                nome_imagem varchar NOT NULL UNIQUE,
                pasta_imagem varchar NOT NULL UNIQUE
                )"""
        )

        self.query.exec(
            """CREATE TABLE IF NOT EXISTS contas_alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                nome_aluno varchar NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                nome_professor varchar NOT NULL,
                email_professor varchar NOT NULL
                )"""
        )

        self.db.close()
        return True

    def add_imagem(self, input_conta):

        self.db.open()
        self.query.prepare("INSERT INTO imagens_atividades (nome_imagem, pasta_imagem) "
                           "VALUES (:nome_imagem, :pasta_imagem)")

        self.query.bindValue(":nome_imagem", input_conta["nome_imagem"])
        self.query.bindValue(":pasta_imagem", input_conta["pasta_imagem"])
        t = self.query.exec_()

        print(f"""Resultado {input_conta["nome_imagem"]} = {t}""")
        print(self.query.lastError().text())
        self.db.close()
        return t

    # TODO verificar o que fazer com essa função depois
    def add_imagens(self):
        import pathlib
        pasta = str(pathlib.Path().absolute())

        caminhos = [path.join(pasta, nome) for nome in listdir(pasta)]
        arquivos = [arq for arq in caminhos if path.isfile(
            arq) and arq.lower().endswith(".png")]
        # pngs = [arq for arq in arquivos if arq.lower().endswith(".png")]
        arquivos_nomes = [arq[77:][:-4] for arq in arquivos]

        for arq in arquivos:
            # TODO not working
            self.add_imagem(
                {"nome_imagem": arq[77:][:-4], "pasta_imagem": arq[49:]})
            print(arq[77:][:-4])

    def seleciona_imagem_por(self, id_i):
        self.db.open()
        query = QtSql.QSqlQuery(
            f"SELECT * FROM imagens_atividades WHERE id = '{id_i}'")
        query.next()
        imagem = {
            "nome_imagem": query.value("nome_imagem"),
            "imagem": query.value("pasta_imagem")}
        self.db.close()
        return imagem

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

    def seleciona_usuario_por_nome(self, nome_usuario):
        self.db.open()
        query = QtSql.QSqlQuery(
            f"SELECT * FROM contas_alunos WHERE nome_aluno = '{nome_usuario}'")
        query.next()
        usuario = {
            "nome_aluno": query.value("nome_aluno"),
            "senha": query.value("senha"),
            "nome_professor": query.value("nome_professor"),
            "email_professor": query.value("email_professor")}
        self.db.close()
        return usuario

    # TODO salvar nome e sobrenome junto mesmo aaargh
    def seleciona_nomes(self):
        self.db.open()
        # TODO alterar esse query
        query = QtSql.QSqlQuery("SELECT * FROM contas_alunos")
        nomes = []
        # query.next()
        # print(query.value("nome_aluno"))
        while(query.next()):
            nomes.append(query.value("nome_aluno"))
        print(nomes)
        self.db.close()
        return nomes
        # print(query.value(0))

    def seleciona_tudo(self):
        self.db.open()
        query = QtSql.QSqlQuery("SELECT * FROM contas_alunos")
        print("contas")
        while(query.next()):
            print(
                f"""
                {query.value("nome_aluno")},
                {query.value("senha")},
                {query.value("nome_professor")},
                {query.value("email_professor")},
                 """
            )
        # print(query.value(0))
        self.db.close()


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
    # contas.seleciona_tudo()
    # contas.seleciona_usuario("Mabel1234")
