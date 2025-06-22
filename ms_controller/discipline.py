'''Модуль перехода от модели БД к схеме запросов'''


from models.discipline import Discipline
from schemes.discipline import DisciplineCreate, DisciplineResponse


def get_or_create_discipline(discipline_create: DisciplineCreate) -> Discipline:
    '''Создает дисциплину'''

    return Discipline.get_or_create(
        name=discipline_create.name
    )[0]


def get_discipline_response(discipline: Discipline) -> DisciplineResponse:
    '''Получение тела ответа запросов на дисциплину'''

    return DisciplineResponse(
        id=discipline.id,
        name=discipline.name
    )


def get_by_id_discipline(discipline_id) -> Discipline:
    '''Получает дисциплины по ее id'''

    return Discipline.get_by_id(discipline_id)


def put_name_discipline(discipline: Discipline, name: str) -> Discipline:
    '''Изменяет название дисциплины'''

    discipline.name = name
    discipline.save()
    return discipline
