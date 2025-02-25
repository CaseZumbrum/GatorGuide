# Code for after user functions are implemented in db_engine API, DOES NOT CURRENTLY WORK

from fastapi import APIRouter, Depends
from GatorGuide.api.db_dependency import get_db
from GatorGuide.database.models import User
from GatorGuide.database.db_engine import DB_Engine
from typing import List

router = APIRouter()

@router.get("/", response_model=List[User])
def get_users(db: DB_Engine = Depends(get_db)):
    """Fetch all users from the database"""
    return db.read_all_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: DB_Engine = Depends(get_db)):
    """Fetch a single user by ID"""
    return db.read_user(user_id)

@router.post("/", response_model=User)
def create_user(user: User, db: DB_Engine = Depends(get_db)):
    """Add a new user"""
    db.write(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: DB_Engine = Depends(get_db)):
    """Delete a user by ID"""
    user = db.read_user(user_id)
    if user:
        db.delete(user)
        return {"message": f"User {user_id} deleted successfully"}
    return {"error": "User not found"}
