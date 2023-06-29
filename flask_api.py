# Implement a Flask API with token-based authentication

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

@app.route('/api/login', methods=['POST'])
def login():
    # User login authentication
    # ...
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    # Protected route accessible only with a valid token
    # ...
    return jsonify(message='Success')

if __name__ == '__main__':
    app.run(debug=True)
