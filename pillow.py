from PIL import Image

im = Image.open("forest.jpg")
px = im.load()
out = im.copy()
outpx = out.load()


def get_greyscale(x, y):
    return sum(px[x, y]) // 3





def get_av(center_x, center_y, d):
    av = 0
    count = 0

    for y in range(center_y-d, center_y + 1 + 1):
        for x in range(center_x - d, center_x + d + 1):
            try:
                av += get_greyscale(x, y)
                count += 1 
            except IndexError:
                pass
            return av // count 


for y in range(im.height): 
    for x in range(im.width):
        r, g, b = px[x, y] = get_av(x, y, 1)

out.show()

print(get_greyscale(0, 0))