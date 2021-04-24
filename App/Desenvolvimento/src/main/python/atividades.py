from random import choice, randint, shuffle


class Atividades():
    def __init__(self) -> None:
        self.contador_index = 0
        # {"nome_imagem": 0} -> numero apresentando os erros
        self.atividade_feitas = {}
        self.max_atividades = 0
        self.fim = False
        self.posic_imagem = 0
        self.posic_letra = 0

    def get_acertos(self) -> int:
        atividades = list(self.atividade_feitas.values())
        return atividades.count(1)

    def get_erros(self) -> int:
        return self.contador_index - self.get_acertos()

    def set_atividades_feitas(self, arg) -> None:
        keys_atividades = list(self.atividade_feitas.keys())

        if(arg in keys_atividades):
            value = self.atividade_feitas.get(arg)
            self.atividade_feitas.update({arg: value + 1})
        else:
            if(len(keys_atividades) == 0):
                # evite que primeiro adicione mais um
                self.atividade_feitas.update({arg: 0})
            else:
                self.atividade_feitas.update({arg: 1})

        # print(self.atividade_feitas)

    def set_total_questoes_mais_um(self) -> None:
        self.total_questoes += 1

    def get_total_questoes(self) -> int:
        return self.total_questoes

    def set_contador_mais_um(self) -> None:
        self.contador_index += 1
        self.fim = (self.contador_index == self.max_atividades - 1)

    def get_contador(self) -> int:
        return self.contador_index

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

    def reset_atividades(self, main_app) -> None:
        main_app.atividades = Atividades()
        shuffle(main_app.atv_imagens_bd)
        self.set_max_atividades(len(main_app.atv_imagens_bd))

    def atv_digite_nome(self, main_app):
        input_nome = str(main_app.ui.input_atv_digt_nome_imagem.text()).strip()
        if (self.get_fim()):
            main_app.tela_feedback()
            self.reset_atividades(main_app)
        else:
            nome_imagem = main_app.change_label_image(
                main_app.ui.latv_digt_nome_imagem)
            if(nome_imagem == input_nome):
                self.set_contador_mais_um()
                main_app.change_label_image(main_app.ui.latv_digt_nome_imagem)
                main_app.ui.input_atv_digt_nome_imagem.setText("")
                self.set_atividades_feitas(nome_imagem)
            else:
                self.set_atividades_feitas(nome_imagem)

    def atv_clique_na_imagem_rand(self, main_app):
        posic_imagem = self.get_posic_imagem()
        nome = ""
        contador = self.get_contador()
        if(posic_imagem == 1):
            nome = main_app.change_btn_image(
                main_app.ui.btn_imagem_1, contador)
            main_app.change_btn_image(main_app.ui.btn_imagem_2,
                                      self.get_2_posicao())
            main_app.change_btn_image(main_app.ui.btn_imagem_3,
                                      self.get_3_posicao())
        elif(posic_imagem == 2):
            nome = main_app.change_btn_image(
                main_app.ui.btn_imagem_2, contador)
            main_app.change_btn_image(main_app.ui.btn_imagem_1,
                                      self.get_2_posicao())
            main_app.change_btn_image(main_app.ui.btn_imagem_3,
                                      self.get_3_posicao())
        else:
            nome = main_app.change_btn_image(
                main_app.ui.btn_imagem_3, contador)
            main_app.change_btn_image(main_app.ui.btn_imagem_1,
                                      self.get_2_posicao())
            main_app.change_btn_image(main_app.ui.btn_imagem_2,
                                      self.get_3_posicao())

        main_app.ui.l_nome_imagem.setText(nome)
        return [posic_imagem, nome]

    # recebe número do button clicado
    def atv_clique_na_imagem(self, main_app, button):

        if (self.get_fim()):
            main_app.tela_feedback()
            self.reset_atividades()
        else:
            posic_imagem = self.atv_clique_na_imagem_rand(main_app)
            if(posic_imagem[0] == button):
                self.set_contador_mais_um()
                self.set_posic_imagem()
                self.atv_clique_na_imagem_rand(main_app)
                self.set_atividades_feitas(posic_imagem[1])
            else:
                self.set_atividades_feitas(posic_imagem[1])

    def atv_clique_na_letra_rand(self, main_app):
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        posic_letra = self.get_posic_letra()
        imagem = main_app.atv_imagens_bd[self.get_contador()]
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
        main_app.ui.l_palavra.setText(nome)

        c1 = choice(alfabeto)  # escolhe uma letra do alfabeto
        # Remove a letra escolhida para que não repita
        alfabeto = alfabeto.replace(c1, "")
        c2 = choice(alfabeto)
        alfabeto = alfabeto.replace(c2, "")
        c3 = choice(alfabeto)
        alfabeto = alfabeto.replace(c3, "")
        c4 = choice(alfabeto)
        alfabeto = alfabeto.replace(c4, "")

        main_app.ui.btn_letra_1.setText(c1)  # define a letra no botão
        main_app.ui.btn_letra_2.setText(c2)
        main_app.ui.btn_letra_3.setText(c3)
        main_app.ui.btn_letra_4.setText(c4)

        if(posic_letra == 1):
            main_app.ui.btn_letra_1.setText(letra)
        elif(posic_letra == 2):
            main_app.ui.btn_letra_2.setText(letra)
        elif(posic_letra == 3):
            main_app.ui.btn_letra_3.setText(letra)
        else:
            main_app.ui.btn_letra_4.setText(letra)

        return [posic_letra, nome_imagem]

    def atv_clique_na_letra(self, main_app, button):

        if (self.get_fim()):
            main_app.tela_feedback()
            self.reset_atividades(main_app)
        else:
            posic_letra = self.atv_clique_na_letra_rand(main_app)
            if(posic_letra[0] == button):
                self.set_contador_mais_um()
                self.set_posic_letra()
                self.atv_clique_na_letra_rand(main_app)
                self.set_atividades_feitas(posic_letra[1])
            else:
                self.set_atividades_feitas(posic_letra[1])
