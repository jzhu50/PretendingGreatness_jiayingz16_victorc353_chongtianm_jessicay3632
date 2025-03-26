from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return "hi"

if __name__ == "__main__":
    app.debug = True
    app.run()
