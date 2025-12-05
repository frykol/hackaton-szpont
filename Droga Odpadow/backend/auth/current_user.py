from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from sqlmodel import Session, select
from database import session
from user import user
from auth.auth import SECRET_KEY, ALGORITHM
import uuid
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/")

security = HTTPBearer()

def get_current_user(cred: HTTPAuthorizationCredentials = Depends(security),session: Session = Depends(session.get_session)) -> user.User:

    token = cred.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_str = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    try:
        user_id = uuid.UUID(user_id_str)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token format")

    user_ret = session.get(user.User, user_id)
    if not user_ret:
        raise HTTPException(status_code=404, detail="User not found")

    return user_ret