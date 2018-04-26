# -*- coding: utf-8 -*-
# CreateTime : 2018/4/12 17:41 
# Author : hbzzws
# Description :

from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from Start import login_manger
from Start import db


class Users(UserMixin, db.Model):
    __tablename__ = 'py_user'  # 对应mysql数据库表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    pwd = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, name, pwd):
        self.id = 1
        self.name = name
        self.pwd = pwd

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
