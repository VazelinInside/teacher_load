'''Модуль таблицы БД групп'''


from peewee import CharField
from models.base import Table


class Group(Table):
    '''Группа'''
    name = CharField()
