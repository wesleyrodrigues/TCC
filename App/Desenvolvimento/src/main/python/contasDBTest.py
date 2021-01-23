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



