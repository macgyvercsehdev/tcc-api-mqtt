from repository import listagem_repository


def listagem_service(listagem_dto: dict):
    """
    Recebe um dicionário `listagem_dto` como entrada e retorna uma lista de objetos.

    :param listagem_dto: Um dicionário contendo os dados necessários para a listagem.
    :type listagem_dto: dict

    :return: Uma lista de objetos representando a resposta do listagem_repository.
    :rtype: list
    """

    match = {}
    response = listagem_repository(
        listagem_dto,
        match
    )

    return response or []
