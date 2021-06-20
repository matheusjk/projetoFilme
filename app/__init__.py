from flask import Flask, render_template, request, flash, url_for, redirect, Blueprint, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy.sql import func
from flask_mail import Mail, Message
from datetime import datetime, timedelta
import os
import jwt

# from app. import filmes


api = Flask(__name__)

api.config.from_object("config")

db = SQLAlchemy(api)
login_manager = LoginManager()
login_manager.init_app(api)

mail = Mail(api)

from app.filmes.routes import filmes

api.register_blueprint(filmes)

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))


# @app.errorhandler(404)
# def naoEncontrado(error):
#     return render_template('error.html'), 404
