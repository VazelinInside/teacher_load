'''Модуль апи нагрузки преподавателя'''


from fastapi import FastAPI
from models import Teacher

app = FastAPI()


@app.post('/add_teacher/')
def add_teacher(name):
    '''Добавление преподавателя'''
    Teacher.create(name=name)
    return {'message': 'Преподаватель добавлен'}
