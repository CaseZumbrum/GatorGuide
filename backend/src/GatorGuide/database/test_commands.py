from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import GatorGuide.database.models as models
import pathlib
import os

sqlite_file_name = (
    pathlib.Path(__file__).parent.resolve().joinpath("./testing_database.db")
)

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

with Session(engine) as session:
    statement = select(models.Major)
    x = session.exec(statement)
    for m in x:
        print(m)
        for g in m.groups:
            print(g)
            for c in g.courses:
                print(c)
