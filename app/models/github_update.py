from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from app.db.base import Base


class GitHubUpdate(Base):
    __tablename__ = "github_updates"

    id = Column(Integer, primary_key=True, index=True)
    repo_full_name = Column(String, nullable=False)
    update_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    author = Column(String, nullable=True)
    summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
