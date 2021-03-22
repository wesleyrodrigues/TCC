from random import randint

class Atividades():
    def __init__(self) -> None:
        self.atividades_feitas = 0
        self.contador_index = 0
        # {"nome_imagem": 0} -> numero apresentando os erros
        self.atividade_com_dificuldade = {}
        self.max_atividades = 0
        self.fim = False
        self.posic_imagem = 0

    def set_contador_mais_um(self) -> None:
        self.contador_index += 1
        self.fim = (self.contador_index ==
                    (self.max_atividades - 1))

    def set_atividade_mais_um(self) -> None:
        self.atividades_feitas += 1

    def get_contador(self):
        return self.contador_index

    def get_atividades_feitas(self) -> int:
        return self.atividades_feitas

    def get_fim(self) -> bool:
        return self.fim

    def set_max_atividades(self, num) -> None:
        self.max_atividades = num

    def set_ativades_com_dificulade(self, dict_nome) -> None:
        self.atividade_com_dificuldade.update(dict_nome)

    def get_3_atividades_com_dificuldade(self) -> None:
        dic = self.atividade_com_dificuldade
        list_atividade = sorted(dic, key=dic.get, reverse=True)
        return list_atividade[:3]

    def set_posic_imagem(self):
        self.posic_imagem = randint(1, 3)
    
    def get_posic_imagem(self):
        return self.posic_imagem
    
    # TODO melhorar depois
    def get_2_posicao(self):
        pos2 = self.get_contador() + 3
        
        if(pos2 < self.max_atividades):
            return pos2
        else:
            return pos2 - self.max_atividades

    def get_3_posicao(self):
        pos3 = self.get_contador() + 6
        
        if(pos3 < self.max_atividades):
            return pos3
        else:
            return pos3 - self.max_atividades