from schemes.teacher import TeacherCreate, TeacherResponse
from models.teacher import Teacher
from fastapi import APIRouter, status


router = APIRouter(prefix="/teachers", tags=["teachers"])


@router.post('/', response_model=TeacherResponse,
             status_code=status.HTTP_201_CREATED)
async def create_teacher(teacher_data: TeacherCreate):
    '''Создание нового преподавателя'''
    teacher = Teacher.create(name=teacher_data.name)

    data = TeacherResponse(
        id=teacher.id,
        name=teacher.name
    )

    return data
