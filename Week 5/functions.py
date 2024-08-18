"""
Carson Mehl
Cst205
7/3/2024
HW3 Week 4
Summary: This code is for the functions of the five image transformations, search function, and options function.
Connected programs required to function: image_info.py, image_info.py
"""

from PIL import Image
from image_info import image_info

# The option chosen by user to decide transformation
def options(option, image_filepath):
    if option == 0:
        sepia(image_filepath)
    elif option == 1:
        negative(image_filepath)
    elif option == 2:
        grayscale(image_filepath)
    elif option == 3:
        thumbnail(image_filepath)
    elif option == 4:
        none_option(image_filepath)

# The five image transformation functions in order, I save the image at the end of each.
# Makes the image look old
def sepia(img_path):
    img = Image.open(img_path)
    width, height = img.size
    
    # go through each pixel and change the RGB to look more brownish (old)
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            red = int(0.393 * r + 0.769 * g + 0.189 * b)
            green = int(0.349 * r + 0.686 * g + 0.168 * b)
            blue = int(0.272 * r + 0.534 * g + 0.131 * b)

            img.putpixel((x, y), (min(red, 255), min(green, 255), min(blue, 255)))

    img.save('transformed_image.jpg') 

# Flips the colors in each pixel of the image
def negative(img_path):
    img = Image.open(img_path)
    negative_list = [(255 - p[0], 255 - p[1], 255 - p[2]) for p in img.getdata()]
    img.putdata(negative_list)
    img.save('transformed_image.jpg')  

# Turns the image a color between white and black by getting the average
def grayscale(img_path):
    img = Image.open(img_path)
    grayscale_list = [(int(sum(p) / 3),) * 3 for p in img.getdata()]
    img.putdata(grayscale_list)
    img.save('transformed_image.jpg')  
    
# Downsizes image in half
def thumbnail(img_path):
    img = Image.open(img_path)
    width, height = img.size
    
    # Get size for the image
    x = width // 2
    y = height // 2
    
    # Resize the image with the new x and y
    thumbnail_image = img.resize((x, y))
    thumbnail_image.save('transformed_image.jpg')

# Does not change the image 
def none_option(image_filepath):
    img = Image.open(image_filepath)
    img.save('transformed_image.jpg')
    
# The search function
def my_search(keyword):
    # initilize variables
    best_match = None
    max_matches = 0
    
    # Iterate through each images title and tags
    for img in image_info:
        title_matches = img['title'].lower().count(keyword.lower())
        tags_matches = sum([tag.lower().count(keyword.lower()) for tag in img['tags']])
        # add up total matches of tags and titles
        total_matches = title_matches + tags_matches
        
        # See if the new image has more or less tags then last
        if total_matches > max_matches:
            max_matches = total_matches
            # get result
            best_match = img['id']
    
    return best_match