from flask import render_template
from app import app



# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)


@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''

    return render_template('movie.html')
