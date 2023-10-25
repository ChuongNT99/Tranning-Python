from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = [
    {"id": 1, "name": "Tuan", "age": 24},
    {"id": 2, "name": "Hai", "age": 25},
    {"id": 3, "name": "Binh", "age": 26}
]

@app.route('/add_user_page', methods=["GET"])
def add_user_page():
    return render_template('create_user.html')

@app.route('/users', methods = ["GET"])
def get_users():
 return jsonify({"users":users})

@app.route('/user/<int:user_id>', methods = ["GET"])
def get_user(user_id):
    user = next(( user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@app.route('/user', methods=["POST"])
def create_user():
    data = request.get_json()
    if "name" in data and "age" in data:
        new_id = max(users, key=lambda user: user["id"])["id"] + 1
        new_user = {"id": new_id, "name": data["name"], "age": data["age"]}
        users.append(new_user)
        return jsonify({"message": "Người dùng mới đã được thêm."}), 201
    return jsonify({"message": "Dữ liệu không hợp lệ."}), 400

if __name__ == '__main__':
    app.run(debug=True)
