import random
import string
import re
from flask import Flask, request, render_template, flash, redirect, url_for, session, Blueprint, send_from_directory
from flask_session import Session
from passlib.hash import sha256_crypt as sha
# from flask_mail import Mail, Message
from app import *

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/login' , methods=['POST','GET'])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        if email=="admin@123" and password=="admin@123":
            session["admin"] = True
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Invalid Credentials, please try again!","danger")
            return redirect(url_for("admin.login"))
    else:
        return render_template('admin/login.html')

@admin.route('/dashboard')
def dashboard():
    if "admin" not in session:
        return redirect(url_for("main.index"))
    else:
        return redirect(url_for("admin.login"))

@admin.route('/logout')
def logout():
    session.pop("admin", False)
    return redirect(url_for("admin.login"))