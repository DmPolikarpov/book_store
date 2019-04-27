from flask import Blueprint, Flask, render_template, flash, redirect, request, url_for
from webapp.user.decorators import admin_required
from webapp.admin.forms import AddAuthor, AddBook

from webapp.db import db, Order
from webapp.author.models import Author
from webapp.book.models import Book
from webapp.user.models import User
from werkzeug.utils import secure_filename

import os, json

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required
def admin_index():
    title = 'Панель управления'
    author_form = AddAuthor()
    book_form = AddBook()
    full_order = []
    user_list = User.query.order_by(User.id.desc()).all()
    for user in user_list:
        user_info = {'first_name':user.first_name, 'last_name':user.last_name, 'birth_date':user.birth_date, 'email':user.email, 'username':user.username}
        order_list = Order.query.filter(Order.user_id == user.id).all()
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
            full_order.append({'user_info':user_info, 'date':date, 'detail':order_detail, 'deliver':deliver})
    return render_template('admin/index.html', page_title=title, author_form=author_form, book_form=book_form, full_order=full_order)

@blueprint.route('/add_author', methods=['POST'])
@admin_required
def add_author():
    form = AddAuthor()
    if not request.files["file"]:
        flash('Вы забыли добавить фотографию автора!')
        return redirect(url_for('admin.admin_index'))
    folder = os.path.abspath(os.path.dirname(__file__)) + '/../static/media/authors'
    file = request.files["file"]
    filename = secure_filename(file.filename)
    image = os.path.join('media/authors', filename)
    file.save(os.path.join(folder, filename))
    if form.validate_on_submit():
        new_author = Author(first_name=form.first_name.data, last_name=form.last_name.data, birth_date=form.birth_date.data, description=form.description.data, image=image)
        db.session.add(new_author)
        db.session.commit()
        flash('Вы успешно добавили нового автора!')
        return redirect(url_for('admin.admin_index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('admin.admin_index'))


@blueprint.route('/add_book', methods=['POST'])
@admin_required
def add_book():
    form = AddBook()
    if not request.files["file"]:
        flash('Вы забыли добавить изображение книги!')
        return redirect(url_for('admin.admin_index'))
    folder = os.path.abspath(os.path.dirname(__file__)) + '/../static/media'
    file = request.files["file"]
    filename = secure_filename(file.filename)
    image = os.path.join('media', filename)
    file.save(os.path.join(folder, filename))
    if form.validate_on_submit():
        new_book = Book(name=form.name.data, genre=form.genre.data, description=form.description.data, price=form.price.data, image=image)
        db.session.add(new_book)
        db.session.commit()
        flash('Вы успешно добавили новую книгу!')
        return redirect(url_for('admin.admin_index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('admin.admin_index'))




