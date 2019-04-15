import psycopg2
import csv
from webapp.db import db
from webapp.author.models import Author
from webapp.book.models import Book
from webapp import create_app


app = create_app()
app.app_context().push()


with open('books.csv', 'r', encoding='utf-8-sig') as f:
    books = csv.DictReader(f, delimiter=';')
    for row in books:
        author_data = Author(first_name=row['first_name'], last_name=row['last_name'], birth_date=row['birth_date'], description=row['author_description'], image=row['author_image'])
        db.session.add(author_data)
        db.session.flush()      
        book_data = Book(name=row['name'], genre=row['category'], description=row['description'], price=row['price'], image=row['image'], author_id=author_data.id, pages=row['pages'], printed_in=row['printed_in'])
        db.session.add(book_data)
        

db.session.commit()
conn.close()
