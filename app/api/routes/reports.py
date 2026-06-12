from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.report_service import ReportService
from app.services.sentinel_service import SentinelService

router = APIRouter()


@router.get("/")
def list_reports(db: Session = Depends(get_db)):
    return ReportService(db).list_reports()


@router.post("/run")
def run_sentinel_once(db: Session = Depends(get_db)):
    return SentinelService(db).run_once()
