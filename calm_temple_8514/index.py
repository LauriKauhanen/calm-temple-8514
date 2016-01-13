from calm_temple_8514 import app
from flask import render_template

@app.route('/')
@app.route('/<name>')
def index(name='World!'):
    return render_template('hello.html', name=name)
