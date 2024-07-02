import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token


app = Flask(__name__)
app.config = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', '')