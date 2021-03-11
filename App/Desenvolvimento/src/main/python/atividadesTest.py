from atividades import Atividades, DigiteNomeDaImagem


ativit = Atividades()
digite_nome_Imagem = DigiteNomeDaImagem()

def test_set_qtd_atividade_mais_um():
    ativit.set_qtd_atividade_mais_um()
    assert ativit.quantidade_atividade_feita == 1

def set_ativades_com_dificulade():
    dict_nome = {"CASA": 1, "PRÉDIO": 3, "ÁRVORE": 7, "GALINHA": 5}
    ativit.set_ativades_com_dificulade(dict_nome)

def test_get_3_atividades_com_dificuldade():
    set_ativades_com_dificulade()
    assert ativit.get_3_atividades_com_dificuldade() == ["ÁRVORE", "GALINHA", "PRÉDIO"]
