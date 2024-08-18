"""
Carson Mehl
Cst205
7/14/2024
Lab - API Task 3 and 4
Summary: This Flask application displays a random cat image from CatAPI 
and when the button is clicked a new page appears with a random cat fact
from catAPI.ninja then may return to the main page using return home link.
"""

import json
import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

# The TheCatAPI API endpoint for a random image
cat_api_endpoint = 'https://api.thecatapi.com/v1/images/search'

# The catfact.ninja API endpoint for a random fact
cat_fact_endpoint = 'https://catfact.ninja/fact'

# For main page with the random image
@app.route('/', methods=['GET'])
def index():
    cat_image_url = fetch_random_cat_image()
    return render_template('index.html', cat_image_url=cat_image_url)

# For fun cat fact page
@app.route('/fun_fact', methods=['GET'])
def fun_fact():
    cat_fact = fetch_random_cat_fact()
    return render_template('cool_fun_fact.html', cat_fact=cat_fact)

# For the return home link
@app.route('/return_home', methods=['GET'])
def return_home():
    return redirect(url_for('index'))

# Try except for the image from CatAPI 
def fetch_random_cat_image():
    try:
        response = requests.get(cat_api_endpoint)
        response.raise_for_status()
        cat_image_url = response.json()[0]['url']
    except requests.exceptions.RequestException as e:
        cat_image_url = None
    return cat_image_url

# Try except for the fun fact from catfact.ninja
def fetch_random_cat_fact():
    try:
        response = requests.get(cat_fact_endpoint)
        response.raise_for_status()
        cat_fact = response.json()['fact']
    except requests.exceptions.RequestException as e:
        cat_fact = None
    return cat_fact