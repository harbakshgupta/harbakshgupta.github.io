import random
import string
import re
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
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        contact_no = request.form["contact_no"]
        email = request.form["email"]
        message = request.form["message"]
        city = request.form["city"]

        if not contact_no.isnumeric() or len(contact_no)!=10:
            flash("Invalid Contact Number, please try again!","danger")
        elif len(message)==0:
            flash("Empty Message, please try again!","danger")
        else:
            print("Success")
            title= f"Message from Website by - {first_name} {last_name}"
            sender="sales.curezonepharma@gmail.com"
            recipients = ["info.curezonepharma@gmail.com"]
            message_html = f"Message from Website by <b>{first_name} {last_name}</b> <br> <b>Contact No:-</b> {contact_no} <br> <b>Email:-</b> {email} <br> <b>City:-</b> {city} <br> <b>Message:-</b> {message}"
            send_mail(title,sender,recipients,message_html) # Sending Mail
            flash("Query Sent Successfully","success")
        return redirect(url_for("main.contact_us"))

    return render_template('contact-us.html')

@main.route('/our-products')
def products():
    return render_template('product-page.html')

@main.route('/all-products')
def products_list():
    return render_template('product-list.html')