from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ Модель пользователя. """
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

# вспомогательная таблица для создания отношения "многие ко многим" между моделями Заказы и Книги
books = db.Table('books',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True)
)

class Order(db.Model):
    """ Модель заказа. """
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    books = db.relationship('Book', secondary=books, lazy='subquery', backref=db.backref('orders', lazy=True))   
    
    def __repr__(self):
        return f'Order {self.id} {self.order_date}'

class Book(db.Model):
    """ Модель книги. """
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
    """ Модель автора. """
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
    """ Модель жанра. """
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    books = db.relationship('Book')
    
    def __repr__(self):
        return f'Genre {self.description}'

class BookFeedback(db.Model):
    """ Модель отзыва на книгу. """
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=True)
    feedback = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'BookFeedback {self.feedback}'

class AuthorFeedback(db.Model):
    """ Модель отзыва на автора. """
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    feedback = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<AuthorFeedback {self.feedback}'






