PROJECT = {
    '_id': 0,
    'id': {'$toString': '$_id'},
    'id_equipamento': 1,
    'temperatura': 1,
    'umidade': 1,
    'data': {'$dateToString': {'format': '%Y-%m-%dT%H:%M:%S', 'date': '$data'}},
    'dia_da_semana': 1,
    'consumo_diario': 1,
    'tarifa': 1,
    'vazao_litro_acumulada':1,
    'umidade': 1
}
# O project serve para definir as colunas que o mongo vai retornar na resposta