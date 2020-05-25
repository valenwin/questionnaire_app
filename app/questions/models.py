from datetime import datetime
from functools import partial

from sqlalchemy import Column

from app import db

NotNullColumn = partial(Column, nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = NotNullColumn(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Question {}>'.format(self.text)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = NotNullColumn(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Answer {} on question {}>'.format(self.text, self.question_id)
