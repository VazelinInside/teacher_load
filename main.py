'''Модуль апи нагрузки преподавателя'''


from fastapi import FastAPI
from api.group import router as groups_router
from api.discipline import router as disciplines_router
from api.load import router as loads_router
from api.teacher import router as teachers_router


app = FastAPI()


app.include_router(disciplines_router)
app.include_router(groups_router)
app.include_router(teachers_router)
app.include_router(loads_router)
