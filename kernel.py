from PIL import Image, ImageFilter

im = Image.open("forest.jpg")
im = im.filter(Image.Filter.Kernel((3, 3), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)))

im.show()