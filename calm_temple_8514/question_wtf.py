from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(Form):
    """WTForms implementation for inputing new questions"""
    question = TextAreaField('question', validators=[DataRequired()])
    answer1 = StringField('answer1', validators=[DataRequired()])
    answer2 = StringField('answer2', validators=[DataRequired()])
    answer3 = StringField('answer3', validators=[DataRequired()])
    answer4 = StringField('answer4', validators=[DataRequired()])

