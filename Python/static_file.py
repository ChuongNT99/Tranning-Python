from flask import Flask, Blueprint, render_template

# Tạo ứng dụng Flask
app = Flask(__name__)

# Tạo blueprint
main = Blueprint('main', __name__, static_folder='static', template_folder='templates')

# Đăng ký blueprint
app.register_blueprint(main)

# Xác định route trên ứng dụng chính
@app.route('/')
@app.route('/static/')
@app.route('/static/<name>')
def static_files(name=None):
    return render_template('demo.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
