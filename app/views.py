from flask import render_template
from app import app



# Views
@app.route('/')
def index():
    return render_template('index.html')
