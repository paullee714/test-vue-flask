from flask_cors import CORS
from flask import Flask, jsonify, request
from pymongo import MongoClient

import os

# instantiate the app
app = Flask(__name__)

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
    data = request.get_json()
    username = data.get('username')
    nickname = data.get('nickname')
    email = data.get('email')
    password = data.get('password')

    user_data = {
        "username" : username,
        "nickname" : nickname,
        "email" : email,
        "password" : password
    }
    db.users.insert_one(user_data)

    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.getenv('FLASK_RUN_PORT'),debug=os.getenv('FLASK_DEBUG'))