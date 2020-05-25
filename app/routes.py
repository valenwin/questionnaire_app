from flask import render_template

from app import app
from .user.utils import get_current_user


@app.route('/')
def index():
    user = get_current_user()
    return render_template('base.html', user=user)
