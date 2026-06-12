from app.db.session import SessionLocal
from app.services.sentinel_service import SentinelService


def run_github_sentinel_job():
    db = SessionLocal()
    try:
        SentinelService(db).run_once()
    finally:
        db.close()
