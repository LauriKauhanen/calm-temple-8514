from calm_temple_8514 import app
from flask import render_template

@app.route('/')
def index(name='World!'):
    return render_template('hello.html', name=name)
