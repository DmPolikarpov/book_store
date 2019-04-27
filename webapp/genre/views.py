from flask import Blueprint, render_template, request, abort

from webapp.book.models import Book
from webapp.author.models import Author

blueprint = Blueprint('genre', __name__, url_prefix='/genre')

@blueprint.route('/')
def genre_index():
	genre_list = Book.query.order_by(Book.genre.desc()).all()
	#genre_list = Book.query.with_entities(Book.genre)
	print('========================')
	print(genre_list)
	print('========================')
	my_list = []
	for genre in genre_list:
		my_list.append(genre.genre) 
	genres = list(set(my_list))
	title = 'Категории'
	return render_template('genre/index.html', page_title=title, genre_list=genre_list, genres=genres)

	
@blueprint.route('/<genre>/', methods=['GET'])
def genre_info(genre):
	genre = genre.lower()
	books = Book.query.filter_by(genre=genre).all()
	if not books:
		abort(404)
	
	title = "Книги категории"
	return render_template("genre/more.html", page_title=title, books=books, genre=genre)

	