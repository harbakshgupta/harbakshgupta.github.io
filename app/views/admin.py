import random
import string
import re
import datetime
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint, send_from_directory
from passlib.hash import sha256_crypt as sha
from ..models.models import Admin, blogPosts
from app import *

admin = Blueprint('admin', __name__, url_prefix='/admin')
BLOG_IMAGE_PATH = "/assets/img/blog/"

@admin.route('/login' , methods=['POST','GET'])
def login():
    isAdmin = session.get("admin",False)
    if request.method=="POST":
        user = request.form.get("username", "default")
        password = request.form.get("password", "default")
        result = db.first_or_404(db.select(Admin).filter_by(username=user))
        invalid_credentials = False
        if result is not None:
            if result.username==user and sha.verify(password, result.password):
                session["admin"] = True
                session.permanent = True
                flash("Login Successful","success")
                return redirect(url_for("main.index"))
            else:
                invalid_credentials = True
        else:
            invalid_credentials = True
        if invalid_credentials:
            flash("Invalid Credentials, please try again!","danger")
            return redirect(url_for("admin.login"))
    else:
        return render_template('admin/login.html', admin=isAdmin)

@admin.route('/dashboard', methods=['POST','GET'])
def dashboard():
    isAdmin = session.get("admin", False)
    if request.method=="POST":
        title = request.form.get("title", "default")
        image = request.form.get("image", "default")
        content = request.form.get("content", "default")
        visible = request.form.get("visible", "off")
        slug = request.form.get("slug", "default")
        short_desc = request.form.get("description", "default")
        date = None
        print(visible)
        if visible == "on":
            date = datetime.datetime.now().strftime("%d %B, %Y")
            visible = True
        else:
            visible = False
        if len(title)==0 or len(image)==0 or len(content)==0 or len(slug)==0 or len(short_desc)==0:
            flash("Empty Fields, please try again!","danger")
        else:
            image_url = os.path.join(BLOG_IMAGE_PATH, image)
            newBlogPost = blogPosts(title=title, image=image_url, content=content, date=date, visible=visible, slug=slug, short_desc=short_desc)
            db.session.add(newBlogPost)
            db.session.commit()
            flash("Blog Post Added Successfully","success")
        return redirect(url_for("admin.dashboard"))
    if isAdmin:
        return render_template('admin/dashboard.html', admin=isAdmin)
    else:
        return redirect(url_for("admin.login"))

@admin.route('/logout')
def logout():
    session.pop("admin", False)
    flash("Logged Out","success")
    return redirect(url_for("admin.login"))

@admin.route('/delete-post/<slug>')
def delete_post(slug):
    isAdmin = session.get("admin",False)
    if isAdmin:
        db.session.query(blogPosts).filter_by(slug=slug).delete()
        db.session.commit()
        flash("Blog Post Deleted Successfully","success")
        return redirect(url_for("admin.dashboard"))
    else:
        return redirect(url_for("admin.login"))