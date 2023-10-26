from flask import Flask, jsonify

app = Flask(__name__)

# Tạo một đoạn middleware đơn giản để xử lý CORS
class CorsMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        def new_start_response(status, response_headers, exc_info=None):
            response_headers.append(('Access-Control-Allow-Origin', '*'))
            response_headers.append(('Access-Control-Allow-Headers', 'Content-Type'))
            return start_response(status, response_headers, exc_info)

        return self.app(environ, new_start_response)

# Sử dụng middleware CorsMiddleware để xử lý CORS
app.wsgi_app = CorsMiddleware(app.wsgi_app)

@app.route('/')
def hello():
    return jsonify(message="Hello, CORS is allowed!")

if __name__ == '__main__':
    app.run(debug=True)
