"""
Carson Mehl
Cst205
7/7/2024
Lab - Flask Part 1
Summary: This code is the first time using flask framework.
Github: 
"""

# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
  words = '<p>My Dad: YOLO </p><br><p>My Mom: OMG</p>'
  return words 

# the route for index.html
@app.route('/carson')
def hello2():
  return render_template('template.html')