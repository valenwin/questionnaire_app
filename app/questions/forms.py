from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators


class QuestionForm(FlaskForm):
    class Meta:
        csrf = False

    text = StringField('Question',
                       validators=[validators.DataRequired()])


class AnswerForm(FlaskForm):
    class Meta:
        csrf = False

    text = StringField('Answer',
                       validators=[validators.DataRequired()])
