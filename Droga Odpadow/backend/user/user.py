from sqlmodel import SQLModel, Field
import uuid


class UserBase(SQLModel):
    imie: str = Field(index=True) 
    nazwisko: str = Field(index=True)
    login: str = Field(index=True, unique=True)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password: str

class UserPublic(UserBase):
    id: uuid.UUID

class UserPost(UserBase):
    password: str

class UserUpdate(UserBase):
    imie: str | None = None
    nazwisko: str | None = None
    password: str | None = None
