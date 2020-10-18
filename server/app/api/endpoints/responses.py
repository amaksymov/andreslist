from typing import List

from fastapi import APIRouter, Depends
from app.models.ad_response import AdResponse, AdResponseIn
from app.models.user import User, get_current_user
from app import db
from app.db.tables import responses

router = APIRouter()


@router.get("/", response_model=List[AdResponse])
async def read_ad_response(announcement_id: int):
    product_set = await db.fetch_all(
        query=(
            responses.select()
            .where(responses.c.announcement_id == announcement_id)
        )
    )
    return [AdResponse(**p) for p in product_set]


@router.post("/", response_model=AdResponse)
async def create_ad_response(
    response: AdResponseIn,
    user: User = Depends(get_current_user),
):
    last_record_id = await db.execute(
        query=(
            responses.insert()
            .values(
                description=response.description,
                user_id=user.id,
                announcement_id=response.announcement_id,
            )
        )
    )
    response_from_db = await db.fetch_one(
        query=(
            responses.select()
            .where(responses.c.id == last_record_id)
        )
    )
    return AdResponse(
        **response_from_db,
    )
