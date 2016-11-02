# coding=utf-8

from app import app
from models.user import User
from flask import session,render_template,request

#进入主页
@app.route("/", methods=['POST','GET'])
def index():
        return render_template('index.html')




# 用户登录模块
@app.route("/login/", method=['POST','GET'])
def login():
    if(request.method='POST'):
        pass
    else:
        pass

def doLogin():
    name=request

#用户注册页面
@app.route("/logup/", methods=['POST'])
def logup():
