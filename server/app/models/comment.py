from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    text: str
    created_date: datetime
    user_id: int
    event_id: int


class CommentIn(BaseModel):
    text: str
    event_id: int
