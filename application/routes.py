from flask import render_template , jsonify,request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from . import application

# Sample data to simulate a database
sample_data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
]

users = {
    "testuser": {"password": "testpassword"}
}

@application.route('/')
def home():
    return render_template('index.html')


@application.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # print(username)
    # print(password)
    # exit()
    
    user = users.get(username, None)
    # print("user from top",user)
    # exit()
    if user and user["password"] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@application.route('/api/items', methods=['GET'])
@jwt_required()
def get_items():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user, items=sample_data), 200

@application.route('/api/items/<int:item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    item = next((item for item in sample_data if item["id"] == item_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@application.route('/api/items', methods=['POST'])
@jwt_required()
def create_item():
    new_item = request.json
    new_item["id"] = len(sample_data) + 1
    sample_data.append(new_item)
    return jsonify(new_item), 201
