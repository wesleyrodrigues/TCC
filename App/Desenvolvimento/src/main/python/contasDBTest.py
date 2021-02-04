from contasDB import Contas
from criptografia import Cript

contasTests = Contas()


def retorna_dic_conta():
    nome_aluno = "Mabel1234"
    sobrenome = "Park"
    senha_cript = Cript.criptografa_senha("RuIVyzVFC8")
    # senha_cript = "RfdsjkalsdjljasdfkljadskjdsakjdfsakuIVyzVFC8"
    nome_professor = "Mason"
    email = "ra@ko.nr"

    return {
        "nome_aluno": nome_aluno,
        "sobrenome_aluno": sobrenome,
        "senha": senha_cript,
        "nome_professor": nome_professor,
        "email_professor": email
    }


def test_createDB():
    assert contasTests.createDB() == True


def test_add_conta():
    assert contasTests.add_conta(retorna_dic_conta()) == True


def test_seleciona_usuario():
    assert contasTests.seleciona_usuario("Mabel1234") == {
        'nome_aluno': 'Mabel1234',
        'sobrenome_aluno': 'Park',
        'senha': '8\x1f\nñÂ£\x8c7úGÖ\x1aÜÍm\x11Ï¯\tx¡\x80X\x15\x17-\x94<9Ñà¸>\xadß¶¬6ó\x07æ_\r\x89\x19íö(<®\x0b~ä÷ÉOå\tûG\x1b¹D\x8a',
        'nome_professor': 'Mason',
        'email_professor': 'ra@ko.nr'
    }
