'''Модуль со схемами нагрузки'''


from pydantic import BaseModel
from schemes.discipline import DisciplineResponse
from schemes.group import GroupResponse
from schemes.teacher import TeacherResponse


class LoadCreate(BaseModel):
    '''Схема создания нагрузки'''
    teacher: int
    group: int
    discipline: int
    hours: int
    semester: int
    course: int


class LoadResponse(BaseModel):
    '''Схема тела ответа запросов на преподавателя'''
    id: int
    teacher: TeacherResponse
    group: GroupResponse
    discipline: DisciplineResponse
    hours: int
    semester: int
    course: int
