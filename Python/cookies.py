from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Đọc cookie có tên 'username' từ request
    username = request.cookies.get('username')
    
    if username:
        return f'Hello, {username}!'
    else:
        return 'Hello, guest!'

@app.route('/setcookie/<username>')
def set_cookie(username):
    # Tạo một response object
    resp = make_response(f'Setting username cookie to {username}')
    
    # Đặt cookie có tên 'username' với giá trị là 'username'
    resp.set_cookie('username', username)
    
    return resp

@app.route('/deletecookie')
def delete_cookie():
    # Tạo một response object để xóa cookie
    resp = make_response('Cookie deleted')
    
    # Xóa cookie có tên 'username'
    resp.delete_cookie('username')
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)
