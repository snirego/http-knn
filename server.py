from curses import window
from flask import Flask, render_template
import base64
from flask import Flask, render_template, redirect, url_for, request
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
# from keras.datasets import mnist

from knn import KNN
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/draw")
def draw():
    return render_template("draw.html")

@app.route("/pred")
def pred(prediction=None):
    return render_template("pred.html", pred=prediction)

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
    # print((image_to_predict))

    base64_img_bytes = base64_img.encode('utf-8')
    with open('decoded_image.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

    image = cv2.imread('decoded_image.png')

    invert = cv2.bitwise_not(image)
    invert_two = cv2.bitwise_not(invert)
    
    cv2.imwrite('inverted_image.png', invert_two)

    resized = cv2.resize(invert_two, (8,8), interpolation = cv2.INTER_AREA)

    resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
 
    # print('Resized Dimensions : ',resized.shape)
    
    cv2.imwrite('resized_image.png', resized)

    # Start KNN Prediction
    knn = KNN(3)

    digits = load_digits()
    x_train = digits.data[0:1400]
    y_train = digits.target[0:1400]
    x_test = digits.data[1400:]
    y_test = digits.target[1400:]

    knn.fit(x_train, y_train)
    print('Our KNN Prediction --->', knn.predict(resized.reshape(1, -1)))

    svm = SVC()
    svm.fit(x_train, y_train)
    print('SVM Prediction --->', svm.predict(resized.reshape(1, -1)))

    rf = RandomForestClassifier()
    rf.fit(x_train, y_train)
    print('Random Forest Prediction --->', rf.predict(resized.reshape(1, -1)))

    xgb = XGBClassifier()
    xgb.fit(x_train, y_train)
    print('XGBoost Prediction --->', xgb.predict(resized.reshape(1, -1)))

    
    # return render_template('pred.html', pred=knn.predict(resized.reshape(1, -1)))
    return '<h1> Prediction Header </h1>'


if __name__ == "__main__":
    # app.run(host="10.0.1.83")
    app.run(host="127.0.0.1")