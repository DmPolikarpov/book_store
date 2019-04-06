from flask import Blueprint, render_template


blueprint = Blueprint('book', __name__)

@blueprint.route('/')
def index():
	title = "Bottlebook"
	return render_template("book/index.html", page_title=title)
