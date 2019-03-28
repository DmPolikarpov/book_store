import os


SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://karo:1karolina@localhost:5432/books'

SECRET_KEY = 'qwnjwdJBjBJ76B8hNNnzapq8'

#SQLALCHEMY_DATABASE_URI = 'postgresql://karo:1karolina@localhost/books'

""" basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db') """