from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.models import CallLog


def check_and_flag_student(db: Session, student_id: int, excuse_category: str):

    seven_days_ago = date.today() - timedelta(days=7)

    # Total absences in last 7 days
    recent_count = db.query(func.count(CallLog.id)).filter(
        CallLog.student_id == student_id,
        CallLog.call_date >= seven_days_ago
    ).scalar()

    # Same category repetition in last 7 days
    same_category_count = db.query(func.count(CallLog.id)).filter(
        CallLog.student_id == student_id,
        CallLog.excuse_category == excuse_category,
        CallLog.call_date >= seven_days_ago
    ).scalar()

    # 🚩 HIGH RISK CONDITIONS
    if recent_count >= 3:
        return "HIGH"

    if same_category_count >= 2:
        return "HIGH"

    if excuse_category in ["Medical Emergency", "Hospitalized"] and same_category_count >= 2:
        return "HIGH"

    # ⚠️ MEDIUM RISK CONDITIONS
    if recent_count == 2:
        return "MEDIUM"

    if excuse_category in ["Personal Work", "Travel"]:
        return "MEDIUM"

    # ✅ Default LOW
    return "LOW"
