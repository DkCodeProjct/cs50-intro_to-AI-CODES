import math
import sys

from PIL import Image, ImageFilter

img = Image.open('cv.jpg').convert('RGB')


filtrd = img.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[
        -1, -1, -1,
        -1,  8, -1,
        -1, -1, -1
    ],
    scale=1

))

filtrd.save('outputcv.jpg')
filtrd.show()