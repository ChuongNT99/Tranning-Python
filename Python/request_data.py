from flask import Flask, request

app = Flask(__name__)

# Truy cập method của request
@app.route('/example1', methods=['GET', 'POST'])
def example1():
    method = request.method
    return f'This request uses the {method} method.'

# Truy cập tham số truy vấn (query parameters):
@app.route('/example2', methods=['GET'])
def example2():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Name: {name}, Age: {age}'

# Truy cập dữ liệu biểu mẫu (form data):
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f'Logging in as {username}...'

# Truy cập header của request:
@app.route('/user-agent', methods=['GET'])
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return f'User-Agent: {user_agent}'  