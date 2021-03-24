# TODO melhorar depois

def mensagens_erros_cadastro(self, arg):
    line_input_cadastro = self.get_input_cadastro()
    self.ui.lcampos.setText("")
    if(arg == "nome_aluno"):
        for count in range(self.ui.cb_nome_aluno.count()):
            if(line_input_cadastro["nome_aluno"] == self.ui.cb_nome_aluno.itemText(count)):
                msg = "Nome do(a) aluno(a), já cadastrado\n"
                self.ui.lverifica_nome.setText(msg)
                return False
        self.ui.lverifica_nome.setText("")
        return True

    # TODO redundancia de ifs em senha e conf_senha
    elif(arg == "senha" or arg == "conf_senha"):
        if(line_input_cadastro["conf_senha"] == ""
           or line_input_cadastro["senha"] == ""):
            self.ui.lverifica_senha.setText("")

        if(line_input_cadastro["conf_senha"] != ""):
            if(line_input_cadastro["senha"] != line_input_cadastro["conf_senha"]):
                msg = "As senhas não são iguais. Tente novamente.\n"
                self.ui.lverifica_senha.setText(msg)
                return False
            self.ui.lverifica_senha.setText("")
            return True

    # TODO redundancia de ifs em email e conf email
    elif(arg == "email" or arg == "conf_email"):
        if(line_input_cadastro["conf_email"] == ""
           or line_input_cadastro["email_professor"] == ""):
            self.ui.lverifica_email.setText("")

        if(line_input_cadastro["conf_email"] != ""):
            if(line_input_cadastro["email_professor"] != line_input_cadastro["conf_email"]):
                msg = "Os emails não são iguais. Tente novamente.\n"
                self.ui.lverifica_email.setText(msg)
                return False
            self.ui.lverifica_email.setText("")
            return True
