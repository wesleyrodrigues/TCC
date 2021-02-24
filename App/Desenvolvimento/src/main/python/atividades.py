from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtGui import QPixmap

class DigiteNomeDaImagem():
    def __init__(self) -> None:
        self.contador = 2
        self.max_contador = 2
    
    def get_QPixmap_image(self, image):
        return QPixmap(ApplicationContext().get_resource(image))
    
    def set_contador_mais_um(self):
        self.contador += 1
        self.contador = min(self.max_contador - 1, self.contador)
    
    def get_contador(self):
        return self.contador
    
    def set_max_contador(self, num):
        self.max_contador = num



