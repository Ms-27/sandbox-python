from PIL import Image, ImageDraw
from math import comb


source = Image.new("RGB", (1200, 500), color = "white")
draw = ImageDraw.Draw(source)

x = 0
for n in range (1,23):
    for i in range(n + 1):
        r = comb(n, i)
        for j in range(30):
            y = 400 - 4 * j
            if r & 2 ** j:
                draw.rectangle(((x, y), (x + 4, y + 4)), fill = 'black')
        x += 4  

source.show()