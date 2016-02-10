from calm_temple_8514 import app
from flask import render_template, request, make_response,redirect, url_for
from time import time

#Index
@app.route('/')
def index(username=None):
    resp = make_response(render_template('index.html'))
    resp.set_cookie('visit', str(time()))
    return resp
    
#Redirect to the FluidUI mock
@app.route('/mock')
def mock():
    url = "https://www.fluidui.com/editor/live/preview/p_q6Nc6uq52Nsa8Ps9QuQ7p2fSSkV00bhm.1455102766253"
    return redirect(url, code=302)

@app.route('/username', methods=['POST'])
def username():
    return NotImplementedError

#404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
