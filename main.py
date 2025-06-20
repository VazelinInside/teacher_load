'''Модуль апи нагрузки преподавателя'''


from fastapi import FastAPI
from ms_controller.teacher import router as teachers_router


app = FastAPI()


app.include_router(teachers_router)


# @app.post('/teacher/')
# def add_teacher(name):
#     '''Добавление преподавателя'''
#     m.Teacher.create(name=name)
#     return Teacher


# @app.post('/group/')
# def add_group(name):
#     '''Добавление группы'''
#     m.Group.create(name=name)
#     return {
#         'id': m.Group.get(name=name).id,
#         'name': m.Group.get(name=name).name
#     }


# @app.post('/discipline/')
# def add_discipline(name):
#     '''Добавление дисциплины'''
#     m.Discipline.create(name=name)
#     return {
#         'id': m.Discipline.get(name=name).id,
#         'name': m.Discipline.get(name=name).name
#     }


# @app.get('/teacher_info/{item_id}')
# def get_teacher(item_id):
#     '''Получение информации о преподавателе'''
#     data = m.Teacher.get_by_id(item_id).name
#     data = data.split(' ')
#     return {
#         'Фамилия': data[0],
#         'Имя': data[1],
#         'Отчество': data[2]
#     }


# @app.get('/group_info/{item_id}')
# def get_group(item_id):
#     '''Получение номеклатуры группы'''
#     data = m.Group.get_by_id(item_id).name
#     return {
#         'Группа': data
#     }


# @app.get('/discipline_info/{item_id}')
# def get_discipline(item_id):
#     '''Получение названия дисциплины'''
#     data = m.Discipline.get_by_id(item_id).name
#     return {
#         'Дисциплина': data
#     }
