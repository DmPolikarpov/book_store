from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_migrate import Migrate

from webapp.models import db, User
from webapp.forms import LoginForm

def create_app():
	app = Flask(__name__) 
	app.config.from_pyfile('config.py')
	db.init_app(app)
	migrate = Migrate(app, db)

	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'login'

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(user_id)
	  
	@app.route('/')
	def index():
		title = "Bottlebook"
		return render_template("index.html", page_title=title)

	@app.route('/login')
	def login():
		title = "Авторизация"
		login_form = LoginForm()
		return render_template('login.html', page_title=title, form=login_form)	

	@app.route('/process-login', methods=['POST'])
	def process_login():
		form = LoginForm()
		if form.validate_on_submit():
			user = User.query.filter_by(username=form.username.data).first()
			if user and user.check_password(form.password.data):
				login_user(user)
				flash('Вы вошли на сайт')
				return redirect(url_for('index'))
		flash('Неправильное имя пользователя или пароль')
		return redirect(url_for('login'))

	@app.route('/logout')
	def logout():
		logout_user()
		return redirect(url_for('index')) 

	@app.route('/admin')
	@login_required
	def admin_index():
		if current_user.is_admin:
			return 'привет админ'
		else:
			return 'ты не админ'
	
	return app


