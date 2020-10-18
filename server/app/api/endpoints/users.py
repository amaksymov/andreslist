from fastapi import APIRouter, Depends

from app.models.user import User, get_current_user

router = APIRouter()


@router.get("/me", response_model=User, response_model_exclude={'password_hash'})
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
