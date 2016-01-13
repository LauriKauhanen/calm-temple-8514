from calm_temple_8514 import app
from flask import render_template

@app.route('/index/')
@app.route('/index/<name>')
def index(name='World!'):
    return render_template('index.html', name=name)
