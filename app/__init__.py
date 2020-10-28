from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.jinja_env().add_extension('jinja2.ext.do')
app.jinja_env.filters['zip'] = zip
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/test.db'
app.config['SECRET_KEY'] = 'BLABLABLA'
db = SQLAlchemy(app)

from .views import *