from PyQt5 import QtWidgets, uic


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        uic.loadUi(ui, self)