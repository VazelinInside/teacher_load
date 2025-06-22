'''Модуль перехода от модели БД к схеме запросов'''


from models.group import Group
from schemes.group import GroupCreate, GroupResponse


def get_or_create_group(group_create: GroupCreate) -> Group:
    '''Создает группу'''

    return Group.get_or_create(
        name=group_create.name
    )[0]


def get_group_response(group: Group) -> GroupResponse:
    '''Получение тела ответа запросов на группу'''

    return GroupResponse(
        id=group.id,
        name=group.name
    )


def get_by_id_group(group_id) -> Group:
    '''Получает группы по ее id'''

    return Group.get_by_id(group_id)


def put_name_group(group: Group, name: str) -> Group:
    '''Изменяет название группы'''

    group.name = name
    group.save()
    return group
