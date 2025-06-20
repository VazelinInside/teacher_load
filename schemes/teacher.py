from pydantic import BaseModel


class TeacherCreate(BaseModel):
    name: str


class TeacherResponse(BaseModel):
    id: int
    name: str
