from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Order(db.Model):
    """ Модель заказа. """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    order_date = db.Column(db.DateTime, default=datetime.now)
    #users = db.relationship('User', backref=db.backref('order', cascade='all, delete-orphan'))
    #books = db.relationship('Book', backref=db.backref('order', cascade='all, delete-orphan'))   
    
    def __repr__(self):
        return f'Order {self.id} {self.order_date}'

class Author(db.Model):
    """ Модель автора. """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False) 
    rating = db.Column(db.Integer, nullable=True)
    #books = db.relationship('Book', backref='book_author', lazy=True)
    feedbacks = db.relationship('AuthorFeedback', backref='author', lazy=True)
    
    def __repr__(self):
        return f'Author {self.first_name} {self.last_name}'

class BookFeedback(db.Model):
    """ Модель отзыва на книгу. """
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=True)
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

