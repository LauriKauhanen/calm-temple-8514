from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, Text, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime
import bcrypt


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(64))
    group_id = Column(Integer, ForeignKey('groups.id'))
    created = Column(DateTime)
    last_logged_on = Column(DateTime)

    group = relationship("Group")

    def __init__(self, username, password=None):
        self.username = username
        self.password = bcrypt.hashpw(password, bcrypt.gensalt(14))
        self.group_id = 1
        self.created = datetime.utcnow()
        self.last_logged_on = datetime.utcnow()


def is_authenticated(self):
    return True


def is_active(self):
    return True


def is_anonymous(self):
    return False


def get_id(self):
    return unicode(self.id)


def __repr__(self):
    return '<User %r>' % (self.username)


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, Sequence('group_id_seq'), primary_key=True)
    name = Column(String(32), unique=True)
    description = Column(Text)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Usergroup %r>' % (self.name)


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, Sequence('answer_id_seq'), primary_key=True)
    answer = Column(Text, unique=True)

    def __init__(self, answer=None):
        self.answer = answer

    def __repr__(self):
        return '<Answer %r>' % (self.name)


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, Sequence('question_id_seq'), primary_key=True)
    question = Column(String(120))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    correct_answer_id = Column(Integer, ForeignKey('answers.id'))
    times_correct = Column(Integer)
    attempts = Column(Integer)

    answer = relationship('Answer', foreign_keys=[answer_id])
    correct_answer = relationship('Answer', foreign_keys=[correct_answer_id])

    def __init__(self, question, answer, correct_answer=None):
        self.question = question
        self.answer = answer
        self.correct_answer = correct_answer
        self.times_correct = 0
        self.attempts = 0


def __repr__(self):
    return '<Question %r>' % (self.question)
