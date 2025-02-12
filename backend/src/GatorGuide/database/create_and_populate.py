from sqlmodel import Session, SQLModel, create_engine
import pathlib
import os
from GatorGuide.database.gather_courses import populate_courses

# path of the DB
sqlite_file_name = pathlib.Path(__file__).parent.resolve().joinpath("./database.db")

# If the DB already exists, delete it
if os.path.isfile(sqlite_file_name):
    os.remove(sqlite_file_name)

sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)


def create_db_and_tables():
    """Create the DB and the tables"""
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
    with Session(engine) as session:
        populate_courses(session)
