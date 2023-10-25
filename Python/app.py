from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Giới hạn kích thước tệp lên tối đa là 16 MB

def allowed_file(filename):
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions

@app.route('/')
def index():
    return render_template('file_upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    # Kiểm tra xem tệp đã chọn có tên không trống
    if file.filename == '':
        return 'No selected file'

    # Kiểm tra kích thước tệp
    if len(file.read()) > app.config['MAX_CONTENT_LENGTH']:
        return 'File size exceeds the allowed limit'

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    if file and allowed_file(file.filename):
        # Xử lý tải lên tệp ở đây
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File uploaded successfully'
    else:
        return "Invalid file. Only files with the extension jpg, jpeg, png or gif are accepted."


if __name__ == '__main__':
    app.run(debug=True)
