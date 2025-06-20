'''Модуль содержащий базу данных о нагрузке преподавателей'''
from peewee import SqliteDatabase

db_load = SqliteDatabase('load.db')


if __name__ == '__main__':
    import discipline
    import group
    import load
    import teacher

    db_load.connect()
    db_load.create_tables([
        teacher.Teacher,
        group.Group,
        discipline.Discipline,
        load.Load
    ], safe=True)
    db_load.close()
