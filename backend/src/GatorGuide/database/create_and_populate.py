from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import GatorGuide.database.models as models
import pathlib
import os
from GatorGuide.database import populate_courses


sqlite_file_name = pathlib.Path(__file__).parent.resolve().joinpath("./database.db")

if os.path.isfile(sqlite_file_name):
    os.remove(sqlite_file_name)

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
    with Session(engine) as session:
        populate_courses(session)
