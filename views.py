# -*- coding: utf-8 -*-
# CreateTime : 2018/4/12 17:43 
# Author : hbzzws
# Description :

"""
视图模型
"""

from  flask import render_template,Blueprint,redirect,url_for,flash
from Start import login_manger
from models.form import Login_Form
from models.users import  Users
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
# from DB import db

blog=Blueprint('blog',__name__)  #蓝图

@blog.route('/')
def index():
    form=Login_Form()
    return render_template('login.html',form=form)

@blog.route('/index')
@login_required
def l_index():
    return render_template('ok.html')

@blog.route('/login',methods=['GET','POST'])
def login():
        form=Login_Form()
        if form.validate_on_submit():
            # user=Users.query.filter_by(name=form.name.data).first()
            user= Users("test","666666")
            if user is not  None and user.pwd==form.pwd.data:
                login_user(user)
                flash('登录成功')
                return  render_template('ok.html',name=form.name.data)
            else:
                flash('用户或密码错误')
                return render_template('login.html',form=form)
        else:
            return render_template('login.html',form=form)



#用户登出
@blog.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已退出登录')
    return redirect(url_for('blog.index'))

