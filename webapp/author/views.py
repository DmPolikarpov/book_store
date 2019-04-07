from flask import Blueprint, render_template

blueprint = Blueprint('author', __name__, url_prefix='/author')

@blueprint.route('/')
def author_index():
	title = 'Авторы'
	return render_template('author/index.html', page_title=title)
