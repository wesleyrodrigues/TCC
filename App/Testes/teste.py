from PyQt5 import QtWidgets

class View(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        buttons = []
        for i in range(3):
            name = "button{}".format(i+1)
            button = QtWidgets.QPushButton()
            button.setObjectName(name)
            layout.addWidget(button)
            button.setProperty("selected", False)
            button.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            button.clicked.connect(lambda on, i=i: self.setSelected(i))
            buttons.append(button)
        self._buttons = buttons
        self.setLayout(layout)
        self.setStyleSheet("""
        QPushButton:hover { border: 2px solid rgb(0, 0, 0);}
        #button1[selected="false"] {background-color: #cccccc;}
        #button2[selected="false"] {background-color: #cccccc;}
        #button3[selected="false"] {background-color: #cccccc;}

        #button1[selected="true"] {background-color: #ccccff;}
        #button2[selected="true"] {background-color: #ccffcc;}
        #button3[selected="true"] {background-color: #ffcccc;}
        """)

    def setSelected(self, i):
        style = self.style()
        for j, button in enumerate(self._buttons):
            button.setProperty("selected", i == j)
            style.unpolish(button)
            style.polish(button)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    view = View()
    view.show()
    app.exec()