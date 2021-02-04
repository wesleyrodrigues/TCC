# import bcrypt
import hashlib
import os

class Cript():
    def criptografa_senha(senha):
        
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', senha.encode('latin-1'), salt, 100000)

        senha_cript = salt + key
        # hashed = bcrypt.hashpw(senha.encode('utf_8'), bcrypt.gensalt())
        # return hashed.decode("utf-8")
        return senha_cript.decode('latin-1')

    def verifica_usuario_e_senha(usuario, senha, senha_cript):
        senha_cript = senha_cript.encode('latin-1')
        salt = senha_cript[:32]
        key = senha_cript[32:]
        new_key = hashlib.pbkdf2_hmac('sha256', senha.encode('latin-1'), salt, 100000)
        print(new_key)
        return key == new_key