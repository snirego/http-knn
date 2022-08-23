from flask import Flask
import random
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/user/<user>")
def user(user):
    return "<h1>Hello, {}!<h1/>".format(user)

@app.route('/')
def welcome():
    return render_template("welcome.html")  # render a template

@app.route('/log_in')
def log_in():
    return render_template("log_in.html")
    
@app.route('/sing_up')
def sing_up():
    return render_template("sing_up.html")

if __name__ == "__main__":
    # app.run(host="10.0.1.83")
    app.run(debug=True)