from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    TIMESTAMP,
    ForeignKey,
)
from sqlalchemy.sql import func
from datetime import datetime
from app.database.db import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    roll_no = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    parent_name = Column(String)
    parent_phone = Column(String(15), nullable=False)
    department = Column(String(50))
    year = Column(Integer)
    section = Column(String(10))
    call_logs = relationship("CallLog", back_populates="student")
    created_at = Column(TIMESTAMP, server_default=func.now())
    attendance = relationship("Attendance", back_populates="student")


from sqlalchemy import Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)  # PRESENT / ABSENT
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    student = relationship("Student")
    status = Column(String)


from sqlalchemy import Text

class CallLog(Base):
    __tablename__ = "call_logs"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    call_sid = Column(String, unique=True)

    recording_url = Column(String, nullable=True)
    transcript_text = Column(Text, nullable=True)
    excuse_category = Column(String, nullable=True)
    risk_level = Column(String, nullable=True)

    call_status = Column(String)      # COMPLETED / NO_ANSWER / FAILED
    call_duration = Column(Integer)   # seconds
    call_date = Column(Date)

    risk_level = Column(String, nullable=True)
    risk_score = Column(Integer, nullable=True)

    student = relationship("Student", back_populates="call_logs")



    created_at = Column(DateTime, default=datetime.utcnow)





class BulkCampaign(Base):
    __tablename__ = "bulk_campaigns"

    id = Column(Integer, primary_key=True, index=True)
    campaign_name = Column(String)
    message = Column(String)
    total_calls = Column(Integer)
    success_calls = Column(Integer, default=0)
    failed_calls = Column(Integer, default=0)
    status = Column(String, default="IN_PROGRESS")  # IN_PROGRESS / COMPLETED
    created_at = Column(DateTime, default=datetime.utcnow)