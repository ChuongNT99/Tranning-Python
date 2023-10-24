from flask import Flask, url_for

app = Flask(__name__)

# Dữ liệu giả lập các bài viết trong ứng dụng blog
posts = [
    {'id': 1, 'title': 'Introduction to Flask', 'content': 'This is a Flask tutorial.'},
    {'id': 2, 'title': 'Flask Routing', 'content': 'Learn how to route in Flask.'},
    {'id': 3, 'title': 'Flask Templates', 'content': 'Using templates in Flask applications.'}
]

@app.route('/')
def home():
    return 'Welcome to our blog!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Tìm bài viết dựa trên post_id
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if post:
        return f'Title: {post["title"]}<br>Content: {post["content"]}'
    else:
        return 'Post not found', 404

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('home'))  # Xây dựng URL cho trang chính, kết quả: '/'
        print(url_for('show_post', post_id=1))  # Xây dựng URL cho bài viết 1, kết quả: '/post/1'
        print(url_for('show_post', post_id=2))  # Xây dựng URL cho bài viết 2, kết quả: '/post/2'
