from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/andre')
def index():
    return 'falatu.com.br'
