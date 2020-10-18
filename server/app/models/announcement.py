from datetime import datetime

from pydantic import BaseModel


class Announcement(BaseModel):
    id: int
    title: str
    description: str
    created_date: datetime
    user_id: int


class AnnouncementIn(BaseModel):
    title: str
    description: str
