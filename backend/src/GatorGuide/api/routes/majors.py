from fastapi import APIRouter, Depends
from GatorGuide.api.db_dependency import get_db
from GatorGuide.database.models import Major
from GatorGuide.database.db_engine import DB_Engine
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Major])
def get_majors(db: DB_Engine = Depends(get_db)):
    """Fetch all majors from the database"""
    return db.read_all_majors()

@router.get("/{major_id}", response_model=Major)
def get_major(major_id: int, db: DB_Engine = Depends(get_db)):
    """Fetch a single major by ID"""
    return db.read_major(major_id)

@router.post("/", response_model=Major)
def create_major(major: Major, db: DB_Engine = Depends(get_db)):
    """Add a new major"""
    db.write(major)
    return major

@router.delete("/{major_id}")
def delete_major(major_id: int, db: DB_Engine = Depends(get_db)):
    """Delete a major by ID"""
    major = db.read_major(major_id)
    if major:
        db.delete(major)
        return {"message": f"Major {major_id} deleted successfully"}
    return {"error": "Major not found"}
