from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey, DateTime, func,
)

from .. import metadata

responses = Table(
    "responses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column("user_id", ForeignKey("users.id")),
    Column("announcement_id", ForeignKey("announcements.id")),
    Column("created_date", DateTime, default=func.now()),
)
