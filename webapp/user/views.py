from flask import Blueprint, Flask, render_template, send_from_directory, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
import os, json

from webapp.db import db, Order
from webapp.user.models import User
from webapp.book.models import Book
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.utils import get_redirect_target
from werkzeug.utils import secure_filename

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
            return redirect(get_redirect_target())
    flash('Неправильное имя пользователя или пароль')
    return redirect(get_redirect_target())

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

@blueprint.route('/profile')
@login_required
def profile():
    title = "личный кабинет"
    full_order = []
    form = EditForm()
    pass_form = EditPasswordForm()
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.birth_date.data = current_user.birth_date
    user = User.query.filter(User.id == current_user.id).first()
    order_list = Order.query.filter(Order.user_id == current_user.id).all()
    for order in order_list:
        order_detail = []
        date = order.order_date
        detail = json.loads(order.detail)
        for item in detail:
            book_name = Book.query.filter(Book.id == item['book_id']).first()
            book_qty = item['qty']
            info = f'Книга {book_name} в количестве {book_qty} шт.'
            order_detail.append(info)
        deliver = json.loads(order.deliver)
        full_order.append({'date':date, 'detail':order_detail, 'deliver':deliver})
    return render_template('user/profile.html', page_title=title, form=form, pass_form=pass_form, user=user, full_order=full_order)

@blueprint.route('/process_edit_data', methods=['POST'])
@login_required
def process_edit_data():
    form = EditForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.birth_date = form.birth_date.data
        db.session.commit()
        flash('Изменения успешно сохранены!')
        return redirect(url_for('user.profile'))

@blueprint.route('/process_edit_password', methods=['POST'])
@login_required
def process_edit_password():
    form = EditPasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        db.session.commit()
        flash('Пароль успешно изменен!')
        return redirect(url_for('user.profile'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.profile'))


@blueprint.route('/uploads', methods=['POST'])
def uploads():
    folder = os.path.abspath(os.path.dirname(__file__)) + '/../static/icons'
    try:
        file = request.files["file"]
    except ValueError:
        abort(400)
    filename = secure_filename(file.filename)
    file.save(os.path.join(folder, filename))
    user = User.query.filter(User.id == current_user.id).first()
    user.image = filename
    db.session.commit()
    return redirect(url_for('user.profile', image=user.image))


    
