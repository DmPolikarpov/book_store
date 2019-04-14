from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class":"form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите свое имя'})
    last_name = StringField('Фамилия', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите свою фамилию'})
    birth_date = StringField('Дата рождения', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Формат 01-01-2001'})
    email = StringField('Электронная почта', validators=[DataRequired(), Email()], render_kw={"class": "form-control", "placeholder": 'Впишите адрес e-mail'})
    username = StringField('Логин', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите свой логин'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите пароль'})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control", "placeholder": 'Повторите пароль'})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')