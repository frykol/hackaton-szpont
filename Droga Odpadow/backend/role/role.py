from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from user.user import User, UserPublic

class RoleBase(SQLModel):
    type: str = Field(index=True)

class Role(RoleBase, table=True):
    id: int = Field(default=None, primary_key=True)

    users: list["User"] = Relationship(back_populates="role")

class RolePublic(RoleBase):
    id: int

class RoleWithUsersPublic(RoleBase):
    id: int
    users: list["UserPublic"] = []

class RolePost(RoleBase):
    type: str

class RoleUpdate(RoleBase):
    type: str | None = None