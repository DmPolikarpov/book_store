from flask import Blueprint, render_template, request
from webapp.book.models import Book


blueprint = Blueprint('book', __name__, url_prefix='/book')

@blueprint.route('/')
def book_index():
	title = "Книги"
	book_list = Book.query.order_by(Book.id.desc()).all()
	return render_template("book/index.html", page_title=title, book_list=book_list)


@blueprint.route('book_id', methods=['POST'])
def book_id():
	book_id = int(request.form['book_id'])
	book = Book.query.filter(Book.id == book_id).first()
	title = "О книге"
	return render_template("book/more.html", page_title=title, book=book)