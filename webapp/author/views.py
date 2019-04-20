from flask import Blueprint, render_template, request
from webapp.author.models import Author

blueprint = Blueprint('author', __name__, url_prefix='/author')

@blueprint.route('/')
def author_index():
	title = 'Авторы'
	author_list = Author.query.order_by(Author.id.desc()).all()
	return render_template('author/index.html', page_title=title, author_list=author_list)

@blueprint.route('author_id', methods=['POST'])
def author_id():
	author_id = int(request.form['author_id'])
	author = Author.query.filter(Author.id == author_id).first()
	title = "О авторе"
	return render_template("author/more.html", page_title=title, author=author)
