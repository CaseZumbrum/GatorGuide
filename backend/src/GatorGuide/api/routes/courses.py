from fastapi import APIRouter, Depends, HTTPException
from GatorGuide.api.db_dependency import db_engine
from GatorGuide.database.models import Course

router = APIRouter()


@router.get("", response_model=list[Course])
def get_all_courses():
    """Fetch all courses from the database."""
    return db_engine.read_all_courses()


@router.get("/{code}", response_model=Course)
def get_course(code: str):
    """Fetch a specific course by its course code."""
    try:
        return db_engine.read_course(code)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Course '{code}' not found")


@router.delete("/{code}")
def delete_course(code: str):
    """Delete a course by course code."""
    try:
        course = db_engine.read_course(code) 
        db_engine.delete(course)
        return {"message": f"Course '{code}' deleted successfully"}
    except Exception:
        raise HTTPException(status_code=404, detail=f"Course '{code}' not found")

@router.post("/", response_model=Course)
def create_course(course: Course):
    """Create a new course in the database."""
    try:
        db_engine.write(course)
        return course
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to create course")
