# ^(?!.*(COP3520)).*^(COP3|MHF4) useful regex
from GatorGuide.database.models import (
    Major,
    Course,
    RequiredGroup,
    User,
    UserAuth,
    UserSession,
    FourYearPlan,
    Semester,
)
from GatorGuide.database.response_models import UserResponse, FourYearPlanResponse
from GatorGuide.database.exceptions import SessionExpiredError
from pathlib import Path
from sqlmodel import Session, SQLModel, create_engine, select
from hashlib import sha256
import os
import re
import string
import secrets
from time import time
from uuid import uuid4
from sqlalchemy.engine import URL


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
        self.session = Session(self.engine)

    def __del__(self):
        self.session.close()
        self.engine.dispose()

    def write(self, object: SQLModel):
        """Write a SQLModel object to the database. Updates existing objects and adds new ones

        Args:
            object (SQLModel): Object to be written
        """
        self.session.add(object)
        self.session.commit()
        self.session.refresh(object)

    def delete(self, object: SQLModel):
        """Delete a SQLModel object from the database

        Args:
            object (SQLModel): Object to be deleted, should exist in the database
        """
        self.session.delete(object)
        self.session.commit()

    def update_user_data(self, user: UserResponse):
        db_plans: list[FourYearPlan] = []
        for plan in user.plans:
            db_major = self.read_major(plan.major.name)
            db_semesters: list[Semester] = []
            for semester in plan.semesters:
                db_semesters.append(Semester())
                for i, course in enumerate(semester.courses):
                    db_semesters[-1].courses.append(self.read_course(course.code))
            db_plans.append(
                FourYearPlan(name=plan.name, major=db_major, semesters=db_semesters)
            )
        statement = select(User).where(User.name == user.name)
        db_user = self.session.exec(statement).one()
        db_user.plans = db_plans
        self.write(db_user)

    def update_user_plan(self, user: User, plan: FourYearPlanResponse):
        db_major = self.read_major(plan.major.name)
        db_semesters: list[Semester] = []
        for semester in plan.semesters:
            db_semesters.append(Semester())
            for i, course in enumerate(semester.courses):
                db_semesters[-1].courses.append(self.read_course(course.code))
        if plan.id:
            statement = select(FourYearPlan).where(FourYearPlan.id == plan.id)
            db_plan = self.session.exec(statement).one()
            db_plan.name = plan.name
            db_plan.major = db_major
            # for semester_old in db_plan.semesters:
            #     self.delete(semester_old)
            db_plan.semesters = db_semesters
        else:
            db_plan = FourYearPlan(
                name=plan.name, major=db_major, semesters=db_semesters
            )
            user.plans.append(db_plan)
        self.write(db_plan)
        self.write(user)

    def add_to_group(self, group: RequiredGroup, regex: str) -> None:
        """Function to add courses to a RequiredGroup object via regex parsing on course codes

        ex: ^(?!.*(COP3520)).*^(COP3|MHF4) will add all 3000 level COP courses
        (not including COP3502) and all 4000 level MHF courses to the RequiredGroup.courses list

        Args:
            group (RequiredGroup): Required group to add to
            regex (str): compleable regex that matches to course codes
        """
        pattern = re.compile(regex)
        statement = select(Course)
        x = self.session.exec(statement)
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
        statement = select(Major).where(Major.name == name)
        return self.session.exec(statement).one()

    def read_all_majors(self) -> list[Major]:
        """Read all majors from the database

        Returns:
            list[Major]: All majors from the database
        """
        statement = select(Major)
        return list(self.session.exec(statement).all())

    def read_course(self, code: str) -> Course:
        """Read a single course from the database by code

        Args:
            code (str): course code

        Returns:
            Course: Course with matching code
        """
        statement = select(Course).where(Course.code == code)
        return self.session.exec(statement).one()

    def read_all_courses(self) -> list[Course]:
        """Retrieve all courses from the database

        Returns:
            list[Course]: All courses from the database
        """
        statement = select(Course)
        return list(self.session.exec(statement).all())

    def read_user(self, username: str) -> User:
        """read a single user from the database by username

        Args:
            username (str): user name of the user

        Returns:
            User: User object
        """
        statement = select(User).where(User.name == username)
        return self.session.exec(statement).one()

    def authenticate_user(self, user: User, password: str) -> bool:
        """Authenticates a user by password

        Args:
            user (User): User object
            password (str): un-hashed password

        Returns:
            bool: whether authenication was successful
        """
        statement = select(UserAuth).where(UserAuth.user_id == user.id)
        a = self.session.exec(statement).one()
        print(password, a.salt, sha256((a.salt + password).encode("utf-8")).hexdigest())
        return sha256((a.salt + password).encode("utf-8")).hexdigest() == a.hashed

    def create_user_authentication(self, user: User, password: str) -> None:
        """Initialize the user authentication for a user, needs to be used when creating new user

        Args:
            user (User): User object
            password (str): un-hashed password
        """
        alphabet = string.ascii_letters + string.digits
        salt = "".join(secrets.choice(alphabet) for i in range(8))

        a = UserAuth(
            user_id=user.id,
            salt=salt,
            hashed=sha256((salt + password).encode("utf-8")).hexdigest(),
        )
        self.write(a)

    def create_user_session(self, user: User) -> str:
        """Create a user session in the database, return the session_id

        Args:
            user (User): User object

        Returns:
            str: session_id for the session
        """
        uuid = str(uuid4())
        s = UserSession(user_id=user.id, session_id=uuid, time=int(time()))
        self.write(s)
        return uuid

    def load_user_session(self, session_id: str) -> User:
        """Load the User associated with a session_id

        Args:
            session_id (str): session_id, likely from the browser cookie

        Raises:
            SessionExpiredError: Session has expired, cookie should be deleted

        Returns:
            User: User object associated with the session
        """
        statement = select(UserSession).where(UserSession.session_id == session_id)
        s = self.session.exec(statement).one()
        # one day timeout
        if int(time()) - s.time > (60 * 60 * 24):
            self.delete(s)
            raise SessionExpiredError
        else:
            s.time = int(time())
            user_statement = select(User).where(User.id == s.user_id)
            self.write(s)
            return self.session.exec(user_statement).one()


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
