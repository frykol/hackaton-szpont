from fastapi import HTTPException
from database import session
from user import user
from hashlib import sha256

def get_user(user_login: str, session: session.SessionDep) -> user.User:
    user_get = session.query(user.User).filter(user.User.login == user_login).first() 
    if not user_get:
        raise HTTPException(status_code=404, detail="User not found")
    return user_get

def create_user(user_create: user.UserPost, session: session.SessionDep) -> user.User:
    user_create.password = sha256(user_create.password.encode()).hexdigest()
    db_user = user.User.model_validate(user_create)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user 
