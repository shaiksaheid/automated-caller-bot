from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.models import Student

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_student(student: dict, db: Session = Depends(get_db)):
    new_student = Student(
        roll_no=student["roll_no"],
        name=student["name"],
        parent_phone=student["parent_phone"],
        department=student.get("department"),
        year=student.get("year"),
        section=student.get("section")
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student added", "id": new_student.id}

@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
