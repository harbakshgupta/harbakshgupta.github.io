from datetime import timedelta
from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from flask_session import Session
from tempfile import mkdtemp
from functools import wraps
from flask_mail import Mail, Message
from .models.models import db
import requests
import json

load_dotenv()
app = Flask(__name__, static_url_path="", static_folder="static")
app.secret_key = "@$$@%_S_O_M_E_S_E_C_R_E_T_K_E_Y_^%#@@@!"

# Forming Postgres URL from .env file
postgres_url = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/curezonepharma").split("://")
postgres_url[0] = postgres_url[0]+"ql"
postgres_url = "://".join(postgres_url)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_url

db.init_app(app)

with app.app_context():
    db.create_all()
    db.reflect()


app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_COOKIE_SECURE"] = True
app.permanent_session_lifetime = timedelta(days=30)

Session(app)

# Configuring Flask-Mail
app.config.update(
	DEBUG=True,

	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
    MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
	)
mail = Mail(app)

def send_mail(title,sender,recipients,message_html):
    msg = Message(title,
        sender=sender,
        recipients=recipients)
    msg.html = message_html
    mail.send(msg)
    return ("Mail Sent")


# Importing Blueprints
from app.views.main import main
from app.views.admin import admin

# Registering Blueprints

app.register_blueprint(main)
app.register_blueprint(admin)
