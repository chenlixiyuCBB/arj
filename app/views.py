# coding=utf-8

from app import app
from models.user import User
from flask import session, render_template, request
from app import db


# 进入主页
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('base.html')


# 用户登录模块
@app.route("/login/", methods=['POST', 'GET'])
def login():
    return render_template('login.html')
    if request.method == 'POST':
        do_login()
    else:
        go_to_login()


def do_login():
    name = request.form['name']
    pass_word = request.form['passWd']

    if User.query.filter_by(Name=name, PssWd=pass_word):
        return render_template('login.html', name=name, passWd=pass_word)
    else:
        return render_template('login.html')


def go_to_login():
    return render_template('login.html')


# 用户注册模块
@app.route("/logup/", methods=['POST', 'GET'])
def log_up():
    if request.method == 'POST':
        do_log_up()
    else:
        go_to_log_up()


def do_log_up():
    user = User(request.form['name'], request.form['passWd'], request.form['phone'])
    if is_log_up_valid(user):
        db.session.add(user)
        db.session.commit()
        return render_template()
    else:
        return render_template()


def go_to_log_up():
    return True


def is_log_up_valid(user):
    return True

