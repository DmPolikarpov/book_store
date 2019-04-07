from flask import Blueprint, render_template

blueprint = Blueprint('contact', __name__, url_prefix='/contact')

@blueprint.route('/')
def contact_index():
	title = 'О нас'
	return render_template('contact/index.html', page_title=title)
