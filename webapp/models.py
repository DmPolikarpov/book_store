"""Модуль содержит модели базы данных магазина."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Модель пользователя.
    Поля:
    1. имя,
    2. фамилия, 
    3. год рождения, 
    4. адрес электронной почты, 
    5. логин, 
    6. пароль,
    7. заказы. 
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False) 
    username = db.Column(db.String, unique=True, nullable=False)    
    password = db.Column(db.String, nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f'User {self.first_name} {self.last_name}'

#вспомогательная таблица для создания отношения "многие ко многим" между моделями Заказы и Книги
books = db.Table('books',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True)
)

class Order(db.Model):
    """ Модель заказа.
    Поля:
    1. дата заказа,
    2. id пользователя, 
    3. заказанная книга. 
    """
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    books = db.relationship('Book', secondary=books, lazy='subquery', backref=db.backref('orders', lazy=True))   
    
    def __repr__(self):
        return f'Order {self.id} {self.order_date}'

class Book(db.Model):
    """ Модель книги.
    Поля:
    1. название,
    2. id автора, 
    3. id жанра, 
    4. описание,
    5. цена,
    6. рейтинг,
    7. отзыв. 
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    description = db.Column(db.Text, nullable=False) 
    price = db.Column(db.Integer, nullable=False)    
    rating = db.Column(db.Integer, nullable=True)
    feedback = db.relationship('BookFeedback', backref='book', lazy=True)
    
    def __repr__(self):
        return f'Book {self.name}'

class Author(db.Model):
    """ Модель автора.
    Поля:
    1. имя,
    2. фамилия, 
    3. дата рождения, 
    4. описание,
    5. рейтинг,
    6. книги,
    7. отзыв.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False) 
    rating = db.Column(db.Integer, nullable=True)
    books = db.relationship('Book', backref='author', lazy=True)
    feedback = db.relationship('AuthorFeedback', backref='author', lazy=True)
    
    def __repr__(self):
        return f'Author {self.first_name} {self.last_name}'

class Genre(db.Model):
    """ Модель жанра.
    Поля:
    1. описание,
    2. книги.
    """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    books = db.relationship('Book')
    
class BookFeedback(db.Model):
    """ Модель отзыва на книгу.
    Поля:
    1. id автора книги,
    2. отзыв.
    """
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=True)
    feedback = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'BookFeedback {self.feedback}'

class AuthorFeedback(db.Model):
    """ Модель отзыва на автора.
    Поля:
    1. id автора, 
    2. отзыв. 
    """
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    feedback = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<AuthorFeedback {self.feedback}'






