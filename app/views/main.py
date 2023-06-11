import random
import string
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint
from passlib.hash import sha256_crypt as sha
# from flask_mail import Mail, Message
from app import *

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
    
@main.route('/about-us')
def about_us():
    return render_template('about-us.html')

@main.route('/contact-us', methods=['POST','GET'])
def contact_us():
    if request.method=="POST":
        pass
    return render_template('contact-us.html')

@main.route('/our-products')
def products():
    return render_template('product-page.html')

@main.route('/all-products')
def products_list():
    return render_template('product-list.html')