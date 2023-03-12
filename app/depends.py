from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.connection import Session
from app.auth_user import UserUseCases


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


def token_verifier(
    db_session: Session = Depends(get_db_session),
    token = Depends(oauth_scheme)
):
    uc = UserUseCases(db_session=db_session)
    uc.verify_token(access_token=token)
