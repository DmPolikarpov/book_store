from webapp.db import db
from datetime import datetime
from sqlalchemy.orm import relationship

class Order(db.Model):
    """ Модель заказа. """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    order_date = db.Column(db.DateTime, default=datetime.now)
    detail = db.Column(db.JSON, nullable=False)
    deliver = db.Column(db.JSON, nullable=False)
    users = db.relationship('User', backref='order')
    books = db.relationship('Book', backref='order')   
    
    def __repr__(self):
        return f'Order {self.id} {self.order_date}'