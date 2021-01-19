from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtSql
from Test4 import Ui_MainWindow
from DB import DBImagens

import sys, os

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        DBImagens.createDBImagens(1)

        # self.ui.btnsair.setText("saindo")
        pasta_imagens = os.path.abspath("imagens")
        # query = QtSql.QSqlQuery("""SELECT * FROM nomesimagens""")
        # print(query.next())
        # self.ui.lblimage.setPixmap(QtGui.QPixmap(pasta_imagens + "/" ))

def main():
    app = QApplication(sys.argv)
    application = ApplicationWindow()
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