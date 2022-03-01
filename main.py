from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return render_template('user.html', username=username)


@app.route('/user')
def user():
    return render_template('user.html')


if __name__ == '__main__':
    app.run(debug=True)
