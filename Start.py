# -*- coding: utf-8 -*-
# CreateTime : 2018/4/12 17:41
# Author : hbzzws
# Description :

from flask import Flask, render_template, flash, url_for, redirect, Blueprint
from flask_bootstrap import Bootstrap

from flask_moment import Moment
from flask_wtf import Form
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
import sys

# 解决flash的一个bug
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

app = Flask(__name__)

# 各项插件的配置
app.config['SECRET_KEY'] = 'kkk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'  # 配置数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
login_manger = LoginManager()
login_manger.session_protection = 'strong'
login_manger.login_view = 'blog.login'
login_manger.init_app(app)


@login_manger.user_loader
def load_user(user_id):
    from models.users import Users
    return Users("ws", "1")


"""
蓝图注册
"""


def init():
    from views import blog
    app.register_blueprint(blueprint=blog, url_prefix='')


if __name__ == '__main__':
    init()
    app.run(port=5600, debug=True)
