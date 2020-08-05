from flask_cors import CORS
from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import jwt
import datetime

import os

# instantiate the app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.vue_app

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/', methods=['GET'])
def test_router():
    return jsonify('This is flask developments Server!')

@app.route('/signup',methods=['POST'])
def signup_router():
    bcrypt = Bcrypt()
    data = request.get_json()
    username = data.get('username')
    nickname = data.get('nickname')
    email = data.get('email')
    password = data.get('password')
    pass_has = bcrypt.generate_password_hash(password)

    user_data = {
        "username" : username,
        "nickname" : nickname,
        # "email" : email,
        "password" : pass_has
    }
    db.users.insert_one(user_data)

    return data

@app.route("/login",methods=['POST'])
def login_router():
    bcrypt = Bcrypt()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_data = db.users.find_one({"username":username})

    token = jwt.encode({
        'sub': user_data.get("username"),
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, os.getenv('SECRET_KEY'))

    get_password =user_data.get('password')

    login_data = {}
    if bcrypt.check_password_hash(get_password,password):
        result = {
            "username" : user_data.get("username"),
            # "email" : user_data.get("email"),
            "nickname" : user_data.get("nickname"),
            "token":token.decode('utf8')
        }
        login_data = {
            "user":result,
            "success":True
        }
    else:
        result = {
            "username": "",
            # "email": "",
            "nickname": ""
        }
        login_data = {
            "user": None,
            "success": False
        }
    return jsonify(login_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050,debug=os.getenv('FLASK_DEBUG'))