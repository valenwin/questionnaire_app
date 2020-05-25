from functools import partial

from sqlalchemy import Column

from app import db

NotNullColumn = partial(Column, nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = NotNullColumn(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = NotNullColumn(db.String(1000))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
