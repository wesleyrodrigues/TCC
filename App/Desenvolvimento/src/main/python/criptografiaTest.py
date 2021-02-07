from criptografia import Cript

senha_cript = Cript.criptografa_senha("123456")
    
def test_verifica_usuario_senha():
    assert Cript.verifica_usuario_e_senha(senha_cript, "123456")

