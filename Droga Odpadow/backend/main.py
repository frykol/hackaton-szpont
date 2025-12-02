from fastapi import FastAPI, HTTPException
from database import session
from pydantic import BaseModel
from user import user_router

app = FastAPI()

app.include_router(user_router.router)

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


@app.on_event("startup")
def on_startup():
    session.create_db_and_tables()
