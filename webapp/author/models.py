from webapp.db import db
from datetime import datetime
from sqlalchemy.orm import relationship



class Author(db.Model):
    """ Модель автора. """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False) 
    rating = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String, nullable=True) 
    books = db.relationship('Book', backref='book_author', lazy=True)
    feedbacks = db.relationship('AuthorFeedback', backref='author', lazy=True)

    def feedbacks_count(self):
        return AuthorFeedback.query.filter(AuthorFeedback.author_id == self.id).count()

    def __repr__(self):
        return f'Author {self.first_name} {self.last_name}'


class AuthorFeedback(db.Model):
    """ Модель отзыва на автора. """
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    feedback = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
  
    def __repr__(self):
        return '<AuthorFeedback {}>'.format(self.id)

  