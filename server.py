from urllib import response
from flask import Flask, render_template
import base64
from flask import Flask, render_template, request
from sklearn.datasets import load_digits
from keras.datasets import mnist

from knn import KNN
import cv2
import numpy as np
import json
import io
import os

app = Flask(__name__)

prediction = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/draw", methods=['GET', 'POST'])
def draw():
    return render_template("draw.html")


@app.route('/form_signup', methods = ['GET','POST'])
def signup():
    try:
        with open("users.json", "r") as file:
            dictionary = json.load(file)
            if request.method == 'POST':  
                username = request.form["username"]
                password = request.form["password"]
                dictionary[username]= password
                with open("users.json", "w") as write_file:
                    json.dump(dictionary, write_file, indent=4)
                return render_template("draw.html")
    except:
        print("File not found in signup")
    return render_template('signup.html')


@app.route('/form_sigin', methods=['GET','POST'])
def signin():
    try:
        with open('users.json', "r") as file:
            dictionary = json.load(file)
            print(dictionary)
            if request.method == 'POST':  
                username = request.form["username"]
                password = request.form["password"]  
                for key,value in dictionary.items():
                    if key == username and value == password:
                        return render_template("draw.html")
                return render_template("signinerror.html")
    except:
        print("File not found in signin")
    return render_template('signin.html')


@app.route('/output', methods=['POST'])
def output():
    try:
        data = request.get_json()
        image_to_predict = data['img_base64'] #will give you array a

        base64_img = image_to_predict.replace('data:image/png;base64,', '')

        # Decode the base64 string image
        base64_img_bytes = base64_img.encode('utf-8')
        with open('decoded_image.png', 'wb') as file_to_save:
            decoded_image_data = base64.decodebytes(base64_img_bytes)
            file_to_save.write(decoded_image_data)

        # Dealing with the image
        image = cv2.imread('decoded_image.png')

        # Invert the image colors so it will be similar to the dataset
        invert = cv2.bitwise_not(image)
        invert_two = cv2.bitwise_not(invert)
        cv2.imwrite('inverted_image.png', invert_two)


        # Resize the image to 8x8 pixels like the sklearn.load_digits dataset
        # resized = cv2.resize(invert_two, (8,8), interpolation = cv2.INTER_AREA)
        
        # Resize the image to 20x20 pixels like the dataset
        resized = cv2.resize(invert_two, (20,20), interpolation = cv2.INTER_AREA)
        resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)    
        cv2.imwrite('resized_image.png', resized)


    # region Old code - sklearn.load_digits dataset
        # # Start KNN Prediction
        # knn = KNN(3)

        # digits = load_digits()
        # x_train = digits.data[0:1400]
        # y_train = digits.target[0:1400]
        # x_test = digits.data[1400:]
        # y_test = digits.target[1400:]


        # knn.fit(x_train, y_train)
        # print('Our KNN Prediction --->', knn.predict(resized.reshape(1, -1)))

    # endregion

        # ----------------------------------------------------------------------------
        # NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW
        # ----------------------------------------------------------------------------
        # Read the image
        data_image = cv2.imread('digits.png')
        
        # gray scale conversion
        gray_img = cv2.cvtColor(data_image, cv2.COLOR_BGR2GRAY)
        
        # We will divide the image
        # into 5000 small dimensions 
        # of size 20x20
        divisions = list(np.hsplit(i,100) for i in np.vsplit(gray_img,50))
        
        # Convert into Numpy array
        # of size (50,100,20,20)
        NP_array = np.array(divisions)
        
        # Preparing train_data
        # and test_data.
        # Size will be (2500,20x20)
        x_train = NP_array[:,:50].reshape(-1,400).astype(np.float32)
        
        # Size will be (2500,20x20)
        x_test = NP_array[:,50:100].reshape(-1,400).astype(np.float32)
        
        # Create 10 different labels 
        # for each type of digit
        k = np.arange(10)
        y_train = np.repeat(k,250)[:,np.newaxis]
        y_test = np.repeat(k,250)[:,np.newaxis]
        
        # Initiate kNN classifier
        knn = KNN(3)
        
        # Train the classifier
        knn.fit(x_train, y_train)
        
        global prediction
        prediction = knn.predict(resized.reshape(1, -1))
        
        print('Our KNN Prediction --->', prediction)
        # ----------------------------------------------------------------------------


        # return render_template('pred.html', pred=knn.predict(resized.reshape(1, -1)))
        return render_template('draw.html', response=str(prediction), success=True)

    except Exception as e:
        print(e)
        return render_template('draw.html', response=str(prediction), success=False)


if __name__ == "__main__":
    # app.run(host="10.0.1.83")
    import socket
    def extract_ip():
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:       
            st.connect(('10.255.255.255', 1))
            IP = st.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            st.close()
        return IP
    print(extract_ip())
    # app.run(host="127.0.0.1")
    app.run(host=f"{extract_ip()}")