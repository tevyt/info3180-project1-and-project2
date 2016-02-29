import json
from app import app
from flask import url_for, redirect, render_template, request , flash, jsonify, Response
from app.forms import UserForm
from app import db
from app.models import User
import os
from random import getrandbits

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/profile' , methods=['GET' , 'POST'])
def new():
    form = UserForm()
    
    if request.headers['Content-Type'] == 'application/json':
        users = db.session.query(User).all()
        return user_list_json(users)
    if request.method == 'GET':
        return render_template('new.html', form=form)
    elif form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        sex = form.sex.data
        age = form.age.data
        image = form.image.data
        user = User(username ,firstname , lastname ,  age , sex ,'')
        filename = str(getrandbits(20)) + image.filename
        image.save(os.path.join("app/static", filename))
        user.file_location = filename
        db.session.add(user)
        db.session.commit()
        flash('New Profile created')
        return redirect(url_for('show' , user_id=user.user_id))
    else:
        return render_template('new.html' , form=form,errors=form.errors.items())

@app.route('/profiles')
def index():
    users = db.session.query(User).all()
    if request.headers['Content-Type'] == 'application/json':
        return user_list_json(users)
        
    if len(users) == 0:
        return 'No Registered Users'
    return render_template('index.html' , users=users)


@app.route('/profile/<user_id>' , methods=['GET' , 'POST'])
def show(user_id):
    user = db.session.query(User).filter_by(user_id=user_id).first()
    if user == None:
        if request.headers['Content-Type'] == 'application/json':
            return jsonify(message="Resource not found") , 404
        return render_template('404.html'), 404
    date = format_date(user.added_on)
    if request.headers['Content-Type'] == 'application/json' or request.method == 'POST':
        return jsonify(userid=user.user_id , username=user.username , image=user.file_location , age=user.age , profile_added_on=date)
    return render_template('show.html', user=user , date=date)

@app.errorhandler(404)
def page_not_found(e):
    if request.headers['Content-Type'] == 'application/json':
        return jsonify(message="Resource not found") , 404
    return render_template('404.html'), 404


def format_date(date):
    return date.strftime('%a %W %b %Y')

def user_list_json(users):
    user_json = []
    for user in users:
        user_json.append({'username': user.username , 'userid': user.user_id})
    return Response(json.dumps(user_json) , mimetype='application/json')

