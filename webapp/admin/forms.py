from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired


class AddAuthor(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите имя автора'})
    last_name = StringField('Фамилия', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите фамилию автора'})
    birth_date = StringField('Дата рождения', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Формат 01-01-2001'})
    description = StringField('Описание', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Добавьте описание'})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-outline-danger"})

class AddBook(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите название книги'})
    genre = SelectField('Категория', choices=[('пива','пиво'), ('вина','вино'), ('водка','водка'),('виски','виски'), ('коктейли','коктейли'), ('самогон','самогон')], validators=[DataRequired()], render_kw={"class": "form-control"})
    description = StringField('Описание', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Добавьте описание'})
    price = StringField('Цена', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Добавьте цену'})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-outline-danger"})



