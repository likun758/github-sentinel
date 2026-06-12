from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.base import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    repo_full_name = Column(String, nullable=False)
    period = Column(String, default="daily")
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
