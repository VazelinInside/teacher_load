from peewee import Model
import models.connect


class Table(Model):
    '''Класс базовой модели'''
    class Meta:
        '''Общий класс Мета'''
        database = models.connect.db_load
