from GatorGuide.database.workflow.create import create_db_and_tables
from GatorGuide.database.db_engine import DB_Engine
from GatorGuide.database.models import Course, PrequisiteGroup
import os
from pathlib import Path
import pytest
from sqlalchemy.exc import NoResultFound

sqlite_file_name = Path(__file__).parent.resolve().joinpath("./database.db")


def test_course_insertion():
    c1 = Course(
        code="COP3502",
        name="Programming Fundamentals 1",
        description="Introduction to programming",
        credits=4,
    )
    e.write(c1)
    c2 = e.read_course(code="COP3502")

    assert c1 == c2


def test_course_deletion():
    c1 = Course(
        code="COP3502",
        name="Programming Fundamentals 1",
        description="Introduction to programming",
        credits=4,
    )
    e.write(c1)
    e.delete(c1)
    with pytest.raises(NoResultFound):
        e.read_course("COP3502")


def test_accessing_nonexistant_course():
    with pytest.raises(NoResultFound):
        e.read_course("COP3503")


def test_course_prerequisites():
    c1 = Course(
        code="COP3530",
        name="DSA",
        description="Introduction to programming",
        credits=4,
    )
    c2 = Course(
        code="COP3503",
        name="Programming Fundamentals 2",
        description="Introduction to programming",
        credits=4,
    )
    c3 = Course(
        code="COP3502",
        name="Programming Fundamentals 1",
        description="Introduction to programming",
        credits=4,
    )

    c_t2 = Course(
        code="COP3530",
        name="DSA",
        description="Introduction to programming",
        credits=4,
    )

    c1.prerequisites.append(PrequisiteGroup(courses=[c2]))
    c2.prerequisites.append(PrequisiteGroup(courses=[c3]))

    e.write(c1)

    # ensure it is stored in the database properly
    c_t = e.read_course("COP3530")

    # does not include a prereq one layer down
    c_t2.prerequisites.append(
        PrequisiteGroup(
            courses=[
                Course(
                    code="COP3503",
                    name="Programming Fundamentals 2",
                    description="Introduction to programming",
                    credits=4,
                )
            ]
        )
    )
    assert c_t == c1
    assert c_t2 != c1


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    global e

    # stuff that happens before tests

    create_db_and_tables(sqlite_file_name)

    e = DB_Engine(sqlite_file_name)

    yield  # tests happen here

    # everything that happens after all test

    del e
    os.remove(sqlite_file_name)


if __name__ == "__main__":
    create_db_and_tables(sqlite_file_name)

    e = DB_Engine(sqlite_file_name)

    test_course_prerequisites()

    del e
    os.remove(sqlite_file_name)
