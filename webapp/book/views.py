from flask import Blueprint, render_template, request, abort
from webapp.book.models import Book
from webapp.author.models import Author



blueprint = Blueprint('book', __name__, url_prefix='/book')

@blueprint.route('/')
def book_index():
	title = "Книги"
	book_list = Book.query.order_by(Book.id.desc()).all()
	return render_template("book/index.html", page_title=title, book_list=book_list)


@blueprint.route('<int:book_id>', methods=['GET'])
def book_info(book_id):
	book = Book.query.get_or_404(book_id)
	author = Author.query.get_or_404(book.author_id)
	title = "О книге"
	return render_template("book/more.html", page_title=title, book=book, author=author)







