from sqlmodel import Session, create_engine, select
from GatorGuide.database.models import Course, Major, Semester, User, FourYearPlan
import pathlib

sqlite_file_name = (
    pathlib.Path(__file__).parent.resolve().joinpath("./user-database.db")
)

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


with Session(engine) as session:
    # s = Semester()
    # statement = select(Course).where(Course.code == "COP3502C")
    # s.courses.append(session.exec(statement).one())

    # m = Major(name="CPE")
    # p = FourYearPlan(name="test", major=m)
    # p.semesters.append(s)

    # u = User(
    #     name="john doe", email="youdontneedtoknowthis@ufl.edu", password="wordpass"
    # )
    # u.plans.append(p)

    # session.add(u)
    # session.commit()

    statement = select(User)
    u = session.exec(statement).one()
    print(u.plans[0].semesters[0].courses)
