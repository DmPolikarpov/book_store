from flask import Blueprint, render_template
from webapp.book.models import Book

blueprint = Blueprint('genre', __name__, url_prefix='/genre')

@blueprint.route('/')
def genre_index():
	genre_list = Book.query.order_by(Book.genre.desc()).all()

	title = 'Категории'
	return render_template('genre/index.html', page_title=title, genre_list=genre_list)

