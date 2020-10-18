from fastapi import APIRouter

from app.api.endpoints import (
    login, users, events, announcements,
    responses, comments,
)

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(announcements.router, prefix="/announcements",
                          tags=["announcements"])
api_router.include_router(responses.router, prefix="/responses",
                          tags=["responses"])
api_router.include_router(comments.router, prefix="/comments",
                          tags=["comments"])
