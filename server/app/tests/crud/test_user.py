import pytest

from databases import Database
from app import crud
from app.models.user import UserCreate
from app.tests.utils.utils import random_lower_string, random_email


@pytest.mark.asyncio
async def test_create_user(db_con: Database) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(
        first_name="John",
        last_name="Doe",
        username=random_lower_string(),
        email=email,
        password=password,
    )
    user = await crud.user.create(obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "password_hash")
