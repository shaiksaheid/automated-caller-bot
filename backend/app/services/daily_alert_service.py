from datetime import date
from sqlalchemy import func
from app.database.models import CallLog
from app.services.twilio_service import send_sms


ALERT_THRESHOLD = 70  # You can change this


def check_daily_risk_and_alert(db, admin_phone=None):

    today = date.today()

    avg_risk = db.query(
        func.avg(CallLog.risk_score)
    ).filter(
        CallLog.call_date == today,
        CallLog.risk_score.isnot(None)
    ).scalar()

    if not avg_risk:
        return {"status": "no data today"}

    avg_risk = float(avg_risk)

    if avg_risk >= ALERT_THRESHOLD:

        message = (
            f"ALERT: High average student risk today. "
            f"Average Risk Score: {round(avg_risk,2)}"
        )

        if admin_phone:
            send_sms(admin_phone, message)

        return {
            "status": "alert_triggered",
            "average_risk": round(avg_risk, 2)
        }

    return {
        "status": "safe",
        "average_risk": round(avg_risk, 2)
    }