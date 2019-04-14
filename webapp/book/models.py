from webapp.db import db
from webapp.author.models import Author


class Book(db.Model):
    """ Модель книги. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    genre = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=True) 
    pages = db.Column(db.String, nullable=True)
    printed_in = db.Column(db.String, nullable=True)
    price = db.Column(db.Numeric, nullable=False)    
    rating = db.Column(db.Integer, nullable=True)
    feedbacks = db.relationship('BookFeedback', lazy=True)

    users = db.relationship('Order', backref='order')
    
    def __repr__(self):
        return f'Book {self.name}'