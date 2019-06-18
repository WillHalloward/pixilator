from PIL import Image

im = Image.open("erin.png")
wight = int(im.size[0]/2)
height = int(im.size[1]/2)
img = Image.new('RGB', (wight, height))
x, y = 0, 0
for z in range(wight):
    for i in range(height):
        tuple1 = im.getpixel((x, y))
        tuple2 = im.getpixel((x + 1, y))
        tuple3 = im.getpixel((x + 1, y + 1))
        tuple4 = im.getpixel((x, y + 1))
        avg = (int((tuple1[0] + tuple2[0] + tuple3[0] + tuple4[0]) / 4),
               int((tuple1[1] + tuple2[1] + tuple3[1] + tuple4[1]) / 4),
               int((tuple1[2] + tuple2[2] + tuple3[2] + tuple4[2]) / 4))
        img.putpixel((z, i), avg)
        y += 2
    x += 2
    y = 0
img.save("pixilated.png")
