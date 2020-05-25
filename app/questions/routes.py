from flask import render_template, redirect, url_for
from flask import request

from . import questions_page
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from .. import db
from ..user.utils import get_current_user
from ..user.models import User


@questions_page.route('/', methods=['GET', 'POST'])
def questions():
    questions_lst = Question.query.join(User, User.id==Question.id).all()

    return render_template('questions/questions.html',
                           questions=questions_lst,
                           )


@questions_page.route('/<question_id>', methods=['GET', 'POST'])
def question(question_id):
    question_item = Question.query.filter_by(id=question_id).first()
    answers = Answer.query.filter_by(question_id=question_id).all()
    return render_template('questions/question.html',
                           question=question_item,
                           answers=answers)


@questions_page.route('/ask-question', methods=['GET', 'POST'])
def ask_question():
    form = QuestionForm(request.form)
    if request.method == 'POST' and form.validate():
        user = get_current_user()
        question = Question(
            text=form.text.data,
            user_id=user.id
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('questions_page.questions'))
    return render_template('questions/ask.html',
                           form=form)


@questions_page.route('/answer-question/<question_id>', methods=['GET', 'POST'])
def answer_question(question_id):
    form = AnswerForm(request.form)
    question_item = Question.query.filter_by(id=question_id).first()
    if request.method == 'POST' and form.validate():
        user = get_current_user()
        answer = Answer(
            text=form.text.data,
            user_id=user.id,
            question_id=question_item.id
        )
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('questions_page.question',
                                question_id=question_item.id))
    return render_template('questions/answer.html',
                           form=form,
                           question=question_item)
