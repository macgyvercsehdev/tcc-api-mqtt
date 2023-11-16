PROJECT = {
    '_id': 0,
    'id': {'$toString': '$_id'},
    'planos_ids': [{
        '$map': {
            'input': '$planos_ids', 
            'as': 'planos_ids', 
            'in': {
                '$toString': '$$planos_ids'
            }
        }
    }],
    'codigo': 1,
    'porcentagem': 1,
    'situacao': 1,
    'limite_de_usos': 1,
    'quantidade_de_usos': 1,
    'vencimento': 1,
}
