from datetime import datetime
from functools import partial

import bcrypt
from slugify import slugify
from sqlalchemy import Column

from app import db

NotNullColumn = partial(Column, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = NotNullColumn(db.String(250))
    email = NotNullColumn(db.String, unique=True)
    password = NotNullColumn(db.String)
    created = db.Column(db.DateTime, default=datetime.now)
    slug = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def __init__(self, *args, **kwargs):
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super().__init__(*args, **kwargs)

    @staticmethod
    def make_password_hash(password):
        hash = bcrypt.hashpw(password=password.encode('utf-8'),
                             salt=bcrypt.gensalt())
        return hash.decode('utf-8')

    def is_password_valid(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),
                              self.password.encode('utf-8'))
