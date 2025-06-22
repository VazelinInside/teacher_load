'''Модуль со схемами дисциплины'''


from pydantic import BaseModel


class DisciplineCreate(BaseModel):
    '''Схема создания дисциплины'''
    name: str


class DisciplineResponse(BaseModel):
    '''Схема тела ответа запросов на дисциплину'''
    id: int
    name: str
