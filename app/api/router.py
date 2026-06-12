from fastapi import APIRouter
from app.api.routes import health, subscriptions, reports

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"])
