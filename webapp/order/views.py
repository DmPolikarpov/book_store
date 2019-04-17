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
    qty = 1
    price = int(request.form['price'])
    cost = price
    if not current_user.is_authenticated:
        flash('Для заказа книг необходимо залогиниться')
        return redirect(url_for('book.book_index'))        
    if not session.get('order'):
        session['order'] = []
    matching = [item for item in session['order'] if item['book_id'] == book_id]
    if matching:
        matching[0]['qty'] += 1
        matching[0]['cost'] = price*matching[0]['qty']
    else:
        session['order'].append(dict({'book_id':book_id, 'book_name':book_name, 'book_image':book_image, 'qty':qty, 'price':price, 'cost':cost}))    
        session.modified = True
    flash('книга успешно добавлена в корзину')
    return redirect(url_for('book.book_index')) 
   

@blueprint.route("/cart")
def cart():
    total = 0
    if not session.get('order'):
        flash('Корзина пуста')
        return redirect(url_for('book.book_index'))
    for item in session['order']:
        total += item['cost']
    nds = total - total/1.2 
    nds = round(nds, 2)
    order = session['order']
    return render_template('order/cart.html', order=order, nds=nds, total=total)

@blueprint.route("/del_position", methods=['POST'])
def del_position():
    book_id = int(request.form['book_id'])
    for item in session['order']:
        if item['book_id'] == book_id:
            session['order'].remove(item)
    session.modified = True
    return redirect(url_for('order.cart'))

@blueprint.route("/number_down", methods=['POST'])
def number_down():
    book_id = int(request.form['book_id'])
    matching = [item for item in session['order'] if item['book_id'] == book_id]
    if matching[0]['qty'] > 1:
        matching[0]['qty'] -= 1
        matching[0]['cost'] = matching[0]['price']*matching[0]['qty']
    else:
        flash('Данное количество - минимальное для заказа.')
    session.modified = True
    return redirect(url_for('order.cart'))

@blueprint.route("/number_up", methods=['POST'])
def number_up():
    book_id = int(request.form['book_id'])
    matching = [item for item in session['order'] if item['book_id'] == book_id]
    if matching[0]['qty'] < 5:
        matching[0]['qty'] += 1
        matching[0]['cost'] = matching[0]['price']*matching[0]['qty']
    else:
        flash('Данное количество - максимальное для заказа. Если Вам необходимо больше, свяжитесь с нами по телефону или электронной почте и получите специальные условия.')
    session.modified = True
    return redirect(url_for('order.cart'))



