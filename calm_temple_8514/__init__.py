# coding=utf-8
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Set secret key for sessions
app.secret_key = os.environ.get('SECRET_KEY')

import calm_temple_8514.index
