from PyQt5 import QtSql, QtWidgets
from os import environ


class Contas(QtSql.QSqlDatabase):

    def __init__(self) -> None:
        super(Contas, self).__init__()
        # TODO verificar depois essa conexão
        self.db = self.addDatabase('QSQLITE')
        self.db.setDatabaseName('contas_alunos.db')
        self.query = QtSql.QSqlQuery()

    def createDB(self) -> bool:
        print("teste")
        # db = self.addDatabase('QSQLITE')
        # db.setDatabaseName('contas.db')

        if not self.db.open():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
                                           QtWidgets.qApp.tr("Unable to establish a database connection.\n"
                                                             "This example needs SQLite support. Please read "
                                                             "the Qt SQL driver documentation for information "
                                                             "how to build it.\n\n" "Click Cancel to exit."),
                                           QtWidgets.QMessageBox.Cancel)

            return False

        # TODO criptografar senha.
        self.query.exec(
            """CREATE TABLE IF NOT EXISTS contas_alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                nome_aluno varchar,
                sobrenome_aluno varchar,
                senha varchar,
                nome_professor varchar,
                email_professor varchar
                )"""
        )

        # query.exec("insert into imagenspng values(1, 'casa')")
        # query.exec("insert into imagenspng values(2, 'arvore')")
        self.db.close()
        return True

    def add_conta(self, input_conta):

        self.db.open()
        # TODO verificar por que não está salvando
        t = self.query.exec(
            f"""INSERT INTO contas_alunos(
                nome_aluno,
                sobrenome_aluno,
                senha,
                nome_professor,
                email_professor
            ) values(
                '{input_conta["nome_aluno"]}',
                '{input_conta["sobrenome_aluno"]}', 
                '{input_conta["senha"]}', 
                '{input_conta["nome_professor"]}', 
                '{input_conta["email_professor"]}'
                )"""
        )
        print(t)
        self.db.close()
        return t

    def seleciona_tudo(self):
        self.db.open()
        query = QtSql.QSqlQuery("SELECT * FROM contas_alunos")
        print("contas")
        while(query.next()):
            print(
                f"""
                {query.value("nome_aluno")},
                {query.value("sobrenome_aluno")},
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
    contas = Contas()
    contas.createDB()
    contas.seleciona_tudo()
