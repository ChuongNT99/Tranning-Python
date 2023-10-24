from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    username = "John"
    return render_template('index.html', username=username)
