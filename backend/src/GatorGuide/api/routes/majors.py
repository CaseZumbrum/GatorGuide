from fastapi import APIRouter, Depends, HTTPException
from GatorGuide.api.db_dependency import db_engine
from GatorGuide.database.models import Major

router = APIRouter()


@router.get("/", response_model=list[Major])
def get_all_majors():
    """Fetch all majors from the database.

    Returns:
        list[Major]: All majors from the database
    """
    return db_engine.read_all_majors()


@router.get("/{name}", response_model=Major)
def get_major(name: str):

    """
    Retrieve a major by its name.

    Args:
        name (str): The name of the major to retrieve.

    Returns:
        Major: The major object if found.

    Raises:
        HTTPException: If the major is not found in the database.
    """
    try:
        return db_engine.read_major(name)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Major '{name}' not found")


@router.delete("/{name}")
def delete_major(name: str):
    """
    Delete a major by its name.

    Args:
        name (str): The name of the major to delete.

    Returns:
        dict: A dictionary with a message indicating the major was deleted successfully.

    Raises:
        HTTPException: If the major is not found in the database.
    """
    try:
        major = db_engine.read_major(name)
        db_engine.delete(major)
        return {"message": f"Major '{name}' deleted successfully"}
    except Exception:
        raise HTTPException(status_code=404, detail=f"Major '{name}' not found")

@router.post("/", response_model=Major)
def create_major(major: Major):

    """
    Create a new major in the database.

    Args:
        major (Major): The major object to be created.

    Returns:
        Major: The created major object.

    Raises:
        HTTPException: If the creation of the major fails.
    """

    try:
        db_engine.write(major)
        return major
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to create major")