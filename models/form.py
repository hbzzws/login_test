# -*- coding: utf-8 -*-
# CreateTime : 2018/4/12 17:42 
# Author : hbzzws
# Description :

"""
表单类
"""

from wtforms import StringField, SubmitField, PasswordField, validators
from flask_wtf import FlaskForm


# 登录表单
class Login_Form(FlaskForm):
    pwdnotnone = validators.DataRequired(u'密码不能为空')
    accountlen = validators.Length(4, 18, u"账号长度在4-18位之间")
    pwdlen = validators.Length(6, 18, u"密码长度在6-18位之间")
    name = StringField('', validators=[accountlen], render_kw={"placeholder": "账号/手机号",})
    pwd = PasswordField('密码', validators=[pwdnotnone, pwdlen])
    submit = SubmitField('Login in')
