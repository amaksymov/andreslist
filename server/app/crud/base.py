from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

import sqlalchemy as sa
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from databases import Database

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateModelType = TypeVar("CreateModelType", bound=BaseModel)
UpdateModelType = TypeVar("UpdateModelType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateModelType, UpdateModelType]):
    def __init__(self, table: sa.Table, model: Type[ModelType], db: Database):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `table`: A SQLAlchemy table object
        * `schema`: A Pydantic model class
        """
        self.table = table
        self.model = model
        self.db = db

    async def get(self, _id: Any) -> Optional[ModelType]:
        if result := await self.db.fetch_one(
            query=(
                self.table
                .select()
                .where(
                    self.table.c.id == _id
                )
            )
        ):
            return self.model(**result)

    async def get_multi(
        self, *, offset: int = 0, limit: int = 100
    ) -> List[ModelType]:
        if result := await self.db.fetch_all(
            query=(
                self.table
                .select()
                .offset(offset)
                .limit(limit)
            )
        ):
            return [self.model(**r) for r in result]

    async def create(self, *, obj_in: CreateModelType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        last_record_id = await self.db.execute(
            query=(
                self.table
                .insert(values={**obj_in_data})
            )
        )
        return await self.get(last_record_id)

    async def update(
        self,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateModelType, Dict[str, Any]]
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        last_record_id = await self.db.execute(
            query=(
                self.table.update(values=update_data)
                .where(self.table.c.id == db_obj.id)
            )
        )
        return db_obj

    async def delete(self, *, _id: int) -> None:
        await self.db.execute(
            query=(
                self.table.delete()
                .where(
                    self.table.c.id == _id
                )
            )
        )
