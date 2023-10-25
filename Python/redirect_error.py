from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    # Thực hiện chuyển hướng đến trang '/about'
    return redirect('/about')

@app.route('/about')
def about():
    return 'This is the About page'

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main':
    app.run()
