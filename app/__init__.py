from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.config['SECRET_KEY'] = 'mnIcdwVxqc80HQ0nYOtS'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
from app import views
from app.models import User
