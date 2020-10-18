from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app import db
from app.db.tables import events


class Event(BaseModel):
    id: int
    title: str
    description: str
    event_date: datetime
    created_date: datetime
    user_id: int


class EventCreate(BaseModel):
    title: str
    description: str
    event_date: datetime


class EventUpdate(EventCreate):
    event_date: Optional[datetime] = None


async def get_event_by_id(event_id: int) -> Optional[Event]:
    if event := await db.fetch_one(
        query=(
            events.select()
            .where(
                events.c.id == event_id
            )
        )
    ):
        return Event(**event)
