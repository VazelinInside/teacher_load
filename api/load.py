'''Модуль endpoint-ов с таблицей нагрузки'''


from fastapi import APIRouter, status
from schemes.load import LoadCreate, LoadResponse
from ms_controller.load import (get_or_create_load, get_load_response,
                                get_by_id_load, put_table_load)


router = APIRouter(prefix="/loads", tags=["loads"])


@router.post('/', response_model=LoadResponse,
             status_code=status.HTTP_201_CREATED)
async def create_load(load_data: LoadCreate):
    '''endpoint создание нового преподавателя'''

    return get_load_response(
        load=get_or_create_load(
            load_create=load_data
        )
    )


@router.get('/{load_id}', response_model=LoadResponse,
            status_code=status.HTTP_200_OK)
async def get_load(load_id):
    '''endpoint получения преподавателя по id'''

    return get_load_response(
        load=get_by_id_load(
            load_id=load_id
        )
    )


@router.put('/{load_id}', response_model=LoadResponse,
            status_code=status.HTTP_200_OK)
async def put_load(load_id: int, load_data: LoadCreate):
    '''endpoint изменения имени преподавателя по id'''

    return get_load_response(
        load=put_table_load(
            load=get_by_id_load(
                load_id=load_id
            ),
            load_create=load_data
        )
    )
