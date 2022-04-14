from itertools import permutations
from PIL import Image, ImageDraw, ImageFont

font_file = 'iranian-sans/irsans.ttf'
فونت = ImageFont.truetype(font_file, 16)

# اجزا = ["نگارینا", "چرا کردی", "بدین زردی", "رخان من"]
اجزا = ["ای بی وفا", "بر عاشقان", "رحمی بکن", "بهر خدا"]

مصرعها = list(permutations(اجزا))
img = Image.new("L", (384, len(مصرعها) * 30), color=255)
draw = ImageDraw.Draw(img)

for خط, مصرع in enumerate(مصرعها):
    draw.text((0, خط * 30), " ".join(مصرع), font=فونت)
img.save("همه مصرعها - "+اجزا[0]+".png")

c = 1
