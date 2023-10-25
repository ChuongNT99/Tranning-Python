from flask import Flask, session
import os

app = Flask(__name__)

# Tạo secret key
def generate_secret_key():
    return os.urandom(24)

# Thiết lập secret key cho ứng dụng Flask
app.secret_key = generate_secret_key()

if app.secret_key:
    print("Secret key đã được đặt.")
else:
    print("Chưa có secret key được đặt.")

@app.route('/')
def home():
    # Lưu một giá trị vào session
    session['user_id'] = 123
    return 'Secret key đã được tạo và sử dụng.'

if __name__ == '__main__':
    app.run(debug=True)
