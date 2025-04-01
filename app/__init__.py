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
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login')) 
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = addUser(username, password)
        if result is None:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template("register.html", error=result)
    return render_template("register.html")

@app.route('/login')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = checkPass(username, password)
        if result is None:
            session['username'] = username
            return redirect(url_for('home'), username=session['username'])
        else:
            return redirect(url_for('login'), error=result)
    return render_template("login.html")

@app.route('/graph')
def graph():
    return "hi"

@app.route('/analysis')
def analysis():
    return "hi"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('logout'))

if __name__ == "__main__":
    app.debug = True
    app.run()
