from flask import escape, request, Flask

app = Flask(__name__)

@app.route('/some_route', methods=['POST'])
def some_route():
    user_input = request.form['user_input']
    escaped_input = escape(user_input)
    return f'You entered: {escaped_input}'
