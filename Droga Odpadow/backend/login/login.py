from sqlmodel import SQLModel

class LoginRequest(SQLModel):
    login: str
    password: str

class Token(SQLModel):
    access_token: str
    toke_type: str = "bearer"