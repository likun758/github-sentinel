from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.base import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, nullable=False)
    repo = Column(String, nullable=False)
    frequency = Column(String, default="daily")
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
