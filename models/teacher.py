'''Модуль с таблицей БД преподавателя'''


from peewee import CharField
from models.base import Table


class Teacher(Table):
    '''Преподаватель'''
    name = CharField()
