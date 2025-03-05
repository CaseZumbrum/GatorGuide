from GatorGuide.database.workflow.create import create_db_and_tables
from GatorGuide.database.db_engine import DB_Engine
from GatorGuide.database.models import Course, Major
import os
from pathlib import Path
import pytest

sqlite_file_name = Path(__file__).parent.resolve().joinpath("./database.db")

create_db_and_tables(sqlite_file_name)

e = DB_Engine(sqlite_file_name)


def test_db_exists():
    assert os.path.exists(sqlite_file_name)


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


@pytest.fixture(scope="session", autouse=True)
def run_before_and_after_tests():
    global e

    # stuff that happens before tests

    yield  # tests happen here

    # everything that happens after all test

    del e
    os.remove(sqlite_file_name)


if __name__ == "__main__":
    pass
