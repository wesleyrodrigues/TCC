class DigiteNomeDaImagem():
    def __init__(self) -> None:
        self.contador = 2
        self.max_contador = 2
    
    def set_contador_mais_um(self):
        self.contador += 1
        self.contador = min(self.max_contador - 1, self.contador)
    
    def get_contador(self):
        return self.contador
    
    def set_max_contador(self, num):
        self.max_contador = num



