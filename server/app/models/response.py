from pydantic import BaseModel


class ResponseOk(BaseModel):
    status: str = 'ok'
