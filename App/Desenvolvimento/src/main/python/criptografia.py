# import bcrypt
import hashlib
import os

#TODO não funciona em produção
class Cript():
    def criptografa_senha(senha):
        # hashed = bcrypt.hashpw(senha.encode('utf_8'), bcrypt.gensalt())
        # return hashed.decode("utf-8")
        return senha

    def verifica_usuario_e_senha(usuario, senha, senha_cript):
        # return bcrypt.checkpw(senha.encode('utf_8'), senha_cript)
        return senha
