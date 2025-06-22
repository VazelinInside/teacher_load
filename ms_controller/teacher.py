'''Модуль перехода от модели БД к схеме запросов'''


from models.teacher import Teacher
from schemes.teacher import TeacherCreate, TeacherResponse


def get_or_create_teacher(teacher_create: TeacherCreate) -> Teacher:
    '''Создает преподавателя'''

    return Teacher.get_or_create(
        name=teacher_create.name
    )[0]


def get_teacher_response(teacher: Teacher) -> TeacherResponse:
    '''Получение тела ответа запросов на преподавателя'''

    return TeacherResponse(
        id=teacher.id,
        name=teacher.name
    )


def get_by_id_teacher(teacher_id: int) -> Teacher:
    '''Получает преподавателя по его id'''

    return Teacher.get_by_id(teacher_id)


def put_name_teacher(teacher: Teacher, name: str) -> Teacher:
    '''Изменяет имя преподавателя'''

    teacher.name = name
    teacher.save()
    return teacher
