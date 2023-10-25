from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '123456'

from flask_session import Session

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    return render_template('demo_session.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Please enter a username."
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
