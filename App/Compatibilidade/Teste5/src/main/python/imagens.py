from PyQt5 import QtSql, QtWidgets


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('imagens.db')

    if not db.open():
        QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
                                   QtWidgets.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtWidgets.QMessageBox.Cancel)

        return False

    query = QtSql.QSqlQuery()

    query.exec_("create table imagenspng(id int primary key, "
                "nome varchar(20))")

    query.exec_("insert into imagenspng values(1, 'casa')")
    query.exec_("insert into imagenspng values(2, 'arvore')")
    return True


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    createDB()
