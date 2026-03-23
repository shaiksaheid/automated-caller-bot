from datetime import date, timedelta
from app.database.models import CallLog


def check_and_flag_student(db, student_id: int, excuse_category: str):

    today = date.today()
    last_7_days = today - timedelta(days=7)

    # Get last 7 days records
    recent_logs = db.query(CallLog).filter(
        CallLog.student_id == student_id,
        CallLog.call_date >= last_7_days
    ).all()

    total_recent = len(recent_logs)

    # Count category frequency
    category_counts = {}

    for log in recent_logs:
        cat = log.excuse_category or "Uncategorized"
        category_counts[cat] = category_counts.get(cat, 0) + 1

    # 🚩 HIGH RISK CONDITIONS
    if total_recent >= 3:
        return "HIGH"

    if category_counts.get("Other / Unclear Reason", 0) >= 2:
        return "HIGH"

    if category_counts.get("Hospitalized / Medical Emergency", 0) >= 3:
        return "HIGH"

    # ⚠ MEDIUM RISK CONDITIONS
    if total_recent == 2:
        return "MEDIUM"

    if category_counts.get(excuse_category, 0) >= 2:
        return "MEDIUM"

    # ✅ LOW RISK
    return "LOW"
