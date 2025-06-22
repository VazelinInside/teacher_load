'''Модуль endpoint-ов с таблицей дисциплины'''


from fastapi import APIRouter, status
from schemes.discipline import DisciplineCreate, DisciplineResponse
from ms_controller.discipline import (get_or_create_discipline,
                                      get_discipline_response,
                                      get_by_id_discipline,
                                      put_name_discipline)


router = APIRouter(prefix="/disciplines", tags=["disciplines"])


@router.post('/', response_model=DisciplineResponse,
             status_code=status.HTTP_201_CREATED)
async def create_discipline(discipline_data: DisciplineCreate):
    '''endpoint создание нового преподавателя'''

    return get_discipline_response(
        discipline=get_or_create_discipline(
            discipline_create=discipline_data
        )
    )


@router.get('/{discipline_id}', response_model=DisciplineResponse,
            status_code=status.HTTP_200_OK)
async def get_discipline(discipline_id):
    '''endpoint получение дисциплины по id'''

    return get_discipline_response(
        discipline=get_by_id_discipline(
            discipline_id=discipline_id
        )
    )


@router.put('/{discipline_id}', response_model=DisciplineResponse,
            status_code=status.HTTP_200_OK)
async def put_discipline(discipline_id, name):
    '''endpoint изменения названия группы по id'''

    return get_discipline_response(
        discipline=put_name_discipline(
            discipline=get_by_id_discipline(
                discipline_id=discipline_id
            ),
            name=name
        )
    )
