from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey, DateTime, func,
)

from .. import metadata

announcements = Table(
    "announcements",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("user_id", ForeignKey("users.id")),
    Column("created_date", DateTime, default=func.now()),
)
