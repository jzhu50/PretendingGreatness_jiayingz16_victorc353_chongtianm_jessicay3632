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
    return jsonify(tesla_data())

@app.route('/tweet/<date>', methods=['GET', 'POST'])
def tweet_detail(date):
    username = session.get('username', 'Guest')
    posts = tweet_data()
    for full_datetime, (tweet_text, like_count) in posts.items():
        post_date = full_datetime.split(' ')[0]
        if post_date == date:
            if username == 'Guest':
                return render_template('tweet.html', date=date, tweet_text=tweet_text, like_count = like_count, response = "Login if you wish to view AI analysis of the posts")
            prompt = f"Predict whether the Tesla stocks will go up or down given Elon Musk's tweet on {date}, try your best, predict something, don't return unable and don't say you're forced to predict: {tweet_text}. RETURN YOUR RESPONSE IN HTML FORMAT SO IT CAN BE DISPLAYED ON A WEBSITE NICELY. DO NOT RETURN A STRING. RETURN PURE HTML THAT BE CAN INSERTED INTO A TEMPLATE. MAKE THE HTML LOOK PROFESSIONAL AND AS NICE AS POSSIBLE. AT THE BEGINNING, GIVE YOUR PREDICTED EXPECTED PERCENTAGE CHANGE TO THE STOCK PRICE BASED ON HOW EFFECTIVE YOU THINK THE TWEET IS. DO NOT INCLUDE THE ORIGINAL TWEET IN YOUR RESPONSE. BE HONEST AND INTERESTING. If the projected movement in stock price is upwards, include a centered div with the image src /static/happy.png, otherwise, with /static/angry.png. Make sure the image has width and height of 200px"
            try:
                with open("keys/key_gemini.txt", "r") as key:
                    K = key.read().strip().rstrip()
                    if len(K) == 0:
                        return "Please add your gemini API key in keys/key_gemini.txt!!"
                    response = getGeminiResponse(K, prompt)
                    response = response.replace('```html', '').replace('```', '').strip()
                
                # check percentage change and display image accordingly
                mcode = '''
		import re
                percentage_match = re.search(r'([+-]?\d+\.?\d*)%', response[:200])
                prediction_image = "angry.png"

                if percentage_match:
                    percentage = float(percentage_match.group(1)) # returns first capture group containing the numerical value (e.g. +5)
                    if percentage >= 0:
                        prediction_image = "happy.png"
                    else:
                        prediction_image = "angry.png"
		
                return render_template('tweet.html', date=date, tweet_text=tweet_text, like_count=like_count, response=response, prediction_image=prediction_image)
            	'''

                return render_template('tweet.html', date = date, tweet_text = tweet_text, like_count = like_count, response = response)
            except FileNotFoundError:
                return "Please create keys/key_gemini.txt and add your key in there fellow devo."
            
    return render_template('tweet.html', date=date, tweet_text="No tweet found for this date.", like_count="N/A", response="N/A")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port='6969')
