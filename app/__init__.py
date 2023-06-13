import os
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from tempfile import mkdtemp
from functools import wraps
from flask_mail import Mail, Message
# from flask_recaptcha import ReCaptcha
import requests
import json

app = Flask(__name__, static_url_path="", static_folder="static")

# Configuring Flask-Mail
# app.config.update(
# 	DEBUG=True,

# 	#EMAIL SETTINGS
# 	MAIL_SERVER='smtp.gmail.com',
# 	MAIL_PORT=465,
# 	MAIL_USE_SSL=True,
#     # MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
#     # MAIL_PASSWORD = os.getenv("MAIL_PASSWORD"),
# 	)
# mail = Mail(app)

# def send_mail(title,sender,recipients,message_html):
#     msg = Message(title,
#         sender=sender,
#         recipients=recipients)
#     msg.html = message_html
#     mail.send(msg)
#     return ("Mail Sent")

## reCaptcha
# recaptcha = ReCaptcha(app=app)
# SITE_KEY= "6Lc7b4gUAAAAAPvGrs6ExI4KCN11VaK5-AygiNDV"
# SECRET_KEY = "6Lc7b4gUAAAAAFzUsJumv07rK7eeRFtXCEfIxhyT"
# def is_human(captcha_response):
#     # Validating recaptcha response from google server
#     # Returns True captcha test passed for submitted form else returns False.
#     payload = {'response':captcha_response, 'secret':SECRET_KEY}
#     response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
#     response_text = json.loads(response.text)
#     return response_text['success']

# Importing Blueprints
from app.views.main import main

# Registering Blueprints

app.register_blueprint(main)