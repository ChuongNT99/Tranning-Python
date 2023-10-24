from flask import Flask

app = Flask(__name__)

@app.route('/')  # Xác định URL cho hàm hello_world
def hello_world():
    return 'Hello, World!'

@app.route('/about')  # Xác định URL cho hàm about
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run()
