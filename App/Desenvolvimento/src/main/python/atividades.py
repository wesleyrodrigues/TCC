class Atividades():
    def __init__(self) -> None:
        self.quantidade_atividade_feita = 0
        # {"nome_imagem": 0} -> numero apresentando os erros
        self.atividade_com_dificuldade = {}
    
    def set_qtd_atividade_mais_um(self):
        self.quantidade_atividade_feita += 1
    
    def set_ativades_com_dificulade(self, dict_nome):
        self.atividade_com_dificuldade.update(dict_nome)
    
    def get_3_atividades_com_dificuldade(self):
        dic = self.atividade_com_dificuldade
        list_atividade = sorted(dic, key = dic.get, reverse = True)
        return list_atividade[:3]


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
    
    



