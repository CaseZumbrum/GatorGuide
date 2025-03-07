# Code for after user functions are implemented in db_engine API, DOES NOT CURRENTLY WORK

from fastapi import APIRouter, Depends, status, Response
from GatorGuide.api.db_dependency import get_db
from GatorGuide.database.models import User
from GatorGuide.database.db_engine import DB_Engine
from hashlib import sha256
from sqlalchemy.exc import NoResultFound, IntegrityError


router = APIRouter()


@router.get("/{user_name}", response_model=User)
def get_user(
    user_name: str, password: str, response: Response, db: DB_Engine = Depends(get_db)
):
    """Fetch a single user by ID"""
    password = sha256(password.encode("utf-8")).hexdigest()
    try:
        u = db.read_user(user_name)
    except NoResultFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": "User not found"}
    if u.hashed_password == password:
        return u
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Error": "Incorrect Password"}


@router.post("/", response_model=User)
def create_user(user: User, response: Response, db: DB_Engine = Depends(get_db)):
    """Add a new user"""
    user.hashed_password = sha256(user.hashed_password.encode("utf-8")).hexdigest()
    try:
        db.write(user)
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
