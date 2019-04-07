from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Order(db.Model):
    """ Модель заказа. """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    order_date = db.Column(db.DateTime, default=datetime.now)
    users = db.relationship('User', backref='order')
    books = db.relationship('Book', backref='order')   
    
    def __repr__(self):
        return f'Order {self.id} {self.order_date}'

class BookFeedback(db.Model):
    """ Модель отзыва на книгу. """
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'BookFeedback {self.feedback}'

class AuthorFeedback(db.Model):
    """ Модель отзыва на автора. """
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    feedback = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'AuthorFeedback {self.feedback}'

