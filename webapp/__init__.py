from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate

from webapp.db import db
from webapp.user.models import User
from webapp.admin.views import blueprint as admin_blueprint
from webapp.author.views import blueprint as author_blueprint
from webapp.book.views import blueprint as book_blueprint
from webapp.contact.views import blueprint as contact_blueprint
from webapp.genre.views import blueprint as genre_blueprint
from webapp.user.views import blueprint as user_blueprint

def create_app():
	app = Flask(__name__) 
	app.config.from_pyfile('config.py')
	db.init_app(app)
	migrate = Migrate(app, db)

	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'user.login'
	app.register_blueprint(admin_blueprint)
	app.register_blueprint(author_blueprint)
	app.register_blueprint(book_blueprint)
	app.register_blueprint(contact_blueprint)
	app.register_blueprint(genre_blueprint)
	app.register_blueprint(user_blueprint)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(user_id)

	@app.route('/')
	def index():
		title = "alcoBS"
		return render_template("index.html", page_title=title)
	 
	return app


