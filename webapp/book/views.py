from flask import Blueprint, render_template
from webapp.book.models import Book


blueprint = Blueprint('book', __name__, url_prefix='/book')

@blueprint.route('/')
def book_index():
	title = "Книги"
	book_list = Book.query.order_by(Book.id.desc()).all()
	return render_template("book/index.html", page_title=title, book_list=book_list)