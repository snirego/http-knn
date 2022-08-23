from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/user/<user>")
def user(user):
    return "<h1>Hello, {}!<h1/>".format(user)

@app.route("/random")
def rand():
    return "<h1>{}<h1/>".format(random.randint(1,100))

if __name__ == "__main__":
    app.run(host="10.0.1.83")