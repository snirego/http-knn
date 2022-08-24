from flask import Flask, render_template
import base64
from flask import Flask, render_template, redirect, url_for, request
import pymongo

app = Flask(__name__)

def access_check(username, password):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["user_system"]
    mycol = mydb["users"]
    user= mycol.find_one({"username": username})
    if user is None:
        return False
    elif user["password"] == password:
        return True


    # user_dict = mycol.find_one({"username": username})
    # print(user_dict)
    # if user_dict is not None:
    #     return(user_dict["password"] == password)

# @app.route("/n")
# def n():
#     return str(access_check("elior", "n"))


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

# from flask import request

@app.route('/addRegion', methods=['POST'])
def addRegion():
    ...
    return (request.form['projectFilePath'])

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



# @app.route('/sing_in', methods=['POST', 'GET'])
# def sing_in():
#     if request.method == 'POST':
#         # data = request.get_json()
#         user_name = request.form['username']
#         password = request.form['password']
#         access = access_check(user_name, password)
#         if access:
#             return render_template('index.html')
#     else:
#         return render_template('sign_in.html')

if __name__ == "__main__":
    # app.run(host="10.0.0.82")
    app.run(host="127.0.0.1")
    
