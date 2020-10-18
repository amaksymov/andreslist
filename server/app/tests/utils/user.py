from app import crud
from app.models.user import User, UserCreate
from app.tests.utils.utils import random_email, random_lower_string


async def create_random_user() -> User:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(
        username=random_lower_string(),
        email=email,
        password=password,
        first_name="John",
        last_name="Doe",
    )
    user = await crud.user.create(obj_in=user_in)
    return user
