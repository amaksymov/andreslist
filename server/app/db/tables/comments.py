from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey, DateTime, func,
)

from .. import metadata

comments = Table(
    "comments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String),
    Column("user_id", ForeignKey("users.id")),
    Column("event_id", ForeignKey("events.id")),
    Column("created_date", DateTime, default=func.now()),
)
