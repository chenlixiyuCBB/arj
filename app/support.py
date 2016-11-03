# coding:utf-8
from flask import session, redirect, url_for


def require_logged_in(func):
    if getattr(session, "username", None) is not None:
        return func
    else:
        return redirect(url_for("login"))


def money_wrapper(money):
    try:
        money = float(money)
    except:
        return money
    return "￥ %4.2f" % money
