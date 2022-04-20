from flask import Flask, render_template, request
from db import create_database
from pesquisa import store

app = Flask("__name__")


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/create_db')
def create_db():
    return create_database()


@app.route('/pesquisa', methods=['GET'])
def pesquisa_create():
    data = request.args['listaAvaliacao']
    result = store(data)
    if result:
        return '1'
    return '0'


# @app.route('/pesquisa/{id}', methods=['PUT'])
# def pesquisa_update():
#     return 'test'


# @app.route('/pesquisa_', methods=['GET'])
# def pesquisa_get():
#     return 'test'


# @app.route('/pesquisa/{id}', methods=['DELETE'])
# def pesquisa_delete():
#     return 'test'

if __name__ == '__main__':
    app.run(debug=True)