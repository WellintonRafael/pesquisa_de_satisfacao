from datetime import datetime
from db import run_sql


def mostra_data() -> str:
    data_atual = datetime.now()
    data_formatada: str = data_atual.strftime('%Y-%m-%d')
    return str(data_formatada)

def store(data):
    values = data.split(',')

    sql = "INSERT INTO tb_teste_3 (data, nome, num_apartamento, atendimento, limpeza, conforto, cafe, \
        internet, custo_beneficio, localizacao, sugestao) \
        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(


            mostra_data(),
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
            values[5],
            values[6],
            values[7],
            values[8],
            values[9]

    )

    try:
        run_sql(sql)
        return True
    except Exception as e:
        print(e)
    return None
