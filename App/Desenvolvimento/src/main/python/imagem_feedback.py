from PIL import Image, ImageFont, ImageDraw
from os import path, listdir
from pathlib import Path


class Feedback():
    def __init__(self) -> None:
        self.img = Image.new("RGBA", (1280, 720), "white")
        self.back = Image.open("backFeed.png")
        self.img.paste(self.back)
        self.font = ImageFont.truetype("arial.ttf", 30)
        self.draw = ImageDraw.Draw(self.img)
        self.img.save("feedback.bmp")

    def get_imagem(self) -> str:

        pasta = str(Path().absolute())

        caminhos = [path.join(pasta, nome) for nome in listdir(pasta)]
        arquivo = [arq for arq in caminhos if path.isfile(
            arq) and arq.lower().endswith(".bmp")]
        return arquivo[0]

    def set_feedback_imagem(self, dict_feedback):
        nome_aluno = "Aluno: " + dict_feedback["nome_aluno"]
        nome_professor = "Professor: " + dict_feedback["nome_professor"]
        tempo_proposto = "Tempo proposto pelo Professor: " + dict_feedback["tempo_proposto"]
        tempo_executado = "Tempo executado pelo Aluno: " +  dict_feedback["tempo_executado"]
        total_questoes = "Total de questões respondidas: " + dict_feedback["total_questoes"]
        acertos = "Acertos: " + dict_feedback["acertos"]
        erros = "Erros: " + dict_feedback["erros"]
        atividades_dificuldade = "Palavras com dificuldade: " + dict_feedback["atividade_dificuldade"]

        lista = ["Feedback", nome_aluno, nome_professor, tempo_proposto, 
                  tempo_executado, total_questoes, acertos, erros, atividades_dificuldade]
        posit = 158

        for str_nome in lista:
            self.draw.text((250, posit), str_nome, font=self.font, fill="black")
            # self.draw.line((0,posit+1, 0, 500), fill=128, width=1)
            posit += 40

        # self.draw.text((100, 52), nome_aluno, font=self.font, fill="black")
        # self.draw.text((100, 102), nome_professor, font=self.font, fill="black")
        # self.draw.text((100, 152), tempo_proposto, font=self.font, fill="black")
        # self.draw.text((100, 202), tempo_executado, font=self.font, fill="black")
        # self.draw.text((100, 252), total_questoes, font=self.font, fill="black")
        # self.draw.text((100, 300), acertos, font=self.font, fill="black")
        # self.draw.text((100, 352), erros, font=self.font, fill="black")
        self.img.save("feedback.bmp")


# img.show()
