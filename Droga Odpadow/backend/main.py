from fastapi import FastAPI, HTTPException
from database import session
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/user/{id}")
def get_user(id: int):
    u = User(wiek=12, nazwa="Ktos")
    u2 = User(wiek=22, nazwa="Ktos inny")
    if id == 2:
         raise HTTPException(status_code=404, detail="User not found")
    return [u, u2]

@app.post("/user", status_code=201)
def add_user(b: User):
    if b.nazwa == "asd":
        raise HTTPException(status_code=404, detail="Jakis błąd")
    return [b, {"message": "Błąd"}]

@app.on_event("startup")
def on_startup():
    session.create_db_and_tables()