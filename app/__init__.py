from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mnIcdwVxqc80HQ0nYOtS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/project1'
db = SQLAlchemy(app)
from app import views
from app.models import User
