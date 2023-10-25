from flask import Flask, jsonify, send_file, Response
import json
from collections import OrderedDict


app = Flask(__name__)

# Phản hồi về dữ liệu JSON
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    response = Response(response=json.dumps(data, indent=4), status=200, content_type='application/json; charset=utf-8')
    return response

#Phản hồi về tệp
@app.route('/download')
def download_file():
    path = 'uploads/logo.png'  # Đường dẫn đến tệp muốn trả về
    return send_file(path, as_attachment=True)

#Phản hồi về văn bản
@app.route('/about')
def about():
    return 'This is the About page'

if __name__ == '__main__':
    app.run()