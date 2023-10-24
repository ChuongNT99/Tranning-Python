from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Trang chủ'

@app.route('/about')
def about():
    return 'Về chúng tôi'

@app.route('/contact')
def contact():
    return 'Liên hệ'

@app.route('/old-url')
def old_url():
    return redirect(url_for('new_url'))

@app.route('/new-url')
def new_url():
    return 'Đây là URL mới'