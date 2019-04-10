import psycopg2
import csv
from webapp.db import db
from webapp.author.models import Author
from webapp.book.models import Book
from webapp import create_app


app = create_app()
app.app_context().push()

with open('books.csv', 'r', encoding='utf-8') as f:
	books = csv.DictReader(f, delimiter=';')
	for row in books:
		author_data = Author(first_name=row['first_name'], last_name=row['last_name'], birth_date=row['birth_date'], description=row['author_description'])
		db.session.add(author_data)
		db.session.flush()		
		print(author_data.id)
		book_data = Book(name=row['name'], genre=row['category'], description=row['description'], price=row['price'], image=row['image'], author_id=author_data.id)
		db.session.add(book_data)

db.session.commit()
conn.close()
