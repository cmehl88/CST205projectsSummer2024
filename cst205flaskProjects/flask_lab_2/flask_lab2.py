"""
Carson Mehl
Cst205
7/7/2024
Lab - Flask 2
Summary: Displays a dictionary and image using flask.
Github: https://github.com/cmehl88/cst205sp24flask
"""

# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

the_dictionary = {
  'brands' : ['Bubly', 'Waterloo', 'LaCroix', 'Perrier'],
  'flavors' : ['pineapple', 'lime', 'lemon', 'berry']
}

# the route for index.html
@app.route('/')
def hello2():
  return render_template('index.html', the_dictionary = the_dictionary)