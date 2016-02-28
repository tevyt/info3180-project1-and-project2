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
        firstname = form.firstname.data
        lastname = form.lastname.data
        sex = form.sex.data
        age = form.age.data
        image = form.image.data
        return image.filename
    else:
        return render_template('new.html' , form=form,errors=form.errors.items())

@app.route('/profiles')
def index():
    return 'TO DO'

@app.route('/profile/<user_id>')
def show(user_id):
    return user_id

