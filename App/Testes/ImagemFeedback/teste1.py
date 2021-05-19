from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (1280, 720), "white")
titulo = "Feedback"

font = ImageFont.truetype("arial.ttf", 50)
largura, altura = font.getsize(titulo)

draw = ImageDraw.Draw(img)
# draw.text(((1280-largura)/2, (720-altura)/2), titulo, font=font,fill="black")
draw.text((100, 2), titulo, font=font,fill="black")
img.save("testando.bmp")
# img.show()

