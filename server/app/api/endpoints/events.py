from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.models.event import Event, EventCreate, get_event_by_id
from app.models.response import ResponseOk
from app.models.user import User, get_current_user
from app import db
from app.db.tables import events, event_participants

router = APIRouter()


@router.get("/", response_model=List[Event])
async def read_event():
    product_set = await db.fetch_all(query=events.select())
    return [Event(**p) for p in product_set]


@router.post("/", response_model=Event)
async def create_event(
    event: EventCreate,
    user: User = Depends(get_current_user),
):
    last_record_id = await db.execute(
        query=(
            events.insert()
            .values(
                title=event.title,
                description=event.description,
                event_date=event.event_date.replace(tzinfo=None),
                user_id=user.id,
            )
        )
    )
    event_from_db = await db.fetch_one(
        query=(
            events.select()
            .where(events.c.id == last_record_id)
        )
    )
    return Event(
        **event_from_db,
    )


@router.post("/{event_id}/subscribe", response_model=ResponseOk)
async def subscribe_to_event(
    event: Event = Depends(get_event_by_id),
    user: User = Depends(get_current_user),
):
    await db.execute(
        query=(
            event_participants.insert()
            .values(
                user_id=user.id,
                event_id=event.id,
            )
        )
    )
    return ResponseOk()


@router.post("/subscribed", response_model=List[Event])
async def user_subscribed_event(
    user: User = Depends(get_current_user),
):
    event_set = await db.fetch_all(
        query=(
            select([events]).select_from(
                events.join(event_participants)
            )
            .where(event_participants.c.user_id == user.id)
        )
    )
    return [Event(**e) for e in event_set]
