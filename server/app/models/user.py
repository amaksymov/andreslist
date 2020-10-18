from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from fastapi import Depends, HTTPException, status

from app import db
from app.db.tables import users
from app.core.security import oauth2_scheme, signer


class User(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    last_name: str
    email: str
    created_date: datetime
    updated_date: datetime
    password_hash: str

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class UserCreate(BaseModel):
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
    password: str


class UserUpdate(UserCreate):
    pass


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = await get_user(signer.unsign(token.encode('utf-8')).decode('utf-8'))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_user(username: str) -> Optional[User]:
    query = users.select().where(users.c.username == username)
    if row := await db.fetch_one(query=query):
        return User(**row)
