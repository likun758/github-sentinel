from sqlalchemy.orm import Session
from app.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate


class SubscriptionService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payload: SubscriptionCreate):
        sub = Subscription(
            owner=payload.owner,
            repo=payload.repo,
            frequency=payload.frequency,
        )
        self.db.add(sub)
        self.db.commit()
        self.db.refresh(sub)
        return sub

    def list_all(self):
        return self.db.query(Subscription).all()

    def list_enabled(self):
        return self.db.query(Subscription).filter(Subscription.enabled == True).all()
