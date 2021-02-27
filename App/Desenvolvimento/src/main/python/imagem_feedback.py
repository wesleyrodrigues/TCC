from PIL import Image, ImageFont, ImageDraw


class Feedback():
    def __init__(self) -> None:
        self.img = Image.new("RGBA", (1280, 720), "white")
        self.titulo = "Feedback"
        self.font = ImageFont.truetype("arial.ttf", 50)
        self.largura, self.altura = self.font.getsize(self.titulo)
        self.draw = ImageDraw.Draw(self.img)
        self.draw.text((100, 2), self.titulo, font=self.font, fill="black")
        # draw.text(((1280-largura)/2, (720-altura)/2), titulo, font=font,fill="black")
        self.img.save("testando.bmp")

    def return_image(self):
        return self.img
# img.show()
