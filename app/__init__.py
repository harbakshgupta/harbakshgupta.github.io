from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from tempfile import mkdtemp
from functools import wraps
from flask_mail import Mail, Message
from flask_session import Session
from .models.models import db
import requests
import json

load_dotenv()
app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = mkdtemp()

# Forming Postgres URL from .env file
postgres_url = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/curezonepharma").split("://")
postgres_url[0] = postgres_url[0]+"ql"
postgres_url = "://".join(postgres_url)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_url

Session(app)
db.init_app(app)

with app.app_context():
    db.create_all()

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