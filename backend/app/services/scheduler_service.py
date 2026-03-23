from apscheduler.schedulers.background import BackgroundScheduler
from app.database.db import SessionLocal
from app.services.daily_alert_service import check_daily_risk_and_alert
from app.services.report_service import generate_daily_report
from app.services.email_service import send_email_with_attachment

from datetime import date
import os


def daily_risk_job():

    db = SessionLocal()

    try:
        # 1️⃣ Risk SMS Alert
        admin_phone = "+918885882321"
        result = check_daily_risk_and_alert(db, admin_phone)
        print("Daily Risk Check Result:", result)

        # 2️⃣ Generate Daily PDF Report
        today = date.today()
        filepath = generate_daily_report(db, today)

        # 3️⃣ Email PDF to Admin
        send_email_with_attachment(
            subject="CMRTC Daily Absentee Call Report",
            body="Please find attached today's absentee call report.",
            to_email=os.getenv("ADMIN_EMAIL"),
            file_path=filepath
        )

        print("Daily report generated & emailed successfully.")

    except Exception as e:
        print("Scheduler Error:", str(e))

    finally:
        db.close()


def start_scheduler():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        daily_risk_job,
        trigger="cron",
        hour=18,
        minute=0
    )

    scheduler.start()