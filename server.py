from flask import Flask, render_template
import base64
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/draw")
def draw():
    return render_template("draw.html")

@app.route('/signup')
def signup():
    return render_template('sign_up.html')  # render a template

@app.route('/signin')
def signin():
    return render_template('sign_in.html')  # render a template

@app.route('/output', methods=['POST'])
def output():
    data = request.get_json()
    image_to_predict = data['img_base64'] #will give you array a

    base64_img = image_to_predict.replace('data:image/png;base64,', '')
    print((image_to_predict))

    base64_img_bytes = base64_img.encode('utf-8')
    with open('decoded_image.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="10.0.0.82")