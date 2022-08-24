from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/user/<user>")
# def user(user):
#     return "<h1>Hello, {}!<h1/>".format(user)

# @app.route("/signup")
# def rand():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(host="10.0.1.83")