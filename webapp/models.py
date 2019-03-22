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
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	birth_date = db.Column(db.DateTime, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False) 
	username = db.Column(db.String, unique=True, nullable=False)    
	password = db.Column(db.String, nullable=False)
	orders = db.relationship('Order')
	order_book = db.relationship('OrderBook')

	def __repr__(self):
		return f'Customer {self.first_name} {self.last_name}'

class Order(db.Model):
	""" Модель заказа.

	Поля:
	1. дата заказа,
	2. id пользователя, 
	3. заказанная книга. 
	"""
	__tablename__ = 'order'
	id = db.Column(db.Integer, primary_key=True)
	order_date = db.Column(db.DateTime, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
	order_book = db.relationship('OrderBook')	
	
	def __repr__(self):
		return f'Order {self.id} {self.order_date}'

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
	__tablename__ = 'author'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	birth_date = db.Column(db.DateTime, nullable=False)
	description = db.Column(db.Text, nullable=False) 
	rating = db.Column(db.Integer, nullable=True)
	books = db.relationship('Book')
	feedback = db.relationship('AuthorFeedback')
	
	def __repr__(self):
		return f'Author {self.first_name} {self.last_name}'

class Genre(db.Model):
	""" Модель жанра.

	Поля:
	1. описание,
	2. книги.
	"""
	__tablename__ = 'genre'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text, nullable=False)
	books = db.relationship('Book')
	
	def __repr__(self):
		return f'Genre {self.description}'

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
	__tablename__ = 'book'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
	genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
	description = db.Column(db.Text, nullable=False) 
	price = db.Column(db.Integer, nullable=False)    
	rating = db.Column(db.Integer, nullable=True)
	feedback = db.relationship('BookFeedback')
	
	def __repr__(self):
		return f'Book {self.name}'

class OrderBook(db.Model):
	""" Модель заказа книги.

	Поля:
	1. id пользователя,
	2. id заказа.
	"""
	__tablename__ = 'orderBook'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

	def __repr__(self):
		return f'OrderBook {self.id} {self.order_id} {self.user_id}'		
    
class BookFeedback(db.Model):
	""" Модель отзыва на книгу.

	Поля:
	1. id автора книги,
	2. отзыв.
	"""
	__tablename__ = 'bookFeedback'
	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
	feedback = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'BookFeedback {self.feedback}'

class AuthorFeedback(db.Model):

	""" Модель отзыва на автора.

	Поля:
	1. id автора, 
	2. отзыв. 
	"""
	__tablename__ = 'authorFeedback'
	id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
	feedback = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'<AuthorFeedback {self.feedback}'
