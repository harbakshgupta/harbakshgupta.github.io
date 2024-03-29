import random
import string
import re
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint, send_from_directory
from passlib.hash import sha256_crypt as sha
from ..models.models import blogPosts
from app import *

main = Blueprint('main', __name__)

@main.route('/')
def index():
    admin = session.get("admin",False)
    return render_template('index.html', admin=admin)
    
@main.route('/about-us')
def about_us():
    admin = session.get("admin",False)
    return render_template('about_us.html', admin=admin)

@main.route('/contact-us', methods=['POST','GET'])
def contact_us():
    admin = session.get("admin",False)
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

    return render_template('contact_us.html', admin=admin)

@main.route('/our-products')
def products():
    admin = session.get("admin",False)
    return render_template('product_page.html', admin=admin)

@main.route('/all-products')
def products_list():
    admin = session.get("admin",False)
    return render_template('product_list.html', admin=admin)

@app.route('/sitemap.xml')
def sitemap_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/robots.txt')
def robots_txt_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@main.route('/blog')
def blog():
    admin = session.get("admin",False)
    posts = db.session.query(blogPosts).filter_by(visible=True).order_by(blogPosts.date).all()
    print(posts)
    return render_template('blog.html', **locals())

@main.route('/blog-post/<slug>')
def blog_post(slug):
    admin = session.get("admin",False)
    post = db.session.execute(db.select(blogPosts).filter_by(slug=slug)).scalar()
    if post is None:
        flash("Blog Post Not Found","warning")
        return redirect(url_for("main.blog"))
    return render_template('blog_post.html', **locals())

# @main.route('/populate-admin')
# def populate_admin():
#     admin = Admin("username", sha.hash("password"))
#     db.session.add(admin)
#     db.session.commit()
#     return "Admin Populated"