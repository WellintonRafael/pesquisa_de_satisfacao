from flask import Flask, render_template, url_for
import psycopg2 as db
from sqlalchemy import create_engine

app = Flask("pesquisa_de_satisfacao")

# engine = create_engine("postgresql://postgres:welL2801@localhost:5432/teste")

# connetion = db.connect(user="postgres", password="welL2801", host="localhost", port="5432", database="teste")
#
# curs = connetion.cursor()
# sql = """CREATE TABLE tb_teste_2 \
#       (id serial PRIMARY KEY, \
#       data DATE, nome VARCHAR (100), \
#       num_apartamento INTEGER, \
#       atendimento VARCHAR (20), \
#       limpeza VARCHAR (20), \
#       conforto VARCHAR (20), \
#       cafe VARCHAR (20), \
#       internet VARCHAR (20), \
#       custo_beneficio VARCHAR (20), \
#       localizacao VARCHAR (20), \
#       sugestao TEXT)"""
#
# curs.execute(sql)
# connetion.commit()


@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
