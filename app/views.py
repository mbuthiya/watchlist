from app import app


# Views
@app.route('/')
def index():
    return '<h1> Hello World </h1>'
