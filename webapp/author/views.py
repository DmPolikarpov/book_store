from flask import abort, Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required

from webapp.db import db
from webapp.author.models import Author, AuthorFeedback
from webapp.book.models import Book
from webapp.author.forms import AuthorFeedbackForm
from webapp.utils import get_redirect_target

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
    feedback_form = AuthorFeedbackForm(author_id=author.id)
    return render_template("author/more.html", page_title=title, author=author, feedback_form=feedback_form)


@blueprint.route('/author/feedback', methods=['POST'])
@login_required
def add_feedback():
    form = AuthorFeedbackForm()
    if form.validate_on_submit():
        if Author.query.filter(Author.id == form.author_id.data).first():
            feedback = AuthorFeedback(feedback=form.feedback_text.data, author_id=form.author_id.data, user_id=current_user.id)
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
    return redirect(get_redirect_target())