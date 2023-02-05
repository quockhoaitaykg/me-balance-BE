from datetime import datetime
from pydantic import BaseModel


class UsersBaseModel(BaseModel):
    name: str | None = None
    email: str | None = None
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    #
    # class Config:
    #     orm_mode = True

