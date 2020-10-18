import pytest

from app.db import db


@pytest.fixture()
async def db_con():
    await db.connect()
    yield db
    await db.disconnect()
