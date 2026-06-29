from fastapi import APIRouter, HTTPException
from sqlalchemy.testing.provision import update_db_opts
from starlette import status

from app.schemas.student_schema import StudentSchema
from app.service.student_service import StudentService

router = APIRouter(prefix = "/student", tags = ["Student"])
service = StudentService()

@router.post("/", response_model=StudentSchema)
def create_student(student: StudentSchema):
    return service.create_student(student.carnet, student.name, student.age)

@router.get("/{carnet}", response_model=StudentSchema)
def get_student(carnet: str):
    student = service.get_student(carnet)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/", response_model=list[StudentSchema])
def list_students():
    return service.list_students()

@router.put("/{carnet}", response_model=StudentSchema)
def update_student(carnet: str, student: StudentSchema):
    updated = service.update_student(carnet, student.name, student.age)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/{carnet}")
def delete_student(carnet: str):
    deleted = service.delete_student(carnet)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"Message:" "Student deleted"}
