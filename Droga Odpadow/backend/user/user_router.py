from fastapi import APIRouter
from database import session
from user import user
from user import user_service

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
def root():
    return {"message": "Work in progress"}


@router.get("/{user_login}", response_model=user.UserPublic)
def get_user(user_login: str, session: session.SessionDep):
    user_response = user_service.get_user(user_login, session)
    return user_response

@router.post("/", response_model=user.UserPublic)
def create_user(user_create: user.UserPost, session: session.SessionDep):
    user_response = user_service.create_user(user_create, session)
    return user_response
