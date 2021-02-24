from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtGui import QPixmap

class DigiteNomeDaImagem():
    def __init__(self) -> None:
        pass
    
    def get_QPixmap_image(image):
        return QPixmap(ApplicationContext().get_resource(image))


