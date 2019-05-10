from flask import abort, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required

from webapp.db import db
from webapp.book.models import Book, BookFeedback
from webapp.author.models import Author
from webapp.book.forms import BookFeedbackForm




blueprint = Blueprint('book', __name__, url_prefix='/book')

@blueprint.route('/')
def book_index():
	title = "Книги"
	book_list = Book.query.order_by(Book.id.desc()).all()
	return render_template("book/index.html", page_title=title, book_list=book_list)


@blueprint.route('<int:book_id>', methods=['GET'])
def book_info(book_id):
	book = Book.query.get_or_404(book_id)
	try:
		author = Author.query.get(book.author_id)
	except TypeError:
		abort(404)
	title = "О книге"
	feedback_form = BookFeedbackForm(book_id=book.id)
	return render_template("book/more.html", page_title=title, book=book, author=author, feedback_form=feedback_form)

@blueprint.route('/book/feedback', methods=['POST'])
@login_required
def add_feedback():
	form = BookFeedbackForm()
	if form.validate_on_submit():
		feedback = BookFeedback(feedback=form.feedback_text.data, book_id=form.book_id.data, user_id=current_user.id)
		db.session.add(feedback)
		db.session.commit()
		flash('Комментарий успешно добавлен')
	else:
		for field, errors in form.errors.items():
			for error in errors:
				flash('Ошибка в заполнении поля "{}": - {}'.format(
					getattr(form, field).label.text,
					error
				))
	return redirect(request.referrer)






