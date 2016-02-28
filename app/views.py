from app import app
from flask import url_for, redirect, render_template
from app.forms import UserForm

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/profile' , methods=['GET' , 'POST'])
def new():
    form = UserForm()
    return render_template('new.html', form=form)

@app.route('/profiles')
def index():
    return 'TO DO'

@app.route('/profile/<user_id>')
def show(user_id):
    return user_id

