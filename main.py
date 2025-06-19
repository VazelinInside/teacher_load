'''Модуль апи нагрузки преподавателя'''


from fastapi import FastAPI
from models import Teacher

app = FastAPI()


@app.post('/teacher/')
def add_teacher(name):
    '''Добавление преподавателя'''
    Teacher.create(name=name)
    return {
        'id': Teacher.get(name=name).id,
        'name': Teacher.get(name=name).name
    }
