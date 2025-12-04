from fastapi import FastAPI, HTTPException
from database import session
from pydantic import BaseModel
from sqlmodel import SQLModel
from contextlib import asynccontextmanager

from user import user_router
from role import role_router

from user.user import User, UserPublic, UserWithRolePublic
from role.role import RolePublic, Role, RoleWithUsersPublic

Role.model_rebuild()
RolePublic.model_rebuild()
RoleWithUsersPublic.model_rebuild()
UserPublic.model_rebuild()
UserWithRolePublic.model_rebuild()

@asynccontextmanager
async def lifespan(app: FastAPI):
    session.create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(user_router.router)
app.include_router(role_router.router)

# @app.on_event("startup")
# async def on_startup():
#     session.create_db_and_tables()


class User(BaseModel):
    wiek: int
    nazwa: str

@app.get("/")
def root():
    return {"msg":"Elloss"} 

@app.get("/test")
def test():
    return [{"msg": "asd"}, {"msg": "123"}]

@app.post("/test")
def dodaj(b: User):
    return [b, {"Jaka metoda": "Post"}]



