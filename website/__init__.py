from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# iniciando o banco de dados
db = SQLAlchemy()

DB_NAME = "database.db" # para o sqlite
def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'borealis-pg-flat-99864 dpxzru6mxicrea6y2uzchvtiuom'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app)

    return app
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')