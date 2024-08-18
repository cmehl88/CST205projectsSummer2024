"""
Carson Mehl
Cst205
7/12/2024
Homework #4
Summary: Using Flask, When the website opens up the user is presented with 
three randomly picks images from the list in image_info.py and then when
an image is clicked its information is displayed.
Github: https://github.com/cmehl88/cst205sp24flask/tree/main/cst205_hw4
"""

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
import random
from PIL import Image
import image_info

# Required Flask objects
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET'])
def index():
    # Get the images from image_info.py
    images = image_info.image_info[:]
    # Randomly select three images using shuffle
    random.shuffle(images)
    selected_images = images[:3]
    return render_template('index.html', images=selected_images)

@app.route('/image/<image_id>', methods=['GET'])
def image_detail(image_id):
    # Create the file path to the image
    image = next((img for img in image_info.image_info if img['id'] == image_id))
    image_path = f'static/images/{image_id}.jpg'
    # Using Pillow obtain the image's details
    with Image.open(image_path) as img:
        mode = img.mode
        img_format = img.format
        width, height = img.size
    # Return the image and the images detail as parameters to detail.html
    return render_template('detail.html', image=image, mode=mode, img_format=img_format, width=width, height=height)

