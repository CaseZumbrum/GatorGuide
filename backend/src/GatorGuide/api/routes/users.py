# Code for after user functions are implemented in db_engine API, DOES NOT CURRENTLY WORK

from fastapi import APIRouter, Depends, status, Response, Cookie, HTTPException
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
    """
    Retrieve the currently logged-in user based on the session cookie.

    Args:
        response (Response): The HTTP response object.
        db (DB_Engine, optional): Database engine dependency.
        GatorGuide_Session (str | None, optional): Session ID from the cookie.

    Returns:
        User: The user associated with the session if valid.

    Raises:
        HTTPException: If the session is not provided, not found, or expired.
    """

    if GatorGuide_Session:
        try:
            u = db.load_user_session(GatorGuide_Session)
            return u
        except NoResultFound:
            response.delete_cookie("GatorGuide_Session")
            raise HTTPException(status_code=404, detail="Session not found")
        except SessionExpiredError:
            response.delete_cookie("GatorGuide_Session")
            raise HTTPException(status_code=401, detail="Session expired")
    else:
        raise HTTPException(status_code=401, detail="No session provided")


@router.get("/{user_name}/login")
def login(
    user_name: str, password: str, response: Response, db: DB_Engine = Depends(get_db)
):
    """
    Log in as a user.

    Args:
        user_name (str): User name of the user to log in as.
        password (str): Password of the user to log in as.
        response (Response): The HTTP response object.
        db (DB_Engine, optional): Database engine dependency.

    Raises:
        HTTPException: If the user is not found or the password is incorrect.
    """
    try:
        u = db.read_user(user_name)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
    
    if db.authenticate_user(u, password):
        uuid = db.create_user_session(u)
        response.set_cookie("GatorGuide_Session", uuid)
    else:
        raise HTTPException(status_code=401, detail="Incorrect password")



@router.get("/{user_name}", response_model=User)
def get_user(
    user_name: str, password: str, response: Response, db: DB_Engine = Depends(get_db)
):
    """
    Get a user by name and password.

    Args:
        user_name (str): User name of the user to retrieve.
        password (str): Password of the user to retrieve.
        response (Response): The HTTP response object.
        db (DB_Engine, optional): Database engine dependency.

    Raises:
        HTTPException: If the user is not found or the password is incorrect.
    """

    try:
        u = db.read_user(user_name)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")

    if db.authenticate_user(u, password):
        return u
    else:
        raise HTTPException(status_code=401, detail="Incorrect password")



@router.post("/", response_model=User)
def create_user(
    user: User, password: str, response: Response, db: DB_Engine = Depends(get_db)
):
    """
    Create a new user with authentication in the database.

    Args:
        user (User): User object containing user information.
        password (str): Password for the new user.
        response (Response): The HTTP response object.
        db (DB_Engine, optional): Database engine dependency.

    Returns:
        User: The created user object.

    Raises:
        HTTPException: If a user with the same username or email already exists.
    """

    try:
        db.write(user)
        db.create_user_authentication(user, password)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Username or email already exists")
    
    return user



@router.delete("/{user_name}")
def delete_user(user_name: str, db: DB_Engine = Depends(get_db)):
    
    """
    Delete a user by username.

    Args:
        user_name (str): Username of the user to delete.
        db (DB_Engine, optional): Database engine dependency.

    Returns:
        dict: A message indicating successful deletion of the user.

    Raises:
        HTTPException: If the user is not found.
    """

    user = db.read_user(user_name)
    if user:
        db.delete(user)
        return {"message": f"User {user_name} deleted successfully"}
    
    raise HTTPException(status_code=404, detail="User not found")

