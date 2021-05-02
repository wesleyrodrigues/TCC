from PIL import Image, ImageFont, ImageDraw
from os import path, listdir
from pathlib import Path


class Feedback():
    def __init__(self) -> None:
        self.img = Image.new("RGBA", (1280, 720), "white")
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
        tempo_proposto = "Tempo proposto pelo Professor ou Responsável: " + dict_feedback["tempo_proposto"]
        tempo_executado = "Tempo executado pelo Aluno: " +  dict_feedback["tempo_executado"]
        total_questoes = "Total de questões respondidas: " + dict_feedback["total_questoes"]
        acertos = "Acertos: " + dict_feedback["acertos"]
        erros = "Erros: " + dict_feedback["erros"]

        lista = ["Feedback", nome_aluno, nome_professor, tempo_proposto, 
                  tempo_executado, total_questoes, acertos, erros]
        posit = 10

        for str_nome in lista:
            self.draw.text((100, posit), str_nome, font=self.font, fill="black")
            posit += 50

        # self.draw.text((100, 52), nome_aluno, font=self.font, fill="black")
        # self.draw.text((100, 102), nome_professor, font=self.font, fill="black")
        # self.draw.text((100, 152), tempo_proposto, font=self.font, fill="black")
        # self.draw.text((100, 202), tempo_executado, font=self.font, fill="black")
        # self.draw.text((100, 252), total_questoes, font=self.font, fill="black")
        # self.draw.text((100, 300), acertos, font=self.font, fill="black")
        # self.draw.text((100, 352), erros, font=self.font, fill="black")
        self.img.save("feedback.bmp")


# img.show()
