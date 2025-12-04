from typing import Annotated

from sqlmodel import Session, create_engine, SQLModel
from fastapi import Depends

from .config import SQLALCHEMY_DATABASE_URL


CONNECT_ARGS = {"check_same_thread": False}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=CONNECT_ARGS)

def create_db_and_tables():
    from user.user import User, UserPublic
    from role.role import Role, RolePublic

    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
