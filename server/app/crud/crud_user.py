from typing import Optional

from app.crud.base import CRUDBase
from app.db import db
from app.db.tables import users
from app.models.user import User, UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def create(self, *, obj_in: UserCreate) -> User:
        last_record_id = await self.db.execute(
            query=(
                self.table
                .insert(
                    values={
                        "username": obj_in.username,
                        "last_name": obj_in.last_name,
                        "first_name": obj_in.first_name,
                        "email": obj_in.email,
                        "password_hash": get_password_hash(obj_in.password),
                    }
                )
            )
        )
        return await self.get(last_record_id)

    async def get_by_email(self, *, email: str) -> Optional[User]:
        if result := await db.fetch_one(
            query=(
                self.table.select()
                .where(
                    self.table.c.email == email
                )
            )
        ):
            return self.model(**result)

    async def authenticate(self, *, email: str, password: str) -> Optional[User]:
        user = await self.get_by_email(email=email)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user


user = CRUDUser(users, User, db)
