from PIL import Image

im = Image.open("stopsign.jpeg")

px = im.load()

for y in range(im.height):
    for x in range(im.width):
        r, g, b, = px[x, y]
        if r > 128 and g > 50 and b < 20:
            px[x ,y] = (255, 255, 255)
        
        else:
            px[x, y] = (0, 0, 0)

im.show()