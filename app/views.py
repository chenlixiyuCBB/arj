# coding=utf-8
from sqlalchemy.exc import DataError

from app import app
from app.models.product import Product
from models.user import User
from flask import session, render_template, request
from app import db


# 进入主页
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('base.html')


# 用户登录模块
@app.route("/login/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        do_login()
    else:
        go_to_login()


def do_login():
    name = request.form['name']
    pass_word = request.form['passWd']

    if User.query.filter_by(Name=name, PssWd=pass_word).all() is not None:
        session['userName'] = name
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
    cur_user = User(request.form['name'], request.form['passWd'], request.form['phone'])
    cur_error = {}
    if is_log_up_valid(cur_user, cur_error):
        try:
            db.session.add(cur_user)
            db.session.commit()
        except:
            raise DataError
        return render_template('user.html', user=cur_user)

    else:
        return render_template('logup.html', user=cur_user, error=cur_error)


def go_to_log_up():
    return render_template('logup.html')


def is_log_up_valid(cur_user, cur_error):
    flag = 0

    return True


# 搜索商品
@app.route('/search/', methods=['POST', 'GET'])
def search():
    if request.form['search_key'] is not None:
        search_key = request.form['search_key']
        rows = Product.query.filter(Product.Name.like('%' + search_key + '%'))
        return render_template('', results=rows)
    else:
        return render_template('', result=None)

# 商品分类搜索
@app.route('/search_kind/', methods=['POST', 'GET'])
def search_kind():
    if request.form['search_key'] is not None:
        search_key = request.form['search_key']
