from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey, DateTime, func,
    PrimaryKeyConstraint,
)

from .. import metadata

events = Table(
    "events",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("user_id", ForeignKey("users.id")),
    Column("created_date", DateTime, default=func.now()),
    Column("event_date", DateTime, default=func.now()),
)


event_participants = Table(
    "events_to_users",
    metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("event_id", ForeignKey("events.id")),
    PrimaryKeyConstraint("user_id", "event_id", name='events_to_users_pk'),
)
