from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import config

app = Flask(__name__)
Bootstrap(app)

app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprints
from .user import user_page
app.register_blueprint(user_page, url_prefix='/user')

from . import routes, models
from .user import routes, models
