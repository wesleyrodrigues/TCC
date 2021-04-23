from random import choice, randint, shuffle


class Atividades():
    def __init__(self) -> None:
        self.atividades_feitas = 0
        self.contador_index = 0
        # {"nome_imagem": 0} -> numero apresentando os erros
        self.atividade_com_dificuldade = {}
        self.max_atividades = 0
        self.fim = False
        self.posic_imagem = 0
        self.posic_letra = 0
        self.acertos = 0
        self.erros = 0
        self.media = 0
    
    def set_acertos_mais_um(self) -> None:
        self.acertos += 1
    
    def get_acertos(self) -> int:
        return self.acertos
    
    def set_erros_mais_um(self) -> None:
        self.erros += 1
    
    def get_erros(self) -> int:
        return self.erros
    
    def set_total_questoes_mais_um(self) -> None:
        self.total_questoes += 1
    
    def get_total_questoes(self) -> int:
        return self.total_questoes

    def set_contador_mais_um(self) -> None:
        self.contador_index += 1
        self.fim = (self.contador_index ==
                    (self.max_atividades - 1))

    def set_atividade_mais_um(self) -> None:
        self.atividades_feitas += 1

    def get_contador(self) -> int:
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

    def set_posic_imagem(self) -> None:
        self.posic_imagem = randint(1, 3)
    
    def set_posic_letra(self) -> None:
        self.posic_letra = randint(1, 4)

    def get_posic_imagem(self) -> int:
        return self.posic_imagem
    
    def get_posic_letra(self) -> int:
        return self.posic_letra

    # TODO melhorar depois
    def get_2_posicao(self) -> int:
        pos2 = self.get_contador() + 3

        if(pos2 < self.max_atividades):
            return pos2
        else:
            return pos2 - self.max_atividades

    def get_3_posicao(self) -> int:
        pos3 = self.get_contador() + 6

        if(pos3 < self.max_atividades):
            return pos3
        else:
            return pos3 - self.max_atividades

# TODO colocar dentro da classe atividades
def reset_atividades(self) -> None:
    self.atividades = Atividades()
    shuffle(self.atv_imagens_bd)
    self.atividades.set_max_atividades(len(self.atv_imagens_bd))


def atv_digite_nome(self):
    input_nome = str(self.ui.input_atv_digt_nome_imagem.text()).strip()
    self.fim_bool = self.atividades.get_fim()
    if (self.fim_bool):
        self.tela_feedback()
        reset_atividades(self)
    else:
        nome_imagem = self.change_label_image(
            self.ui.latv_digt_nome_imagem)
        if(nome_imagem == input_nome):
            self.atividades.set_contador_mais_um()
            self.change_label_image(self.ui.latv_digt_nome_imagem)
            self.ui.input_atv_digt_nome_imagem.setText("")
        else:
            self.atividades.set_erros_mais_um()

# TODO tentar melhorar essa função.


def atv_clique_na_imagem_rand(self):
    posic_imagem = self.atividades.get_posic_imagem()
    nome = ""
    contador = self.atividades.get_contador()
    if(posic_imagem == 1):
        nome = self.change_btn_image(self.ui.btn_imagem_1, contador)
        self.change_btn_image(self.ui.btn_imagem_2,
                              self.atividades.get_2_posicao())
        self.change_btn_image(self.ui.btn_imagem_3,
                              self.atividades.get_3_posicao())
    elif(posic_imagem == 2):
        nome = self.change_btn_image(self.ui.btn_imagem_2, contador)
        self.change_btn_image(self.ui.btn_imagem_1,
                              self.atividades.get_2_posicao())
        self.change_btn_image(self.ui.btn_imagem_3,
                              self.atividades.get_3_posicao())
    else:
        nome = self.change_btn_image(self.ui.btn_imagem_3, contador)
        self.change_btn_image(self.ui.btn_imagem_1,
                              self.atividades.get_2_posicao())
        self.change_btn_image(self.ui.btn_imagem_2,
                              self.atividades.get_3_posicao())

    self.ui.l_nome_imagem.setText(nome)
    return posic_imagem

# recebe número do button clicado
def atv_clique_na_imagem(self, button):
    self.fim_bool = self.atividades.get_fim()

    if (self.fim_bool):
        self.tela_feedback()
        self.reset_atividades()
    else:
        posic_imagem = atv_clique_na_imagem_rand(self)
        if(posic_imagem == button):
            self.atividades.set_contador_mais_um()
            self.atividades.set_posic_imagem()
            atv_clique_na_imagem_rand(self)
        else:
            self.atividades.set_erros_mais_um()

def atv_clique_na_letra_rand(self):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posic_letra = self.atividades.get_posic_letra()
    imagem = self.atv_imagens_bd[self.atividades.get_contador()]
    nome_imagem = imagem[:-4]
    letra_index = randint(0, len(nome_imagem) - 1)
    nome = ""
    letra = ""
    for i in range(0, len(nome_imagem)):
        if(i == letra_index):
            letra = nome_imagem[i]
            alfabeto = alfabeto.replace(letra, "")
            nome += "_"
        else:
            nome += nome_imagem[i]
    # print(nome)
    self.ui.l_palavra.setText(nome)

    c1 = choice(alfabeto) # escolhe uma letra do alfabeto
    alfabeto = alfabeto.replace(c1, "") # Remove a letra escolhida para que não repita
    c2 = choice(alfabeto)
    alfabeto = alfabeto.replace(c2, "")
    c3 = choice(alfabeto)
    alfabeto = alfabeto.replace(c3, "")
    c4 = choice(alfabeto)
    alfabeto = alfabeto.replace(c4, "")

    self.ui.btn_letra_1.setText(c1) # define a letra no botão
    self.ui.btn_letra_2.setText(c2)
    self.ui.btn_letra_3.setText(c3)
    self.ui.btn_letra_4.setText(c4)
    
    if(posic_letra == 1):
        self.ui.btn_letra_1.setText(letra)
    elif(posic_letra == 2):
        self.ui.btn_letra_2.setText(letra)
    elif(posic_letra == 3):
        self.ui.btn_letra_3.setText(letra)
    else:
        self.ui.btn_letra_4.setText(letra)
    
    return posic_letra


def atv_clique_na_letra(self, button):
    self.fim_bool = self.atividades.get_fim()

    if (self.fim_bool):
        self.tela_feedback()
        reset_atividades(self)
    else:
        posic_letra = atv_clique_na_letra_rand(self)
        if(posic_letra == button):
            self.atividades.set_contador_mais_um()
            self.atividades.set_posic_letra()
            atv_clique_na_letra_rand(self)
        else:
            self.atividades.set_erros_mais_um()
