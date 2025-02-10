from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import GatorGuide.database.models as models
import pathlib
import os

sqlite_file_name = pathlib.Path(__file__).parent.resolve().joinpath("./database.db")

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

with Session(engine) as session:
    statement = select(models.Course).where(models.Course.code == "COP3530")
    x = session.exec(statement)
    for c in x:
        for g in c.prerequisites:
            print(g.courses)
