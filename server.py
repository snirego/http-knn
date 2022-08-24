from flask import Flask, render_template
import random
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
    result = []
    data = request.get_json()
    image_to_predict = data['img_base64'] #will give you array a
    # image_to_predict.replace('data:image/png;base64,', '')
    #To test you got the data do a print statement

    

    # The for loop is not necessary if you pass the newArray directly to 
    # your template "output.html".
    #
    #for element in newArray:
    #    result.append(element)
    #
    #like this
    # return render_template('index.html', element=image_to_predict)
    from PIL import Image
    from io import BytesIO
    import base64

    # data['img_base64']
    
    # im = Image.open(BytesIO(base64.b64decode(image_to_predict * (-len(image_to_predict) % 4))))
    # im.save('test.png')


    base64_img = image_to_predict.replace('data:image/png;base64,', '')
    print((image_to_predict))

    base64_img_bytes = base64_img.encode('utf-8')
    with open('decoded_image.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        # im = Image.open(file_to_save)
        # im.save('decoded_image.png')
        file_to_save.write(decoded_image_data)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="10.0.0.82")
    # app.run(debug=True)