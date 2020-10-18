from app.crud.base import CRUDBase
from app.db import db
from app.db.tables import events
from app.models.event import Event, EventCreate, EventUpdate


class CRUDEvent(CRUDBase[Event, EventCreate, EventUpdate]):
    async def create_with_owner(
        self, *, obj_in: EventCreate, owner_id: int,
    ) -> Event:
        last_record_id = await self.db.execute(
            query=(
                self.table
                .insert(
                    values={
                        **obj_in.dict(),
                        "user_id": owner_id,
                    }
                )
            )
        )
        return await self.get(last_record_id)


event = CRUDEvent(events, Event, db)
