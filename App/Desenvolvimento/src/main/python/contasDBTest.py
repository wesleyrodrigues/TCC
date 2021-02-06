from contasDB import Contas
from criptografia import Cript

contasTests = Contas()


def retorna_dic_conta():
    nome_aluno = "Mabel1234"
    senha_cript = Cript.criptografa_senha("RuIVyzVFC8")
    # senha_cript = "RfdsjkalsdjljasdfkljadskjdsakjdfsakuIVyzVFC8"
    nome_professor = "Mason"
    email = "ra@ko.nr"

    return {
        "nome_aluno": nome_aluno,
        "senha": senha_cript,
        "nome_professor": nome_professor,
        "email_professor": email
    }


def test_createDB():
    assert contasTests.createDB() == True


def test_add_conta():
    assert contasTests.add_conta(retorna_dic_conta()) == True


# def test_seleciona_usuario():
#     assert contasTests.seleciona_usuario("Mabel1234") == {
#         'nome_aluno': 'Mabel1234',
#         'senha': 'k²°\x9a\x14\x19®î&o[\x08\x82X$RSË\x17øÉ\x8ft2DSol]z»\x0c\x9bmáù\x11¨\x81"ÿF\x88\x97ê2\x10ô\x03\x94l¸¤#ªÁ<\x06ûv>Àrè',
#         'nome_professor': 'Mason',
#         'email_professor': 'ra@ko.nr'
#     }
