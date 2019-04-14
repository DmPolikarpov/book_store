from flask import Blueprint, render_template
from webapp.author.models import Author

blueprint = Blueprint('author', __name__, url_prefix='/author')

@blueprint.route('/')
def author_index():
	title = 'Авторы'
	author_list = Author.query.order_by(Author.id.desc()).all()
	return render_template('author/index.html', page_title=title, author_list=author_list)
