from peewee import IntegerField, ForeignKeyField
from models.base import Table
from models.discipline import Discipline
from models.group import Group
from models.teacher import Teacher


class Load(Table):
    '''Нагрузка преподавателя'''
    teacher = ForeignKeyField(Teacher)
    group = ForeignKeyField(Group)
    discipline = ForeignKeyField(Discipline)
    hours = IntegerField()
    semester = IntegerField()
    course = IntegerField()
