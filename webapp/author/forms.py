from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.author.models import Author

class AuthorFeedbackForm(FlaskForm):
    author_id = HiddenField('ID автора', validators=[DataRequired()])
    feedback_text = StringField('Текст комментария', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

    def validate_author_id(self, author_id):
        if not Author.query.get(author_id.data):
            raise ValidationError('Вы пытаетесь прокомментировать новость с несуществующим id')