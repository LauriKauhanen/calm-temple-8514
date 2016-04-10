from wtforms import Form, TextField, PasswordField, TextAreaField, StringField
from wtforms.validators import DataRequired, EqualTo, Length

class RegistrationForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )
	
class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
	
class QuestionForm(Form):
    """WTForms implementation for inputting new questions"""
    question = TextAreaField('question', validators=[DataRequired()])
    answer1 = StringField('answer1', validators=[DataRequired()])
    answer2 = StringField('answer2', validators=[DataRequired()])
    answer3 = StringField('answer3', validators=[DataRequired()])
    answer4 = StringField('answer4', validators=[DataRequired()])