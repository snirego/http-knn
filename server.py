from flask import Flask
import random
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/user/<user>")
def user(user):
    return "<h1>Hello, {}!<h1/>".format(user)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


if __name__ == "__main__":
    # app.run(host="10.0.1.83")
    app.run(debug=True)