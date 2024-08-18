"""
Carson Mehl
Cst205
7/7/2024
Lab - Flask 3
Summary: User types a name of a song and the genre and it's added to a playlist.
Github: https://github.com/cmehl88/cst205sp24flask
"""

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

class Playlist(FlaskForm):
    song_title = StringField(
        'Song Title', 
        validators=[DataRequired()]
    )
    genre_type = StringField(
        'Genre', 
        validators=[DataRequired()]
    )
    submit = SubmitField('Add Song')
    
# where the song names go
playlist = []

def store_song(my_song, my_genre):
    playlist.append(dict(
        song = my_song,
        genre = my_genre
    ))

# Need to add GET and POST 
@app.route('/', methods=('GET', 'POST'))
def index():
    form = Playlist()
    if form.validate_on_submit():
        store_song(form.song_title.data, form.genre_type.data)
        return redirect('/view_playlist')
    return render_template('index.html', form=form)

@app.route('/view_playlist')
def pl():
    return render_template('vp.html', playlist=playlist)