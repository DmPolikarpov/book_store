from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	""" Этот класс описывет покупателя книг, создавая в базе параметры:
	имя, фамилия, год рождения, адрес электронной почты, логин, пароль,
	заказы 
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
	""" Этот класс создает запись о заказе покупателя с полями: 
	дата заказа, id покупателя, заказанная книга.
	"""
	__tablename__ = 'order'
	id = db.Column(db.Integer, primary_key=True)
	order_date = db.Column(db.DateTime, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
	order_book = db.relationship('OrderBook')	
	
	def __repr__(self):
		return f'Order {self.id} {self.order_date}'

class Author(db.Model):
	""" Этот класс создет запись о авторе книги со следующими полями:
	имя, фамилия, дата рождения, описание автора, рейтинг, его книги, отзывы.
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
	""" Этот класс создает запись о жанре книги с такими полями как:
	описание, книги.
	"""
	__tablename__ = 'genre'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text, nullable=False)
	books = db.relationship('Book')
	
	def __repr__(self):
		return f'Genre {self.description}'

class Book(db.Model):
	""" Этот класс создает запись о книге с полями:
	название, автор, жанр, описание, цена, рейтинг, отзывы.
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
	""" Этот класс создает запись о заказе с полями:
	клиент, сделавший заказ и номер заказа.
	"""
	__tablename__ = 'orderBook'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

	def __repr__(self):
		return f'OrderBook {self.id} {self.order_id} {self.user_id}'		
    
class BookFeedback(db.Model):
	""" Этот класс создает запись о отзыве на книгу с полями:
	номер книги, отзыв.
	"""
	__tablename__ = 'bookFeedback'
	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
	feedback = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'BookFeedback {self.feedback}'

class AuthorFeedback(db.Model):
	""" Этот класс создает запись о отзыве на автора с полями:
	номер автора, отзыв.
	"""
	__tablename__ = 'authorFeedback'
	id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
	feedback = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return f'<AuthorFeedback {self.feedback}'
