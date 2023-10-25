from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Thư mục để lưu trữ các tệp tải lên
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024  # Giới hạn kích thước file lên tối đa là 100 KB


@app.route('/')
def index():
    return render_template('file_upload.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in {'jpg', 'jpeg', 'png', 'gif'}

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

    # Kiểm tra xem tệp là hợp lệ
    if file and allowed_file(file.filename):
        # Kiểm tra có quá dung lượng tối đa hay không
        if file.content_length <= app.config['MAX_CONTENT_LENGTH']:
            # Lưu tệp tải lên vào thư mục lưu trữ
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'File uploaded successfully'
        else:
            return 'File size exceeds the allowed limit'
    return 'Invalid file or no file provided'

if __name__ == '__main__':
    app.run(debug=True)
