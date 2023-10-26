from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_session import Session
import os

app = Flask(__name__)

# Tạo secret key
app.secret_key = os.urandom(24)

# Cấu hình session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        flash('Đăng nhập thành công!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Sai tên đăng nhập hoặc mật khẩu!', 'danger')
        return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
