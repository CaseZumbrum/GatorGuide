from GatorGuide.database.workflow.create import create_db_and_tables
from GatorGuide.database.db_engine import DB_Engine
from GatorGuide.database.models import Course, Major
import os
from pathlib import Path
import pytest
from sqlalchemy.exc import NoResultFound

sqlite_file_name = Path(__file__).parent.resolve().joinpath("./database.db")


def test_db_exists():
    assert os.path.exists(sqlite_file_name)


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
    pass
