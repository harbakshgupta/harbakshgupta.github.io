import random
import string
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from passlib.hash import sha256_crypt as sha
# from flask_mail import Mail, Message
from app import *

main = Blueprint('main', __name__)

@main.route('/', methods=['POST','GET'])
def index():
    if request.method== 'GET':
        return render_template('index.html')
    
@main.route('/about-us')
def about_us():
    return render_template('about-us.html')

@main.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

@main.route('/our-products')
def products():
    return render_template('product-page.html')