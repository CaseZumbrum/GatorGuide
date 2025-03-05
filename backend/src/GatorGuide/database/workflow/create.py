from sqlmodel import SQLModel, create_engine
import pathlib
import os

# this import is necessary to create the database
from GatorGuide.database import models

# path of the DB


def create_db_and_tables(sqlite_file_name):
    # If the DB already exists, delete it
    if os.path.isfile(sqlite_file_name):
        os.remove(sqlite_file_name)

    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url)
    """Create the DB and the tables"""
    SQLModel.metadata.create_all(engine)
    engine.dispose()


if __name__ == "__main__":
    sqlite_file_name = (
        pathlib.Path(__file__).parent.resolve().joinpath("../database.db")
    )
    create_db_and_tables(sqlite_file_name)
