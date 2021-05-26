from imagem_feedback import Feedback

feedback_test = Feedback()

feedback_test.set_feedback_imagem(
    {
        "nome_aluno": "Wesley",
        "nome_professor": "Josefina",
        "tempo_proposto": "01:00",
        "tempo_executado": "01:00",
        "total_questoes": "10",
        "acertos": "10",
        "erros": "0",
        "atividade_dificuldade": "0"
    }
)

feedback_test.get_imagem()