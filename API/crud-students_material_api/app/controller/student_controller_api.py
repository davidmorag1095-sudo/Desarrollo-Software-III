from fastapi import APIRouter
from starlette import status

from app.schemas.student_schema import StudentSchema
from app.service.student_service import StudentService

router = APIRouter(prefix = "/student", tags = ["Student"])
service = StudentService()

@router.post("/", response_model=StudentSchema)
def create_student(student: StudentSchema):
    return service.create_student(student.carnet, student.name, student.age)