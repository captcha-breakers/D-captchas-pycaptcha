from captcha.image import ImageCaptcha
from os import system, listdir
from random import choices
from string import ascii_uppercase
from IPython.display import Image
from time import time
from PIL import ImageFont
import sys

# You need a font for reference
image = ImageCaptcha(fonts=["./fonts/"+i for i in listdir("./fonts/")])

system("mkdir -p data")
base_dir = "./data/"
start = time()

# Total images
n = int(sys.argv[1])  # Total captchas needs to be generated
for i in range(n):
    value = ''.join(choices(ascii_uppercase, k=6))
    data = image.generate(value)
    name = base_dir+value+'.png'
    image.write(value, name)

end = time()
print("Time consumed: ", end - start)
