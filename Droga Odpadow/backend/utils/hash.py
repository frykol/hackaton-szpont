
from hashlib import sha256

def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    return hashed_password == sha256(password.encode()).hexdigest()
