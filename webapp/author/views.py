from flask import Blueprint, render_template, request, abort
from webapp.author.models import Author

blueprint = Blueprint('author', __name__, url_prefix='/author')

@blueprint.route('/')
def author_index():
	title = 'Авторы'
	author_list = Author.query.order_by(Author.id.desc()).all()
	return render_template('author/index.html', page_title=title, author_list=author_list)

@blueprint.route('<int:author_id>', methods=['GET'])
def author_info(author_id):
	author = Author.query.get_or_404(author_id)
	title = "О авторе"
	return render_template("author/more.html", page_title=title, author=author)
