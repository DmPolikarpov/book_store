from webapp.db import db
from webapp.book.models import Book
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    """ Модель пользователя. """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    birth_date = db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String, unique=True, nullable=True) 
    username = db.Column(db.String, unique=True, nullable=False)    
    password = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)
    role = db.Column(db.String(10), index=True, nullable=True)
    books = db.relationship('Order', backref='order_book')
    book_feedbacks = db.relationship('BookFeedback', backref='feedback_author', lazy=True)
    author_feedbacks = db.relationship('AuthorFeedback', backref='feedback_author', lazy=True)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'
    

    def __repr__(self):
        return f'User {self.first_name} {self.last_name}'