from flask import Blueprint, render_template


blueprint = Blueprint('book', __name__)

@blueprint.route('/')
def index():
	title = "Bottlebook"
	return render_template("main_page/index.html", page_title=title)