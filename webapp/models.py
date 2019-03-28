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
    book_feedbacks = db.relationship('BookFeedback', backref='user', lazy=True)
    author_feedbacks = db.relationship('AuthorFeedback', backref='user', lazy=True)

    def __repr__(self):
        return f'User {self.first_name} {self.last_name}'


class Book(db.Model):
    """ Модель книги. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    genre = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False) 
    price = db.Column(db.Numeric, nullable=False)    
    rating = db.Column(db.Integer, nullable=True)
    feedback = db.relationship('BookFeedback', backref='book', lazy=True)

    
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
    books = db.relationship('Book', backref='author', lazy=True)
    feedback = db.relationship('AuthorFeedback', backref='author', lazy=True)
    
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
        return f'<AuthorFeedback {self.feedback}'






