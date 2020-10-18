import datetime

import pytest

from databases import Database
from app import crud
from app.models.event import EventCreate, EventUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


@pytest.mark.asyncio
async def test_create_item(db_con: Database):
    title = random_lower_string()
    description = random_lower_string()
    event_in = EventCreate(
        title=title,
        description=description,
        event_date=datetime.datetime.now() + datetime.timedelta(days=15)
    )
    user = await create_random_user()
    event = await crud.event.create_with_owner(obj_in=event_in, owner_id=user.id)
    assert event.title == title
    assert event.description == description
    assert event.user_id == user.id


@pytest.mark.asyncio
async def test_get_item(db_con: Database):
    title = random_lower_string()
    description = random_lower_string()
    event_in = EventCreate(
        title=title,
        description=description,
        event_date=datetime.datetime.now() + datetime.timedelta(days=15)
    )
    user = await create_random_user()
    event = await crud.event.create_with_owner(obj_in=event_in, owner_id=user.id)
    stored_event = await crud.event.get(_id=event.id)
    assert stored_event
    assert event.title == stored_event.title
    assert event.description == stored_event.description
    assert event.user_id == stored_event.user_id


@pytest.mark.asyncio
async def test_update_item(db_con: Database):
    title = random_lower_string()
    description = random_lower_string()
    event_in = EventCreate(
        title=title,
        description=description,
        event_date=datetime.datetime.now() + datetime.timedelta(days=15)
    )
    user = await create_random_user()
    event = await crud.event.create_with_owner(obj_in=event_in, owner_id=user.id)
    description2 = random_lower_string()
    title2 = random_lower_string()
    event_update = EventUpdate(title=title2, description=description2)
    await crud.event.update(db_obj=event, obj_in=event_update)
    event2 = await crud.event.get(_id=event.id)
    assert event.id == event2.id
    assert event.user_id == event2.user_id
    assert event2.title == title2
    assert event2.description == description2


@pytest.mark.asyncio
async def test_delete_item(db_con: Database):
    title = random_lower_string()
    description = random_lower_string()
    event_in = EventCreate(
        title=title,
        description=description,
        event_date=datetime.datetime.now() + datetime.timedelta(days=15)
    )
    user = await create_random_user()
    event = await crud.event.create_with_owner(obj_in=event_in, owner_id=user.id)
    await crud.event.delete(_id=event.id)
    event2 = await crud.event.get(event.id)
    assert event2 is None
