# ^(?!.*(COP3520)).*^(COP3|MHF4) useful regex
from GatorGuide.database.models import Major, Course, RequiredGroup
from pathlib import Path
from sqlmodel import Session, SQLModel, create_engine, select
import os
import re


class DB_Engine:
    """
    API for using the GatorGuide Course Database
    """

    def __init__(self, path: Path) -> None:
        """Create a DB_Engine instance

        Args:
            path (Path): Path to the DB in use
        """
        sqlite_url = f"sqlite:///{path}"
        self.engine = create_engine(sqlite_url)

    def write(self, object: SQLModel):
        """Write a SQLModel object to the database. Updates existing objects and adds new ones

        Args:
            object (SQLModel): Object to be written
        """
        with Session(self.engine) as session:
            session.add(object)
            session.commit()

    def delete(self, object: SQLModel):
        """Delete a SQLModel object from the database

        Args:
            object (SQLModel): Object to be deleted, should exist in the database
        """
        with Session(self.engine) as session:
            session.delete(object)
            session.commit()

    def add_to_group(self, group: RequiredGroup, regex: str) -> None:
        """Function to add courses to a RequiredGroup object via regex parsing on course codes

        ex: ^(?!.*(COP3520)).*^(COP3|MHF4) will add all 3000 level COP courses
        (not including COP3502) and all 4000 level MHF courses to the RequiredGroup.courses list

        Args:
            group (RequiredGroup): Required group to add to
            regex (str): compleable regex that matches to course codes
        """
        pattern = re.compile(regex)
        with Session(self.engine) as session:
            statement = select(Course)
            x = session.exec(statement)
            for c in x:
                if pattern.match(c.code):
                    group.courses.append(c)
        self.write(group)

    def read_major(self, name: str) -> Major:
        """read a major from the DB by name

        Args:
            name (str): name of the major

        Returns:
            Major: Major object matching the name
        """
        with Session(self.engine) as session:
            statement = select(Major).where(Major.name == name)
            return session.exec(statement).one()

    def read_all_majors(self) -> list[Major]:
        """Read all majors from the database

        Returns:
            list[Major]: All majors from the database
        """
        with Session(self.engine) as session:
            statement = select(Major)
            return list(session.exec(statement).all())

    def read_course(self, code: str) -> Course:
        """Read a single course from the database by code

        Args:
            code (str): course code

        Returns:
            Course: Course with matching code
        """
        with Session(self.engine) as session:
            statement = select(Course).where(Course.code == code)
            return session.exec(statement).one()

    def read_all_courses(self) -> list[Course]:
        """Retrieve all courses from the database

        Returns:
            list[Course]: All courses from the database
        """
        with Session(self.engine) as session:
            statement = select(Course)
            return list(session.exec(statement).all())


if __name__ == "__main__":
    import shutil

    base_db_file_name = Path(__file__).parent.resolve().joinpath("./database.db")

    sqlite_file_name = Path(__file__).parent.resolve().joinpath("./testing_database.db")

    if os.path.isfile(sqlite_file_name):
        os.remove(sqlite_file_name)

    if os.path.isfile(base_db_file_name):
        shutil.copyfile(base_db_file_name, sqlite_file_name)

    cpe = Major(
        name="Computer Engineering",
    )
    g = RequiredGroup(name="tech electives", credits=16)

    e = DB_Engine(sqlite_file_name)
    e.add_to_group(g, "^(?!.*(COP3520)).*^(COP3|MHF4)")
    cpe.groups.append(g)
    e.write(cpe)
