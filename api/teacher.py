'''Модуль endpoint-ов с таблицей Учителя'''


from fastapi import APIRouter, status
from schemes.teacher import TeacherCreate, TeacherResponse
from ms_controller.teacher import (get_or_create_teacher, get_teacher_response,
                                   get_by_id_teacher, put_name_teacher)


router = APIRouter(prefix="/teachers", tags=["teachers"])


@router.post('/', response_model=TeacherResponse,
             status_code=status.HTTP_201_CREATED)
async def create_teacher(teacher_data: TeacherCreate):
    '''endpoint создание нового преподавателя'''

    return get_teacher_response(
        teacher=get_or_create_teacher(
            teacher_create=teacher_data
        )
    )


@router.get('/{teacher_id}', response_model=TeacherResponse,
            status_code=status.HTTP_200_OK)
async def get_teacher(teacher_id):
    '''endpoint получения преподавателя по id'''

    return get_teacher_response(
        teacher=get_by_id_teacher(
            teacher_id=teacher_id
        )
    )


@router.put('/{teacher_id}', response_model=TeacherResponse,
            status_code=status.HTTP_200_OK)
async def put_teacher(teacher_id, name):
    '''endpoint изменения имени преподавателя по id'''

    return get_teacher_response(
        teacher=put_name_teacher(
            teacher=get_by_id_teacher(
                teacher_id=teacher_id
            ),
            name=name
        )
    )
