"""
Carson Mehl
Cst205
6/8/2024
Project: Using image from PIL display a name and save it to an image.
"""

from PIL import Image, ImageDraw
import random

# Generate a dark 8-bit color
my_color = random.randint(0, 150)

# Enter your name here as a string
my_name = 'Carson Mehl'

# Create 8-bit grayscale image of size 200x200 using
# the randomly-generated 8-bit color
img = Image.new('L', (200,200), color = my_color)

# add text to drawing at position (30,30)
# in white
my_text = ImageDraw.Draw(img)
my_text.text((30, 30), my_name, fill=255)

# save image as task4.png
img.save('task4.png')