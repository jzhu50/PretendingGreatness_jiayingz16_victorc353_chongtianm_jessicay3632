# PretendingGreatness: Michelle, Victor, Mark, Jessica
# P4: Makers Makin' It, Act II -- The Seequel
# SoftDev
# March 2025

from flask import Flask, render_template, session, request, redirect, url_for
from user_db import *
from AI import *
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

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if not prompt:
            return render_template('analysis.html', error="Please enter a prompt.")
        else:
            response = getGeminiResponse('AIzaSyBUudUUQJh-fGmE-iOPm_1A8caQTb62nJ4', prompt)
            return render_template('analysis.html', response=response)
    return render_template('analysis.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('logout'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
