'''Модуль перехода от модели БД к схеме запросов'''


from models.load import Load
from ms_controller.discipline import (get_by_id_discipline, get_discipline_response)
from ms_controller.group import (get_by_id_group, get_group_response)
from ms_controller.teacher import (get_by_id_teacher, get_teacher_response)
from schemes.load import LoadCreate, LoadResponse


def get_or_create_load(load_create: LoadCreate) -> Load:
    '''Создает нагрузку'''

    return Load.get_or_create(
        teacher=load_create.teacher,
        group=load_create.group,
        discipline=load_create.discipline,
        hours=load_create.hours,
        semester=load_create.semester,
        course=load_create.course
    )[0]


def get_load_response(load: Load) -> LoadResponse:
    '''Получение тела ответа запросов на преподавателя'''

    return LoadResponse(
        id=load.id,
        teacher=get_teacher_response(
            teacher=get_by_id_teacher(
                teacher_id=load.teacher
            )
        ),
        group=get_group_response(
            group=get_by_id_group(
                group_id=load.group
            )
        ),
        discipline=get_discipline_response(
            discipline=get_by_id_discipline(
                discipline_id=load.discipline
            )
        ),
        hours=load.hours,
        semester=load.semester,
        course=load.course
    )


def get_by_id_load(load_id: int) -> Load:
    '''Получает преподавателя по его id'''

    return Load.get_by_id(load_id)


def put_table_load(load: Load, load_create: LoadCreate) -> Load:
    '''Создает нагрузку'''

    load.teacher=load_create.teacher
    load.group=load_create.group
    load.discipline=load_create.discipline
    load.hours=load_create.hours
    load.semester=load_create.semester
    load.course=load_create.course

    load.save()

    return load
