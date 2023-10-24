from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Thư mục để lưu trữ các tệp tải lên
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('file_upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Kiểm tra xem yêu cầu có chứa tệp tải lên hay không
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # Kiểm tra xem tệp đã chọn có tên không trống
    if file.filename == '':
        return 'No selected file'

    # Kiểm tra xem thư mục UPLOAD_FOLDER đã tồn tại chưa
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Lưu tệp tải lên vào thư mục lưu trữ
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
