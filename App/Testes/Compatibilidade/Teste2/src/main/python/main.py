from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication
from Test2 import Ui_MainWindow

import sys

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


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