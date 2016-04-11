#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from calm_temple_8514 import app
from .database import db_session
from .forms import *
from flask import render_template, request, make_response, redirect, url_for, \
    session, json
from flask.json import JSONEncoder
import os

#----------------------------------------------------------------------------#
# Controllers
#----------------------------------------------------------------------------#

# TODO: Actually implement fetching from database
def get_new_questions():
    """Function that returns 16 question fetched randomly from the database"""
    questions = []
    for i in range(16):
        question = Question()
        question.question = "Question " + str(i + 1)
        question.answers = ["a", "b", "c", "d"]
        question.right_answer = "a"
        questions.append(question)
    return questions

# Temporary class until adding orm model
class Question:

    def __init__(self):
        self.question = ""
        self.answers = None
        self.right_answer = ""


class QuestionJSONEncoder(JSONEncoder):
    """Encodes questions to json for storing in session"""
    def default(self, obj):
        if isinstance(obj, Question):
            return {
                'question': obj.question,
                'answers': obj.answers,
                'right_answer': obj.right_answer
            }
        return super(QuestionJSONEncoder, self).default(obj)


# Set custom encoder to use for saving questions to session
app.json_encoder = QuestionJSONEncoder


#----------------------------------------------------------------------------#
# Routers
#----------------------------------------------------------------------------#

#Index
@app.route('/')
def index():
    if session.get('logged', None) == True:
        return redirect(url_for('users', username = session['username']))
    else:
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('forms/register.html', form=form)

# User main page
@app.route('/users/<username>')
def users(username):
    if check_user_login(username):
        return make_response(render_template('pages/index.html', username=username))
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
            session['isAdmin'] = False
            return redirect(url_for('index'))
    return make_response(render_template('forms/login.html'))

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
    if request.method == 'GET':
        questions = get_new_questions()
        i = 1
        for q in questions:
            session['question' + str(i)] = q
            i += 1
        session['current_question'] = 1
        question = session['question' + str(session['current_question'])]
        # For some reason the questions are not yet saved as json dictionary.
        # The first question needs to be accessed as normal object.
        # Maybe the objects are not saved to session before end of call.
        # Is there a way to force saving to session?
        qstn = question.question
        answrs = question.answers
    if request.method == 'POST':
        session['current_question'] += 1
        question = session['question' + str(session['current_question'])]
        # Questions are now saved as dictionaries
        qstn = question['question']
        answrs = question['answers']

    return make_response(render_template(
        'pages/quiz.html',
        question=qstn,
        answers=answrs,
        username=session['username'])
    )


#404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

def check_user_login(username):
    if session.get('logged', None) == True and \
       session.get('username', None) == username:
        return True
    else:
        return False
