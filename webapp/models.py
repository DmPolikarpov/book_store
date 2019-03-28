from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """ Модель пользователя. """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    birth_date = db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String, unique=True, nullable=True) 
    username = db.Column(db.String, unique=True, nullable=False)    
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String(10), nullable=True)
    books = db.relationship('Book', secondary='order')
    book_feedbacks = db.relationship('BookFeedback', backref='feedback_author', lazy=True)
    author_feedbacks = db.relationship('AuthorFeedback', backref='feedback_author', lazy=True)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.first_name} {self.last_name}'

class Order(db.Model):
    """ Модель заказа. """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    order_date = db.Column(db.DateTime, default=datetime.now)
    users = db.relationship('User', backref=db.backref('order', cascade='all, delete-orphan'))
    books = db.relationship('Book', backref=db.backref('order', cascade='all, delete-orphan'))   
    
    def __repr__(self):
        return f'Order {self.id} {self.order_date}'

class Book(db.Model):
    """ Модель книги. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    genre = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False) 
    price = db.Column(db.Numeric, nullable=False)    
    rating = db.Column(db.Integer, nullable=True)
    feedback = db.relationship('BookFeedback', backref='book', lazy=True)

    users = db.relationship('User', secondary='order')
    
    def __repr__(self):
        return f'Book {self.name}'

class Author(db.Model):
    """ Модель автора. """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False) 
    rating = db.Column(db.Integer, nullable=True)
    books = db.relationship('Book', backref='book_author', lazy=True)
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

