from flask import Blueprint, flash, render_template, redirect, url_for, request, session
from flask_login import current_user
from datetime import datetime

from webapp.db import db, Order
from webapp.book.models import Book
from webapp.user.forms import OrderForm
from webapp.user.models import User




blueprint = Blueprint('order', __name__, url_prefix='/order')

@blueprint.route("/add_to_order", methods=['POST'])
def add_to_order():
    if not current_user.is_authenticated:
        flash('Для заказа книг необходимо залогиниться')
        return redirect(url_for('book.book_index'))
    book_id = int(request.form['book_id'])
    book_name = str(request.form['book_name'])
    book_image = str(request.form['image'])
    qty = 1
    price = int(request.form['price'])
    cost = price       
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
    if not current_user.is_authenticated:
        flash('Для просмотра корзины необходимо залогиниться')
        return redirect(url_for('book.book_index'))
    title = 'Корзина'
    total = 0
    if not session.get('order'):
        flash('Корзина пуста')
        return redirect(url_for('book.book_index'))
    for item in session['order']:
        total += item['cost']
    nds = total - total/1.2 
    nds = round(nds, 2)
    order = session['order']
    return render_template('order/cart.html', page_title=title, order=order, nds=nds, total=total)

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

@blueprint.route("/form_order")
def form_order():
    title = "заказ"
    total = 0
    order_form = OrderForm()
    user = User.query.filter(User.id == current_user.id).all()
    order = session['order']
    for item in order:
        total += item['cost']
    return render_template('order/form_order.html', user=user, order=order, total=total, page_title=title, form=order_form)

@blueprint.route("/process_order", methods=['POST'])
def process_order():
    form = OrderForm()
    if form.validate_on_submit():
        order_detail = session['order']
        phone = form.phone.data
        region = form.region.data
        city = form.city.data
        street = form.street.data
        house = form.house.data
        deliver = dict({'phone':phone, 'region':region, 'city':city, 'street':street, 'house':house })
        new_order = Order(user_id=current_user.id, detail=order_detail, deliver=deliver)
        db.session.add(new_order)
        db.session.commit()
        session['order'].clear()
        flash('Заказ успешно оформлен! Ожидайте звонка оператора.')
        return redirect(url_for('book.book_index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('order.form_order'))

