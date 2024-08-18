"""
Summary: Task 1 was I had trouble because I left out the * 3 after the parenthesis.
Task three was the hardest part and used the code from the lab. I was confused on 
how to count the occurences so lines 53, 54, 58 were suggested from GitHub Copilet.
The last tasks were from the given slides. The comparison png is submitted with the
left side being the Average grayscale method used and then the right side is the 
Luminous Method, and the Luminous method looks to be a little bit brighter.
"""
from PIL import Image
from colorthief import ColorThief
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy

# Task 1 ------------------
img = Image.open('RGB.png')

# Using the Average method add them all and divide by three for all three
new_list = [((r + g + b) // 3, ) * 3 for (r, g, b) in img.getdata()]

# Create the new image and save
gray_img = Image.new('RGB', img.size)
gray_img.putdata(new_list)
gray_img.save('RGB2.png')

# Task 2 -------------------
img2 = Image.open('RGB.png')

# Luminous Method
new_list = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000,) * 3 for a in img2.getdata()]

# Create the new image and save
ray_img = Image.new('RGB', img.size)
gray_img.putdata(new_list)
gray_img.save('RGB3.png')

# Task 3 --------------------
color_thief = ColorThief('RGB.png')
dominant_color = color_thief.get_color(quality=1)

#Find the component that has the highest value our of the three
max_value = max(dominant_color)
max_index = dominant_color.index(max_value)

#Assign dominant color name based on the highest component
if max_index == 0:
    dominant_color_name = "red"
elif max_index == 1:
    dominant_color_name = "green"
else:
    dominant_color_name = "blue"

#Open the image again to count occurrences of the dominant color
with open('RGB.png', 'rb') as f:
    image = f.read()

#Count occurrences of the dominant color level in the original image
count = sum(1 for pixel in image if pixel == max_value)

# Print the dominant color and occurences
print(f"Dominant Color: {dominant_color_name}")
print(f"Occurrences at the dominant color level: {count}")

# Task 4 -----------------------
# Using the example from the slides to get the difference
def patch_asscalar(a):
  return a.item()
setattr(numpy, "asscalar", patch_asscalar)

color1_rgb = sRGBColor(176, 63, 81, True)
color2_rgb = sRGBColor(185, 77, 89, True)

color1_lab = convert_color(color1_rgb, LabColor)
color2_lab = convert_color(color2_rgb, LabColor)
delta_e = delta_e_cie2000(color1_lab, color2_lab)
print(f'The difference is {delta_e}.')

# Task 5 -----------------------
# Using the example from the slides to compare the distance
def color_distance(c1, c2):
    r_diff = (c1[0] - c2[0]) ** 2
    g_diff = (c1[1] - c2[1]) ** 2
    b_diff = (c1[2] - c2[2]) ** 2
    return (r_diff + g_diff + b_diff) ** (1/2)

distance = color_distance((176, 63, 81), (185, 77, 89))
print(f"The distance between Apple 1 and Apple 2 is", distance)