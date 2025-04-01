# PretendingGreatness: Michelle, Victor, Mark, Jessica
# P4: Makers Makin' It, Act II -- The Seequel
# SoftDev
# March 2025

from flask import Flask, render_template, session, request, redirect, url_for
from user_db import *
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

createUsers()

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("home.html")
    

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/graph')
def graph():
    return "hi"

@app.route('/analysis')
def analysis():
    return "hi"

if __name__ == "__main__":
    app.debug = True
    app.run()
