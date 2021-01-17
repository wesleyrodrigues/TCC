from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (900, 900), "white")
string1 = "Testando"

font = ImageFont.truetype("arial.ttf", 75)
w,h = font.getsize(string1)

draw = ImageDraw.Draw(img)
draw.text(((900-w)/2, (900-h)/2), string1, font=font,fill="black")
img.save("testando.bmp")
# img.show()