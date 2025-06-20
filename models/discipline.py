from peewee import CharField
from models.base import Table


class Discipline(Table):
    '''Дисциплина'''
    name = CharField()
