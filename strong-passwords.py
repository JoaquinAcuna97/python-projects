from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if not is_strong_password(password):
        return jsonify({"message": "Password must be at least 8 characters long, contain uppercase, lowercase, a number, and a special character"}), 400

    hashed_password = generate_password_hash(password)
    
    # Here you would save the user to the database
    # For example: save_user_to_db(username, hashed_password)
    
    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)