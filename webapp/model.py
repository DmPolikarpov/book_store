from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	birth_date = db.Column(db.DateTime, nullable=False)
	email = db.Column(db.String, nullable=False) 
	username = db.Column(db.String, unique=True, nullable=False)    
	password = db.Column(db.String, nullable=False)
	orders = db.relationship('Order')
	order_book = db.relationship('OrderBook')

	def __repr__(self):
		return '<Customer {} {}>'.format(self.first_name, self.last_name)

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	order_date = db.Column(db.DateTime, nullable=False)
	customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id)) 
	order_book = db.relationship('OrderBook')	
	
	def __repr__(self):
		return '<Order {} {}>'.format(self.id, self.order_date)

class Author(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	birth_date = db.Column(db.DateTime, nullable=False)
	description = db.Column(db.Text, nullable=False) 
	rating = db.Column(db.Integer, nullable=True)
	books = db.relationship('Book')
	feedback = db.relationship('AuthorFeedback')
	
	def __repr__(self):
		return '<Author {} {}>'.format(self.first_name, self.last_name)

class Genre(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text, nullable=False)
	books = db.relationship('Book')
	
	def __repr__(self):
		return '<Genre {}>'.format(self.description)

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	author_id = db.Column(db.Integer, db.ForeignKey(Author.id))
	genre_id = db.Column(db.Integer, db.ForeignKey(Genre.id))
	description = db.Column(db.Text, nullable=False) 
	price = db.Column(db.Integer, nullable=False)    
	rating = db.Column(db.Integer, nullable=True)
	feedback = db.relationship('BookFeedback')
	
	def __repr__(self):
		return '<Book {}>'.format(self.name)

class OrderBook(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id))
	order_id = db.Column(db.Integer, db.ForeignKey(Order.id))

	def __repr__(self):
		return '<OrderBook {} {} {}>'.format(self.id, self.customer_id, self.order_id)		
    
class BookFeedback(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer, db.ForeignKey(Book.id))
	feedback = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return '<BookFeedback {}>'.format(self.feedback)

class AuthorFeedback(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(db.Integer, db.ForeignKey(Author.id))
	feedback = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return '<AuthorFeedback {}>'.format(self.feedback)
