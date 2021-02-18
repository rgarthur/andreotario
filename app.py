from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    return 'que azar man'

@app.route('/about')
def about():
    return render_template('about.html')