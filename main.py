from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Em Breve teremos uma pesquisa de satisfação para melhor atender nossos clientes'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return render_template('user.html', username=username)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='Jhon Doe'))


if __name__ == '__main__':
    app.run(debug=True)

