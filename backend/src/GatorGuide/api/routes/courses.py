from fastapi import APIRouter, Depends, HTTPException
from GatorGuide.api.db_dependency import db_engine
from GatorGuide.database.models import Course

router = APIRouter()


@router.get("/", response_model=list[Course])
def get_all_courses():
    """Fetch all courses from the database.

    Returns:
        list[Course]: All courses from the database
    """

    return db_engine.read_all_courses()


@router.get("/{code}", response_model=Course)
def get_course(code: str):

    """Fetch a single course by its code.

    Args:
        code (str): The course code to retrieve.

    Returns:
        Course: The course object if found.

    Raises:
        HTTPException: If the course is not found in the database.
    """
    try:
        return db_engine.read_course(code)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Course '{code}' not found")


@router.delete("/{code}")
def delete_course(code: str):

    """Delete a single course by its code.

    Args:
        code (str): The course code to delete.

    Returns:
        dict: A message indicating successful deletion of the course.

    Raises:
        HTTPException: If the course is not found in the database.
    """
    try:
        course = db_engine.read_course(code) 
        db_engine.delete(course)
        return {"message": f"Course '{code}' deleted successfully"}
    except Exception:
        raise HTTPException(status_code=404, detail=f"Course '{code}' not found")

@router.post("/", response_model=Course)
def create_course(course: Course):

    """Create a new course in the database.

    Args:
        course (Course): The course object to be created.

    Returns:
        Course: The created course object.

    Raises:
        HTTPException: If the creation of the course fails.
    """
    try:
        db_engine.write(course)
        return course
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to create course")
