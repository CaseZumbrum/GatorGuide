from GatorGuide.database.workflow.create import create_db_and_tables
from GatorGuide.database.db_engine import DB_Engine
from GatorGuide.database.models import Course, Major, RequiredGroup
import os
from pathlib import Path
import pytest
from sqlalchemy.exc import NoResultFound

sqlite_file_name = Path(__file__).parent.resolve().joinpath("./database.db")


def test_major_insertion():
    e.write(CPE)
    m = e.read_major("Computer Engineering")
    assert CPE == m


def test_major_deletion():
    e.write(CPE)
    e.delete(CPE)
    with pytest.raises(NoResultFound):
        e.read_major("Computer Engineering")


def test_reading_nonexistant_major():
    with pytest.raises(NoResultFound):
        e.read_major("Computer Engineering")


def test_reading_empty_major_list():
    assert e.read_all_majors() == []


def test_adding_course_group():
    e.write(DSA)
    e.write(COP3503)
    e.write(COP3502)

    CPE.groups.append(RequiredGroup(name="electives", credits="18"))

    e.add_to_group(CPE.groups[0], "^(?!.*(COP3502)).*^(COP3)")
    e.write(CPE)

    t = e.read_major("Computer Engineering")

    assert t.groups[0].courses == [DSA, COP3503]


def test_adding_critical_tracking():
    CPE.critical_tracking.extend([DSA, COP3503, COP3502])
    e.write(CPE)

    t = e.read_major("Computer Engineering")

    assert t.critical_tracking == [DSA, COP3503, COP3502]


def test_deleting_critical_tracking():
    CPE.critical_tracking.extend([DSA, COP3503, COP3502])
    e.write(CPE)

    t = e.read_major("Computer Engineering")
    t.critical_tracking.remove(DSA)
    e.write(t)

    t = e.read_major("Computer Engineering")
    assert t.critical_tracking == [COP3503, COP3502]


def test_adding_required():
    CPE.required.extend([DSA, COP3503, COP3502])
    e.write(CPE)

    t = e.read_major("Computer Engineering")

    assert t.required == [DSA, COP3503, COP3502]


def test_deleting_required():
    CPE.required.extend([DSA, COP3503, COP3502])
    e.write(CPE)

    t = e.read_major("Computer Engineering")
    t.required.remove(DSA)
    e.write(t)

    t = e.read_major("Computer Engineering")
    assert t.required == [COP3503, COP3502]


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    global e
    global CPE
    global COP3503
    global COP3502
    global DSA

    # stuff that happens before tests

    create_db_and_tables(sqlite_file_name)

    e = DB_Engine(sqlite_file_name)

    CPE = Major(name="Computer Engineering")

    COP3503 = Course(
        code="COP3503",
        name="Programming Fundamentals 2",
        description="Introduction to programming",
        credits=4,
    )

    COP3502 = Course(
        code="COP3502",
        name="Programming Fundamentals 1",
        description="Introduction to programming",
        credits=4,
    )

    DSA = Course(
        code="COP3530",
        name="DSA",
        description="Introduction to programming",
        credits=4,
    )

    yield  # tests happen here

    # everything that happens after all test

    del e
    os.remove(sqlite_file_name)


if __name__ == "__main__":
    pass
