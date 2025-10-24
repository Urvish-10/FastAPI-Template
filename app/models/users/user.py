import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlmodel import SQLModel, Field

# To avoid circular imports, use TYPE_CHECKING as a guard
# if TYPE_CHECKING:
#     from app.models import


class Users(SQLModel, table=True):
    __tablename__ = "users"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    name: str | None = Field(default=None, max_length=255)
    is_active: bool = True
    is_superuser: bool = True
    created_ts: datetime = Field(default_factory=datetime.now)
    password: str


# JSON payload containing an access token
class Token(SQLModel):
    user_id: uuid.UUID
    user_email: str
    user_name: str
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserUpdate(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)  # type: ignore
    password: str | None = Field(default=None, min_length=8, max_length=40)


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: uuid.UUID


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int
