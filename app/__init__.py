# PretendingGreatness: Michelle, Victor, Mark, Jessica
# P4: Makers Makin' It, Act II -- The Seequel
# SoftDev
# March 2025

from flask import Flask, render_template, session, request, redirect, url_for, jsonify
import os
from datetime import datetime

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
    username = session.get('username', 'Guest')
    return render_template('graph.html', username=username)

@app.route('/api/tesla_stock_data')
def tesla_stock_data():
    return jsonify(aaaaa())

@app.route('/tweet/<date>', methods=['GET', 'POST'])
def tweet_detail(date):
    posts = tweet_data()
    for full_datetime, (tweet_text, like_count) in posts.items():
        post_date = full_datetime.split(' ')[0]
        if post_date == date:
            prompt = f"Predict whether the Tesla stocks will go up or down given Elon Musk's tweet on {date}, try your best, predict something, don't return unable: {tweet_text}. RETURN YOUR RESPONSE IN HTML FORMAT SO IT CAN BE DISPLAYED ON A WEBSITE NICELY. DO NOT RETURN A STRING. RETURN PURE HTML THAT BE CAN INSERTED INTO A TEMPLATE. AT THE BEGINNING, GIVE A SCORE FROM -100 TO 100 TO HOW EFFECTIVE YOU THINK THE TWEET IS TO TESLA STOCK CHANGES. BE HONEST AND INTERESTING."
            with open("keys/key_gemini.txt", "r") as key:
                response = getGeminiResponse(key.read().strip().rstrip(), prompt)
                response = response.replace('```', '')
                response = response.replace('html', '')
            return render_template('tweet.html', date=date, tweet_text=tweet_text, like_count=like_count, response=response)
    return render_template('tweet.html', date=date, tweet_text="No tweet found for this date.", like_count="N/A", response="N/A")

'''
@app.route('/analysis')
def analysis():
    """for testing purpose"""
    prompt = "Predict whether the Tesla stocks will go up or down given the following tweet, try your best, predict something, don't return unable to predict: RT @BillyM2k: dude bookmarks are an awesome twitter feature, especially when preparing for a twitter"
    response = getGeminiResponse('AIzaSyBUudUUQJh-fGmE-iOPm_1A8caQTb62nJ4', prompt)
    return render_template('analysis.html', response=response)
'''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('logout'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='6969')
