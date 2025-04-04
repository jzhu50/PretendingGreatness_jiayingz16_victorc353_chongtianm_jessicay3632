# PretendingGreatness: Michelle, Victor, Mark, Jessica
# P4: Makers Makin' It, Act II -- The Seequel
# SoftDev
# March 2025

from flask import Flask, render_template, session, request, redirect, url_for, jsonify
import os

from graphloading import *
from user_db import *
from AI import *

app = Flask(__name__)
app.secret_key = os.urandom(32)

createUsers()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/registerPage', methods=['GET'])
def registerPage():
    return render_template("registerPage.html")

@app.route('/auth_register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    result = addUser(username, password)
    if result is None:
        session['username'] = username
        return redirect(url_for('home'))
    return render_template("home.html", error=result)

@app.route('/auth_login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    result = checkPass(username, password)
    if result is None:
        session['username'] = username
        return redirect(url_for('graph'))
    return render_template('home.html')

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    username = session.get('username')
    if username is None:
        return redirect(url_for('graph.html'))
    return render_template('graph.html', username="Welcome, " + username + " !")

@app.route('/api/tesla_stock_data')
def tesla_stock_data():
    return jsonify(tsla_data())

@app.route('/analysis')
def analysis():
    """for testing purpose"""
    prompt = "Predict whether the Tesla stocks will go up or down given the following tweet: RT @BillyM2k: dude bookmarks are an awesome twitter feature, especially when preparing for a twitter"
    response = getGeminiResponse('AIzaSyBUudUUQJh-fGmE-iOPm_1A8caQTb62nJ4', prompt)
    #print(response)
    return render_template('analysis.html', response=response)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('logout'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='5001')