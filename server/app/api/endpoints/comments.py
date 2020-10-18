from typing import List

from fastapi import APIRouter, Depends
from app.models.comment import Comment, CommentIn
from app.models.user import User, get_current_user
from app import db
from app.db.tables import comments

router = APIRouter()


@router.get("/", response_model=List[Comment])
async def read_comment(event_id: int):
    product_set = await db.fetch_all(
        query=(
            comments.select()
            .where(comments.c.event_id == event_id)
        )
    )
    return [Comment(**p) for p in product_set]


@router.post("/", response_model=Comment)
async def create_comment(
    comment: CommentIn,
    user: User = Depends(get_current_user),
):
    last_record_id = await db.execute(
        query=(
            comments.insert()
            .values(
                text=comment.text,
                user_id=user.id,
                event_id=comment.event_id,
            )
        )
    )
    comment_from_db = await db.fetch_one(
        query=(
            comments.select()
            .where(comments.c.id == last_record_id)
        )
    )
    return Comment(
        **comment_from_db,
    )
