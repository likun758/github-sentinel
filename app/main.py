from fastapi import FastAPI
from app.api.router import api_router
from app.db.base import Base
from app.db.session import engine
from app.jobs.scheduler import start_scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GitHub Sentinel",
    description="AI Agent for tracking GitHub repository updates",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api")


@app.on_event("startup")
def startup_event():
    start_scheduler()


@app.get("/")
def root():
    return {
        "name": "GitHub Sentinel",
        "status": "running",
    }
