from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        # Truy cập thông tin từ tham số truy vấn (query parameters)
        name = request.args.get('name', 'Guest')
        return f'Hello, {name}!'
    elif request.method == 'POST':
        # Truy cập dữ liệu từ biểu mẫu gửi lên (form data)
        user_input = request.form['user_input']
        return f'You entered: {user_input}'
    else:
        return 'Invalid request method'

if __name__ == '__main__':
    app.run(debug=True)
