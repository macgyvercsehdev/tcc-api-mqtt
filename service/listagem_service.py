from repository import listagem_repository


def listagem_service(listagem_dto: dict):

    match = {}

    response = listagem_repository(
        listagem_dto,
        match
    )

    return response or []
