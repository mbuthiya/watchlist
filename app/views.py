from flask import render_template
from app import app



# Views
@app.route('/')
def index():
    message = 'Hello World'
    return render_template('index.html',message = message)
