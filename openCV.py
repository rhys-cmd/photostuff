from cv2 import VideoCapture, imshow, waitKey, destroyWindow
from math import dist

cam = VideoCapture(0)
result, image = cam.read()
imshow('cam',image)

while result:
    result, image = cam.read()
    imshow('cam', image)
    width, height, _= image.shape
    best = 1000
    best_pos = (0, 0)
    for y in range(height):
        for x in range(width):
            b, g, r, = image[y, x]
            d = dist(image[y, x], (0, 0, 255))
            if d < best:
                best = best_pos(x, y)

    try:
        for y in range(-10, 10):
            for x in range(-10, 10):
                image[best_pos[1]+y, best_pos[0]+x] = (255, 255, 255)
    
    except IndentationError:
        pass
            

    key = waitKey(20)
    if key == 27:
        break
