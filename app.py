from flask import Flask, render_template, redirect, url_for, request
from database.sqlite import SQLite

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        username = request.form['username']
        password = request.form['password']
        sqlite = SQLite()
        query = 'SELECT username, password, name FROM users WHERE username=? AND password=?'
        result = sqlite.select(query, [username, password])
        if result:
            return 'user' + result[0]['name'] + ' Conectado com sucesso'
    return 'foi nao lek'