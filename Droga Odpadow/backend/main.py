from fastapi import FastAPI
from database import session

app = FastAPI()

session.create_db_and_tables()

@app.get("/")
def root():
    return {"msg":"Elloss"} 

@app.get("/test")
def test():
    return [{"msg": "asd"}, {"msg": "123"}]