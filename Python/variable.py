from flask import Flask, jsonify

app = Flask(__name__)

# Tạo một danh sách chứa thông tin của các user
users = [
    {
        'id': 1,
        'name': 'John Doe',
        'age': 30,
        'school': 'ABC School'
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'age': 25,
        'school': 'XYZ School'
    }
]

@app.route('/user/<int:user_id>')
def show_user(user_id):
    # Tìm user có id tương ứng trong danh sách users
    user = next((user for user in users if user['id'] == user_id), None)

    if user is not None:
        # Trả về thông tin của user dưới dạng JSON
        return jsonify(user)
    else:
        return 'User not found', 404

if __name__ == '__main__':
    app.run(debug=True)
