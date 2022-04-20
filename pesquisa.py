from db import run_sql


def store(data):
    values = data.split(',')

    sql = "INSERT INTO tb_teste_3 (atendimento, limpeza, conforto, cafe, \
        internet, custo_beneficio, localizacao) \
        VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
            values[5],
            values[6]
        )

    try:
        run_sql(sql)
        return True
    except Exception as e:
        print(e)
    return None
