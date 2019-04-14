from flask import Blueprint, flash, render_template, redirect, url_for, request, session
from flask_login import current_user

from webapp.db import db, Order
from webapp.book.models import Book



blueprint = Blueprint('order', __name__, url_prefix='/order')

@blueprint.route("/add_to_order", methods=['POST'])
def add_to_order():
    book_id = int(request.form['book_id'])
    book_name = str(request.form['book_name'])
    book_image = str(request.form['image'])
    price = int(request.form['price'])

    if not current_user.is_authenticated:
        flash('Для заказа книг необходимо залогиниться')
        return redirect(url_for('book.book_index'))        
    if not session.get('order'):
        session['order'] = []
    session['order'].append(dict({'book_id':book_id, 'book_name':book_name, 'book_image':book_image, 'price':price}))
    session.modified = True
    flash('книга успешно добавлена в корзину')
    return redirect(url_for('book.book_index')) 
   

@blueprint.route("/cart")
def cart():
    if not session.get('order'):
        flash('Корзина пуста')
        return redirect(url_for('book.book_index'))
    order = session['order']
    return render_template('order/cart.html', order=order)






