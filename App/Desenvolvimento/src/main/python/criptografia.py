import hashlib

class Cript():
    def criptografa_senha(senha):
        resultado = hashlib.md5(senha.encode("utf-8")).hexdigest()
        return resultado

    def verifica_usuario_e_senha(senha_cript, senha):
        return hashlib.md5(senha.encode("utf-8")).hexdigest() == senha_cript