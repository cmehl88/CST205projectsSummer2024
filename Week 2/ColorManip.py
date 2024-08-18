"""
Summary: For task one, I used a 100 x 100 pixel image and the first negative looked the opposite of
what the image looked like before, But when doing the negative again the image goes back to being
normal colored. I included a screenshot png of the negative and double negative image in the submissions.
I'm not sure if it's correct but it makes sense in my mind that a negative of a negative would be back to 
original. For task two I liked how the image turned out. I kept it at 50% and I think it hit the spot and 
also but in the side by side screenshot in the submissions. For task 3 I'm not sure if I did it right 
because lab said stuff about using split for conversion but I just created the image with the given tuples,
all I have to say is thank god for 5000% zoom for the photos app because 6 pixels is crazy. Overall completed
all the tasks.
"""

# Task 1
from PIL import Image
im = Image.open('labimage1.png')
negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
im.putdata(negative_list)
negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
im.putdata(negative_list)
im.save('negative_labimage2.png')

# Task 2
im = Image.open('sunset1.png')
sunset_list = [(p[0], p[1] // 2, p[2] // 2) for p in im.getdata()]
im.putdata(sunset_list)
im.save('sunset2.png')

# Task 3
# List out the tuples like from the labs last week
color_tuples = [
    (54, 54, 54),
    (232, 22, 93),
    (204, 82, 122),
    (54, 54, 54),
    (71, 71, 71),
    (168, 167, 167)
]

# Using x and y as width and height create a new image and save it
x = 2  # 2 pixels in each row
y = 3  # 3 rows of pixels
new_image = Image.new("RGB", (x, y))
new_image.putdata(color_tuples)
new_image.save("pixel.png")