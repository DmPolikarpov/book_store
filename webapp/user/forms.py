from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class":"form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-outline-danger"})


class RegistrationForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите свое имя'})
    last_name = StringField('Фамилия', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите свою фамилию'})
    birth_date = StringField('Дата рождения', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Формат 01-01-2001'})
    email = StringField('Электронная почта', validators=[DataRequired(), Email()], render_kw={"class": "form-control", "placeholder": 'Впишите адрес e-mail'})
    username = StringField('Логин', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите свой логин'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите пароль'})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control", "placeholder": 'Повторите пароль'})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-outline-danger"})

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')

class OrderForm(FlaskForm):
    phone = StringField('Номер телефона', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите номер телефона для связи'})
    region = StringField('Регион', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите свой регион'})
    city = StringField('Город', validators=[DataRequired()], render_kw={"class":"form-control", "placeholder": 'Впишите свой город'})
    street = StringField('Улица', validators=[DataRequired()], render_kw={"class":"form-control", "placeholder": 'Впишите свою улицу'})    
    house = StringField('Дом', validators=[DataRequired()], render_kw={"class":"form-control", "placeholder": 'Впишите номер дома'})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-outline-danger"})

class EditForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()], render_kw={"class": "form-control"})
    last_name = StringField('Фамилия', validators=[DataRequired()], render_kw={"class": "form-control"})
    birth_date = StringField('Дата рождения', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-outline-danger"})

class EditPasswordForm(FlaskForm):
    old_password = PasswordField('Старый пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите старый пароль'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": 'Впишите новый пароль'})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control", "placeholder": 'Повторите новый пароль'})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-outline-danger"})

    def validate_old_password(self, old_password):
        user = User.query.filter(User.id == current_user.id).first()
        if not user.check_password(old_password.data):
            raise ValidationError('Неправильный пароль')







