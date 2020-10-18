from sqlalchemy import (
    Table, Column, DateTime,
    Integer, String, Boolean,
    ForeignKey, func
)

from .. import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("first_name", String),
    Column("last_name", String),
    Column("email", String),
    Column("password_hash", String),
    Column("disabled", Boolean, default=True),
    Column("created_date", DateTime, default=func.now()),
    Column("updated_date", DateTime, default=func.now(),
           onupdate=func.now()),
)
