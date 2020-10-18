from datetime import datetime

from pydantic import BaseModel


class AdResponse(BaseModel):
    id: int
    description: str
    created_date: datetime
    user_id: int
    announcement_id: int


class AdResponseIn(BaseModel):
    description: str
    announcement_id: int
