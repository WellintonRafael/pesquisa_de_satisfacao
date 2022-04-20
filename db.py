import psycopg2 as db
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:welL2801@localhost:5432/teste")

<<<<<<< HEAD
=======
# connection = db.connect(user="postgres", password="welL2801", host="localhost", port="5432", database="teste")
>>>>>>> github/main
connection = db.connect(user="qixgziaqwjfnxq", password="45db650b13d205b6b4cd198dfa8767748ddd28f65a2f2c7a62d9c77cebd505ee", host="ec2-54-158-26-89.compute-1.amazonaws.com", port="5432", database="d5k8f7g7cmuq2g")


def run_sql(sql):
    with connection.cursor() as curs:
        curs.execute(sql)
        connection.commit()


def create_database():
    sql = """
        CREATE TABLE tb_teste_3 \
        (id serial PRIMARY KEY, \
        data DATE, \
        nome VARCHAR (100), \
        num_apartamento INTEGER, \
        atendimento VARCHAR (20), \
        limpeza VARCHAR (20), \
        conforto VARCHAR (20), \
        cafe VARCHAR (20), \
        internet VARCHAR (20), \
        custo_beneficio VARCHAR (20), \
        localizacao VARCHAR (20), \
        sugestao TEXT)
    """
    try:
        run_sql(sql)
        return ("Criado com Sucesso")
    except Exception as e:
        return(f"Erro: {e}")


def drop_database():
    sql = """
        DROP TABLE tb_teste_3
    """
    run_sql(sql)
