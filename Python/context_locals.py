# APLICATION CONTEXT
from flask import Flask, request, session

app = Flask(__name__)
app.config['APP_NAME'] = 'FLY BIRD'
app_name = app.config['APP_NAME']

# Kích hoạt Application Context
with app.app_context():
    # Bây giờ có thể thao tác với ứng dụng Flask
    app.config['DEBUG'] = True

# Có thể truy cập app.config ở bên ngoài context
app_name = app.config['APP_NAME']

#################################################################################

# REQUEST CONTEXT
@app.route('/hello', methods=['GET'])
def hello():
    # Request Context được kích hoạt tự động
    method = request.method  # Phương thức HTTP
    url = request.url  # URL của yêu cầu
    return f'Method: {method}, URL: {url}'

################################################################################

# SESSION REQUEST
@app.route('/login')
def login():
    # Kích hoạt Session Context
    with app.test_request_context('/login'):
        # Bây giờ bạn có thể thiết lập và lưu trữ thông tin phiên người dùng
        session['user_id'] = 123


