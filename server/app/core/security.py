from itsdangerous import Signer
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app import settings

signer = Signer(settings.SECRET_KEY)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
