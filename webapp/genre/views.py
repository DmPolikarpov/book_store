from flask import Blueprint, render_template, request

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

	
"""@blueprint.route(' int<genre.id>', methods=['GET'])
def genre_info(genre_id):
	genre = Book.query.get_or_404(genre_id)
	author = Author.query.get_or_404(genre.author_id)
	title = "Книги категории"
	return render_template("genre/more.html", page_title=title, genre=genre, author=author)
"""
	