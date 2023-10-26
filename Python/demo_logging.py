from flask import Flask
import logging


app = Flask(__name__)

user = { "username": "Chuong"}

# Cấu hình logging
app.logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.disabled = True


@app.route('/')
def home():
    app.logger.debug('Truy cập trang chủ')
    return 'Trang chủ'

@app.route('/log')
def hello():
    app.logger.debug('Đây là một debug message')
    app.logger.debug(f'Username: {user["username"]}')
    app.logger.info('Đây là một info message')
    app.logger.warning('Đây là một warning message')
    app.logger.error('Đây là một error message')
    app.logger.critical('Đây là một critical message')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
