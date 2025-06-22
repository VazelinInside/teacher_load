'''Модуль со схемами группы'''


from pydantic import BaseModel


class GroupCreate(BaseModel):
    '''Схема создания группы'''
    name: str


class GroupResponse(BaseModel):
    '''Схема тела ответа запросов на группу'''
    id: int
    name: str
