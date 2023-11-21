from repository import listagem_repository
from datetime import datetime

def listagem_service(listagem_dto: dict):
    """
    Recebe um dicionário `listagem_dto` como entrada e retorna uma lista de objetos.

    :param listagem_dto: Um dicionário contendo os dados necessários para a listagem.
    :type listagem_dto: dict

    :return: Uma lista de objetos representando a resposta do listagem_repository.
    :rtype: list
    """
    match = {}
    hoje = None

    if listagem_dto['data']:
        hoje = datetime.strptime(listagem_dto['data'], '%Y-%m-%d')
        hoje = datetime(hoje.year, hoje.month, hoje.day, 0, 0, 0)
        match.update(
            {
                'data': {
                    '$gte': hoje,
                    '$lt': datetime(hoje.year, hoje.month, hoje.day, 23, 59, 59)
                }
            }
        )

    response = listagem_repository(
        listagem_dto,
        match
    )

    return response
