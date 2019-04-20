from flask import Blueprint, Flask, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from webapp.db import db
from webapp.user.models import User
from webapp.user.forms import LoginForm, RegistrationForm

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)    

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('book.book_index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('book.book_index')) 

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('book.book_index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('user/registration.html', page_title=title, form=form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, birth_date=form.birth_date.data, email=form.email.data, username=form.username.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.register'))

@blueprint.route('/profil')
def profil():
    title = "личный кабинет"
    return render_template('user/profil.html', page_title=title)




    