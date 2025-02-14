from GatorGuide.database.workflow import populate_courses, populate_majors
from GatorGuide.database.db_engine import DB_Engine
from sqlmodel import SQLModel, create_engine
import pathlib
import os

# this import is necessary to create the database
from GatorGuide.database import models

# path of the DB
sqlite_file_name = pathlib.Path(__file__).parent.resolve().joinpath("./database.db")

# If the DB already exists, delete it
if os.path.isfile(sqlite_file_name):
    os.remove(sqlite_file_name)

sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)


if __name__ == "__main__":
    """Create the DB and the tables"""
    SQLModel.metadata.create_all(engine)

    print("________________________")
    print("CREATING DB")
    e = DB_Engine(sqlite_file_name)
    print("________________________")
    print("ADDING COURSES")
    populate_courses.populate(e)
    print("________________________")
    print("ADDING MAJORS")
    populate_majors.populate(e)
