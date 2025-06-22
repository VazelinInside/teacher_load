'''Модуль апи нагрузки преподавателя'''


from fastapi import FastAPI
from api.teacher import router as teachers_router


app = FastAPI()


app.include_router(teachers_router)
