from flask import Flask, render_template
import random
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template('sign_up.html')  # render a template

@app.route('/signin')
def signin():
    return render_template('sign_in.html')  # render a template


if __name__ == "__main__":
    # app.run(host="10.0.1.83")
    app.run(debug=True)