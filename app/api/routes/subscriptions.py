from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.subscription import SubscriptionCreate
from app.services.subscription_service import SubscriptionService

router = APIRouter()


@router.post("/")
def create_subscription(
    payload: SubscriptionCreate,
    db: Session = Depends(get_db),
):
    return SubscriptionService(db).create(payload)


@router.get("/")
def list_subscriptions(db: Session = Depends(get_db)):
    return SubscriptionService(db).list_all()
