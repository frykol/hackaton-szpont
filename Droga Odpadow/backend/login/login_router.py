from fastapi import APIRouter
from database import session
from login.login import Token, LoginRequest
from login.login_service import login as loginf

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/", response_model=Token)
def login(data: LoginRequest, session: session.SessionDep):
    token = loginf(data, session)
    return token