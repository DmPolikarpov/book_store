from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.book.models import Book

class BookFeedbackForm(FlaskForm):
    book_id = HiddenField('ID  книги', validators=[DataRequired()])
    feedback_text = StringField('Текст комментария', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

    def validate_book_id(self, book_id):
        if not Book.query.get(book_id.data):
            raise ValidationError('Вы пытаетесь прокомментировать новость с несуществующим id')