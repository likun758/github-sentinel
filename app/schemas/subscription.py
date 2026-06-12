from pydantic import BaseModel


class SubscriptionCreate(BaseModel):
    owner: str
    repo: str
    frequency: str = "daily"


class SubscriptionResponse(BaseModel):
    id: int
    owner: str
    repo: str
    frequency: str
    enabled: bool

    class Config:
        from_attributes = True
