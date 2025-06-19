'''Модуль содержащий базу данных о нагрузке преподавателей'''
from peewee import (SqliteDatabase, Model, ForeignKeyField, CharField,
                    IntegerField)


db_load = SqliteDatabase('load.db')


class BaseModel(Model):
    '''Класс базовой модели'''
    class Meta:
        '''Общий класс Мета'''
        database = db_load


class Teacher(BaseModel):
    '''Преподаватель'''
    name = CharField()


class Group(BaseModel):
    '''Группа'''
    name = CharField()


class Discipline(BaseModel):
    '''Дисциплина'''
    name = CharField()


class LoadTeacher(BaseModel):
    '''Нагрузка преподавателя'''
    teacher = ForeignKeyField(Teacher)
    group = ForeignKeyField(Group)
    discipline = ForeignKeyField(Discipline)
    hours = IntegerField()
    semester = IntegerField()
    course = IntegerField()


if __name__ == '__main__':
    db_load.connect()
    db_load.create_tables([Teacher, Group, Discipline, LoadTeacher], safe=True)
    db_load.close()
