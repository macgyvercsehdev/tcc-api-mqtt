from models.dto.listagem_dto import ListagemDTO
from fastapi import status, Depends, Request
from service import listagem_service
from .router import router


@router.get('', status_code=status.HTTP_200_OK)
def listagem_controller(
    listagem_dto: ListagemDTO = Depends(),
):

    return listagem_service(
        listagem_dto.__dict__,
    )
