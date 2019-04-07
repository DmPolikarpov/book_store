from flask import Blueprint, render_template

blueprint = Blueprint('genre', __name__, url_prefix='/genre')

@blueprint.route('/')
def genre_index():
	title = 'Категории'
	return render_template('genre/index.html', page_title=title)
