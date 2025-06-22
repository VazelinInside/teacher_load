'''Модуль endpoint-ов с таблицей группы'''


from fastapi import APIRouter, status
from schemes.group import GroupCreate, GroupResponse
from ms_controller.group import (get_or_create_group, get_group_response,
                                 get_by_id_group, put_name_group)


router = APIRouter(prefix="/groups", tags=["groups"])


@router.post('/', response_model=GroupResponse,
             status_code=status.HTTP_201_CREATED)
async def create_group(group_data: GroupCreate):
    '''endpoint создание новой группы'''

    return get_group_response(
        group=get_or_create_group(
            group_create=group_data
        )
    )


@router.get('/{group_id}', response_model=GroupResponse,
            status_code=status.HTTP_200_OK)
async def get_group(group_id):
    '''endpoint получения группы по id'''

    return get_group_response(
        group=get_by_id_group(
            group_id=group_id
        )
    )


@router.put('/{group_id}', response_model=GroupResponse,
            status_code=status.HTTP_200_OK)
async def put_group(group_id, name):
    '''endpoint изменения названия группы по id'''

    return get_group_response(
        group=put_name_group(
            group=get_by_id_group(
                group_id=group_id
            ),
            name=name
        )
    )
