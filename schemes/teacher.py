'''Модуль со схемами преподавателей'''


from pydantic import BaseModel


class TeacherCreate(BaseModel):
    '''Схема создания преподавателя'''
    name: str


class TeacherResponse(BaseModel):
    '''Схема тела ответа запросов на преподавателя'''
    id: int
    name: str
