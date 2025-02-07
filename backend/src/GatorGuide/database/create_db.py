from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import GatorGuide.database.models as models



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_courses():
    with Session(engine) as session:

        
        DSA = models.Course(code="COP3530", name="Data Structures and Algorithms", description="foobarbaz")
        CPE = models.Major(name="Computer Engineering")
        CPE.critical_tracking.append(DSA)
        session.add(DSA)
        session.add(CPE)
        session.commit()



def main():
    create_db_and_tables()
    create_courses()


if __name__ == "__main__":
    main()

