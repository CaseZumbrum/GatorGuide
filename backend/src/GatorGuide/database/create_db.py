from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import GatorGuide.database.models as models
import pathlib


sqlite_file_name = pathlib.Path(__file__).parent.resolve().joinpath("./database.db")
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_courses():
    with Session(engine) as session:
        DSA = models.Course(
            code="COP3530",
            name="Data Structures and Algorithms",
            description="foobarbaz",
            credits=3,
        )
        DISCRETE = models.Course(
            code="COT3100",
            name="Discrete Structures",
            description="lorim ipsum ts",
            credits=3,
        )
        CIS = models.Course(
            code="CIS4715",
            name="CS Teaching and Learning",
            description="don't do it",
            credits=1,
        )

        tech_electives = models.RequiredGroup(
            name="Tech Electives", credits=16, courses=[CIS]
        )

        CPE = models.Major(name="Computer Engineering")
        CPE.critical_tracking.append(DSA)
        CPE.required.append(DISCRETE)
        CPE.groups.append(tech_electives)

        session.add(DSA)
        session.add(DISCRETE)
        session.add(tech_electives)
        session.add(CPE)
        session.commit()


def main():
    create_db_and_tables()
    create_courses()


if __name__ == "__main__":
    # main()
    with Session(engine) as session:
        statement = select(models.Major).where(
            models.Major.name == "Computer Engineering"
        )
        x = session.exec(statement).one()
        x.print()
