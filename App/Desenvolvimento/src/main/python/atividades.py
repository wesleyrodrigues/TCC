class DigiteNomeDaImagem():
    def __init__(self) -> None:
        self.contador = 0
        self.max_contador = 0
        self.fim = False
    
    def set_contador_mais_um(self):
        self.contador += 1
        self.fim = (self.contador == self.max_contador)
    
    def get_contador(self):
        return self.contador

    def get_fim (self) -> bool:
        return self.fim
    
    def set_max_contador(self, num):
        self.max_contador = num



