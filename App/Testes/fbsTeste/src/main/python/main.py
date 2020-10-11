from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import sys

if __name__ == '__main__':
    Form, Window = uic.loadUiType("main.ui")
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    form = Form()
    form.setupUi(window)
    # window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)