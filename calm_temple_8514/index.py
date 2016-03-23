# coding=utf-8
from calm_temple_8514 import app
from flask import render_template, request, make_response, redirect, url_for, \
    session
from time import time

#Index
@app.route('/')
def index():
    if session.get('logged', None) == True:
        return redirect(url_for('users', username = session['username']))
    else:
        return redirect(url_for('login'))

# User main page
@app.route('/users/<username>')
def users(username):
    if check_user_login(username):
        return make_response(render_template('index.html', username=username))
    else:
        return redirect(url_for('login'))

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'demo' and \
           request.form['password'] == 'demo':
            session['username'] = request.form['username']
            session['logged'] = True
            return redirect(url_for('index'))
    return make_response(render_template('login.html'))

# Logout
@app.route('/logout')
def logout():
    session.pop('logged', None)
    return redirect(url_for('login'))

# Quiz
@app.route('/users/<username>/quiz', methods=['GET', 'POST'])
def quiz(username):
    if check_user_login(username) != True:
        return redirect(url_for('login'))
    if request.method == 'POST':
        pass
    question = u"""
        Tässä on kysymys jonka olisi tarkoitus vaihtua
        eri sivuilla. Kysymykset tulisi hakea tietokannasta.
        """
    answers = ['1', '2', '3', '4']
    return make_response(render_template(
        'quiz.html', question=question, answers=answers,
        username=session['username']))

#Redirect to the FluidUI mock
@app.route('/mock')
def mock():
    url = "https://www.fluidui.com/editor/live/preview/p_q6Nc6uq52Nsa8Ps9QuQ7p2fSSkV00bhm.1455102766253"
    return redirect(url, code=302)

#404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


def check_user_login(username):
    if session.get('logged', None) == True and \
       session.get('username', None) == username:
        return True
    else:
        return False

