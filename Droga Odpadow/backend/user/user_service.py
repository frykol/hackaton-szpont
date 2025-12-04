from fastapi import HTTPException
from sqlmodel import select
from database import session
from user import user
from role import role_service
from hashlib import sha256

def get_users(session: session.SessionDep) -> list[user.User]:
    users = session.exec(select(user.User)).all()
    return users

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

def update_user(user_login: str, user_update: user.UserUpdate, session: session.SessionDep) -> user.User:
    user_to_update = get_user(user_login, session)
    role_data = user_to_update.model_dump(exclude_unset=True)
    user_to_update.sqlmodel_update(user_update)
    session.add(user_to_update)
    session.commit()
    session.refresh(user_to_update)
    return user_to_update

def delete_user(user_login: str, session: session.SessionDep):
    user_to_delete = get_user(user_login, session)
    session.delete(user_to_delete)
    session.commit()
    return {"deleted": user_login}

def set_role_to_user(user_login: str, role_id: int, session: session.SessionDep) -> user.User:
    user_update = get_user(user_login, session)
    role_update = role_service.get_role(role_id, session)
    
    role_update.users.append(user_update)
    session.add(role_update)
    session.commit()
    session.refresh(role_update)
    return user_update

