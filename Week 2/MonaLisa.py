"""
Summary: Was having trouble with image.open so I went with open, I think its because it's a text
file it's trying to open and with Image.open I dont think txt is supported... because its not a image.
Then did readlines() to read all the lines. But that was a quick fix, the challenge for me was lines 28
to 21 turning the pixel values into integers and had to look up how that happens for python as
I've yet to deal with many images while coding, so those 4 lines aren't my own. The rest is from the slides
and I don't want to talk about how long it took me to figure out that for the file path I only put the file
name and not the entire path before it because terminal is already in that file directory with the text file,
but the lab is complete.
"""
from PIL import Image

# Read pixel values from the text file
with open('mona.txt', 'r') as file:
    lines = file.readlines()

# Parse pixel values and convert them to integers
pixels = []
for line in lines:
    row = [int(val) for val in line.strip().split('\t')]
    pixels.append(row)

# Get the x and y for the image
x = len(pixels[0])
y = len(pixels)

# Create the new grayscale image!
img = Image.new('L', (x, y))

# Place the pixel values of the image
for x in range(x):
    for y in range(y):
        img.putpixel((x, y), pixels[y][x])

# Save the image
img.save('new_mona.png')