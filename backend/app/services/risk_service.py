from app.database.models import CallLog
from sqlalchemy.orm import Session

def calculate_risk(student_id: int, category: str, db: Session):
    
    # 🔹 Base scores
    base_scores = {
        "Medical": 3,
        "Fever": 2,
        "Family Function": 1,
        "Out of Station / Travel": 2,
        "Personal Work": 2,
        "No Response": 3,
        "Other": 1
    }

    score = base_scores.get(category, 1)

    # 🔹 Count previous same category
    previous_count = (
        db.query(CallLog)
        .filter(
            CallLog.student_id == student_id,
            CallLog.excuse_category == category
        )
        .count()
    )

    # 🔹 Repetition bonus
    if previous_count == 2:
        score += 1
    elif previous_count == 3:
        score += 2
    elif previous_count >= 4:
        score += 3

    # 🔹 Convert to risk level
    if score <= 2:
        return "LOW"
    elif score <= 4:
        return "MEDIUM"
    else:
        return "HIGH"
