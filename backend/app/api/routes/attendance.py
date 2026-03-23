from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.database.db import SessionLocal
from app.database.models import Attendance

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/mark")
def mark_attendance(
    student_id: int,
    status: str,
    attendance_date: date,
    db: Session = Depends(get_db)
):
    # 🔍 Check if already exists
    record = db.query(Attendance).filter(
        Attendance.student_id == student_id,
        Attendance.date == attendance_date
    ).first()

    if record:
        # ✅ UPDATE existing record
        record.status = status
    else:
        # ✅ CREATE new record
        record = Attendance(
            student_id=student_id,
            status=status,
            date=attendance_date
        )
        db.add(record)

    db.commit()

    return {"message": "Attendance updated successfully"}

@router.get("/absent")
def get_absent_students(attendance_date: date, db: Session = Depends(get_db)):
    return db.query(Attendance).filter(
        Attendance.date == attendance_date,
        Attendance.status == "ABSENT"
    ).all()



@router.get("/all")
def get_all_attendance(attendance_date: str, db: Session = Depends(get_db)):
    records = db.query(Attendance).filter(
        Attendance.date == attendance_date
    ).all()

    return [
        {
            "student_id": r.student_id,
            "status": r.status
        }
        for r in records
    ]