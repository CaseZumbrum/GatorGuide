from fastapi import APIRouter, Depends, HTTPException
from GatorGuide.api.db_dependency import db_engine
from GatorGuide.database.models import Major

router = APIRouter()


@router.get("", response_model=list[Major])
def get_all_majors():
    """Fetch all majors from the database."""
    return db_engine.read_all_majors()


@router.get("/{name}", response_model=Major)
def get_major(name: str):
    """Fetch a specific major by name."""
    try:
        return db_engine.read_major(name)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Major '{name}' not found")


@router.delete("/{name}")
def delete_major(name: str):
    """Delete a major by name."""
    try:
        major = db_engine.read_major(name)
        db_engine.delete(major)
        return {"message": f"Major '{name}' deleted successfully"}
    except Exception:
        raise HTTPException(status_code=404, detail=f"Major '{name}' not found")

@router.post("/", response_model=Major)
def create_major(major: Major):
    """Create a new major in the database."""
    try:
        db_engine.write(major)
        return major
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to create major")