from fastapi import APIRouter, Depends
from GatorGuide.api.db_dependency import get_db
from GatorGuide.database.models import Course
from GatorGuide.database.db_engine import DB_Engine
from typing import List

router = APIRouter()

"""Fetch all courses"""
@router.get("/", response_model=List[Course])
def get_courses(db: DB_Engine = Depends(get_db)):
    return db.read_all_courses()

"""Fetch a single course by ID"""
@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int, db: DB_Engine = Depends(get_db)):
    return db.read_course(course_id)

"""Add a new course"""
@router.post("/", response_model=Course)
def create_course(course: Course, db: DB_Engine = Depends(get_db)):
    db.write(course)
    return course

"""Delete a course by ID"""
@router.delete("/{course_id}")
def delete_course(course_id: int, db: DB_Engine = Depends(get_db)):
    course = db.read_course(course_id)
    if course:
        db.delete(course)
        return {"message": f"Course {course_id} deleted successfully"}
    return {"error": "Course not found"}
