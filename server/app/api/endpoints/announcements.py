from typing import List

from fastapi import APIRouter, Depends
from app.models.announcement import Announcement, AnnouncementIn
from app.models.user import User, get_current_user
from app import db
from app.db.tables import announcements

router = APIRouter()


@router.get("/", response_model=List[Announcement])
async def read_announcement():
    product_set = await db.fetch_all(query=announcements.select())
    return [Announcement(**p) for p in product_set]


@router.post("/", response_model=Announcement)
async def create_announcement(
    announcement: AnnouncementIn,
    user: User = Depends(get_current_user),
):
    last_record_id = await db.execute(
        query=(
            announcements.insert()
            .values(
                title=announcement.title,
                description=announcement.description,
                user_id=user.id,
            )
        )
    )
    announcement_from_db = await db.fetch_one(
        query=(
            announcements.select()
            .where(announcements.c.id == last_record_id)
        )
    )
    return Announcement(
        **announcement_from_db,
    )
