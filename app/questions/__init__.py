from flask import Blueprint

questions_page = Blueprint('questions_page', __name__)

from app.questions import routes