from flask import session

from .models import User


def get_current_user():
    user = None
    if 'user' in session:
        user = User.query.filter_by(email=session['user']).first()
    return user
