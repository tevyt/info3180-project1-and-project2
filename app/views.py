from app import app
from flask import url_for, redirect
# from flask import render_template

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/profile' , methods=['GET' , 'POST'])
def new():
    return 'TO DO'

@app.route('/profiles')
def index():
    return 'TO DO'

@app.route('/profile/<user_id>')
def show(user_id):
    return user_id

