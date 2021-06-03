from PyQt5 import QtSql, QtWidgets
from os import environ
import sys


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

        self.db.close()
        return True

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
