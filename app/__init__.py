import os
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from tempfile import mkdtemp
from functools import wraps
from flask_mail import Mail, Message
from flask_session import Session
import requests
import json

app = Flask(__name__, static_url_path="", static_folder="static")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = mkdtemp()

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

# Registering Blueprints

app.register_blueprint(main)