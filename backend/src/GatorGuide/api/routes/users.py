# Code for after user functions are implemented in db_engine API, DOES NOT CURRENTLY WORK

from fastapi import APIRouter, Depends, status, Response, Cookie
from GatorGuide.api.db_dependency import get_db
from GatorGuide.database.models import User
from GatorGuide.database.db_engine import DB_Engine
from sqlalchemy.exc import NoResultFound, IntegrityError
from typing import Annotated
from GatorGuide.database.exceptions import SessionExpiredError

router = APIRouter()


@router.get("/me")
def get_me(
    response: Response,
    db: DB_Engine = Depends(get_db),
    GatorGuide_Session: Annotated[str | None, Cookie()] = None,
):
    if GatorGuide_Session:
        try:
            u = db.load_user_session(GatorGuide_Session)
            return u
        except NoResultFound:
            response.status_code = status.HTTP_404_NOT_FOUND
            response.delete_cookie("GatorGuide_Session")
        except SessionExpiredError:
            response.status_code = status.HTTP_401_UNAUTHORIZED
            response.delete_cookie("GatorGuide_Session")
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED


@router.get("/{user_name}/login")
def login(
    user_name: str, password: str, response: Response, db: DB_Engine = Depends(get_db)
):
    """Fetch a single user by ID"""
    try:
        u = db.read_user(user_name)
    except NoResultFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": "User not found"}
    if db.authenticate_user(u, password):
        uuid = db.create_user_session(u)
        response.set_cookie("GatorGuide_Session", uuid)
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Error": "Incorrect Password"}


@router.get("/{user_name}", response_model=User)
def get_user(
    user_name: str, password: str, response: Response, db: DB_Engine = Depends(get_db)
):
    """Fetch a single user by ID"""
    try:
        u = db.read_user(user_name)
    except NoResultFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": "User not found"}
    if db.authenticate_user(u, password):
        return u
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Error": "Incorrect Password"}


@router.post("/", response_model=User)
def create_user(
    user: User, password: str, response: Response, db: DB_Engine = Depends(get_db)
):
    """Add a new user"""

    try:
        db.write(user)
        db.create_user_authentication(user, password)
    except IntegrityError:
        response.status_code = status.HTTP_409_CONFLICT
        return {"Error", "Username or Email already exists"}
    return user


@router.delete("/{user_name}")
def delete_user(user_name: str, db: DB_Engine = Depends(get_db)):
    """Delete a user by ID"""
    user = db.read_user(user_name)
    if user:
        db.delete(user)
        return {"message": f"User {user_name} deleted successfully"}
    return {"error": "User not found"}
