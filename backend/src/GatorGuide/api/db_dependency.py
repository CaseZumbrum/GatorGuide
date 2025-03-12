from GatorGuide.database.db_engine import DB_Engine
from pathlib import Path

# Provide the correct database path (update this if necessary)
DB_PATH = Path(__file__).parent.resolve().joinpath("../database/database.db")


db_engine = DB_Engine(DB_PATH)


def get_db():
    return db_engine
