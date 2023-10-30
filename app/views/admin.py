import random
import string
import re
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint, send_from_directory
from flask_session import Session
from passlib.hash import sha256_crypt as sha
from ..models.models import Admin, blogPosts
from app import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/login' , methods=['POST','GET'])
def login():
    if request.method=="POST":
        user = request.form.get("username", "default")
        password = request.form.get("password", "default")
        result = db.first_or_404(db.select(Admin).filter_by(username=user))
        invalid_credentials = False
        if result is not None:
            if result.username==user and sha.verify(password, result.password):
                session["admin"] = True
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
        return render_template('admin/login.html')

@admin.route('/dashboard')
def dashboard():
    admin = session.get("admin",False)
    if admin:
        return render_template('admin/dashboard.html', admin=admin)
    else:
        return redirect(url_for("admin.login"))

@admin.route('/logout')
def logout():
    session.pop("admin", False)
    return redirect(url_for("admin.login"))