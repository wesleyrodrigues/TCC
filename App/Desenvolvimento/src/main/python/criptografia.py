import bcrypt


class Cript():  
    def criptografa_senha(senha):
         # Hash a password for the first time, with a randomly-generated salt
        hashed = bcrypt.hashpw(senha.encode('utf_8'), bcrypt.gensalt())
        return hashed
    
    def verifica_senha(senha, senha_cript):
        #TODO buscar senha no banco de dados
        return bcrypt.checkpw(senha.encode('utf_8'), senha_cript) 

