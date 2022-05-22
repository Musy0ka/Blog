from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager

def create_app():
  app = Flask (__name__)
  app.config['SECRET_KEY'] = 'secretkey'

  @app.route("/")
  def home():
    return "<h1>Hello</h1>"

  @app.route("/profile")
  def profile():
    return "<h1>Profile</h1>"

  return app