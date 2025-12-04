from fastapi import HTTPException, Depends
from login.login import LoginRequest, Token
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from database import session
from user.user import User
from user import user_service
from utils import hash
from auth import auth

def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(session.get_session)) -> Token:
    
    login = form_data.username
    password = form_data.password


    user_get = user_service.get_user(login, session)

    if not hash.verify_password(password, user_get.password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    access_token = auth.create_access_token({"sub": str(user_get.id)})

    return Token(access_token=access_token)
