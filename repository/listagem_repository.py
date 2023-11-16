from models.dao.project import PROJECT
from models.dao.mongo import db
from math import ceil


def listagem_repository(listagem_dto: dict, match):
    if listagem_dto['paginacao_limite'] == 0:
        return list(db.mqtt.find(
            match
        ))

    total = db.mqtt.count_documents(
        match
    )
    paginas = 1

    if listagem_dto['paginacao_limite'] != 0:
        paginas = ceil(total / listagem_dto['paginacao_limite'])

    paginacao = [
        {'$sort': {'criado_em': -1}},
        {'$skip': (listagem_dto['paginacao_pagina'] - 1) * listagem_dto['paginacao_limite']},
        {'$limit': listagem_dto['paginacao_limite']}
    ]

    response = db.mqtt.find(
        match,
        PROJECT
    )

    return {
        'total': total,
        'paginas': paginas,
        'pagina': listagem_dto['paginacao_pagina'],
        'limite': listagem_dto['paginacao_limite'],
        'itens': list(response)
    }
