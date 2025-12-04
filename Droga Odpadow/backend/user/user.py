from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship
import uuid

if TYPE_CHECKING:
    from role.role import Role, RolePublic

class UserBase(SQLModel):
    imie: str = Field(index=True) 
    nazwisko: str = Field(index=True)
    login: str = Field(index=True, unique=True)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password: str
    role_id: int | None = Field(default=None, foreign_key="role.id")

    role: "Role" = Relationship(back_populates="users")

class UserPublic(UserBase):
    id: uuid.UUID

class UserWithRolePublic(UserBase):
    id: uuid.UUID
    role: Optional["RolePublic"] = None

class UserPost(UserBase):
    password: str

class UserUpdate(UserBase):
    imie: str | None = None
    nazwisko: str | None = None
    password: str | None = None
