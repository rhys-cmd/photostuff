from PIL import Image

im = Image.open("stopsign.jpeg")

px = im.load()

for y in range(im.height):
    for x in range(im.width):
        r, g, b, = px[x, y]
        if r > 130 and g > 11 and b < 13:
            px[x ,y] = (0, 0, 0)
        
        else:
            px[x, y] = (0, 0, 0)

im.show()