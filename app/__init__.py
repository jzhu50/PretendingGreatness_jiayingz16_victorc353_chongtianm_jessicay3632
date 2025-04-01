# PretendingGreatness: Michelle, Victor, Mark, Jessica
# P4: Makers Makin' It, Act II -- The Seequel
# SoftDev
# March 2025

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return "hi"

@app.route('/graph')
def graph():
    return "hi"

@app.route('/analysis')
def analysis():
    return "hi"

if __name__ == "__main__":
    app.debug = True
    app.run()
