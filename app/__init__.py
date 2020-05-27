from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import config

app = Flask(__name__)
Bootstrap(app)

app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Blueprints
from .user import user_page
from .questions import questions_page
app.register_blueprint(user_page, url_prefix='/user')
app.register_blueprint(questions_page, url_prefix='/questions')

from . import routes, models
from .user import routes, models
from .questions import routes, models