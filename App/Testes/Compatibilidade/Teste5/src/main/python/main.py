from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtSql
from Test4 import Ui_MainWindow

import sys, os

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pasta_imagens = pasta_imagens = os.path.abspath("imagens")
    
    def mostrarcasa(self):
        query = QtSql.QSqlQuery("""SELECT nome FROM imagenspng WHERE id=1""")
        query.next()
        # query.next()
        self.ui.lblimage.setPixmap(QtGui.QPixmap(self.pasta_imagens + "/" + query.value(0) + ".png"))
    

def main():
    app = QApplication(sys.argv)
    application = ApplicationWindow()
    
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('imagens.db')
    db.open()

    application.ui.btnescimage.clicked.connect(ApplicationWindow.mostrarcasa)

    application.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()



# if __name__ == '__main__':
#     appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
#     window = QMainWindow()
#     window.resize(250, 150)
#     window.show()
#     exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
#     sys.exit(exit_code)