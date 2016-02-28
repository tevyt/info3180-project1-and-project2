from app import app
from flask import url_for, redirect, render_template, request
from app.forms import UserForm

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/profile' , methods=['GET' , 'POST'])
def new():
    form = UserForm()
    if request.method == 'GET':
        return render_template('new.html', form=form)
    elif form.validate():
        firstname = form.firstname
        lastname = form.lastname
        sex = form.sex
        age = form.age
        image = form.image
        return 'Valid'
    else:
        return render_template('new.html' , form=form,errors=form.errors.items())

@app.route('/profiles')
def index():
    return 'TO DO'

@app.route('/profile/<user_id>')
def show(user_id):
    return user_id

