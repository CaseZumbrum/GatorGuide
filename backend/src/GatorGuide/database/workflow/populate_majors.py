from GatorGuide.database.models import (
    Major,
    RequiredGroup,
)
import pathlib
from GatorGuide.database.db_engine import DB_Engine


def populate(engine: DB_Engine):
    """Populate the majors

    Args:
        engine (DB_Engine): Database API
    """

    # COMPUTER ENGINEERING
    # https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CPE_BSCO/#criticaltrackingtext
    print("-----------------------")
    print("Adding Computer Engineering...")
    CPE = Major(
        name="Computer Engineering",
    )

    # Required Courses
    CPE.required.append(engine.read_course("CDA3101"))
    CPE.required.append(engine.read_course("CEN3031"))
    CPE.required.append(engine.read_course("COP3502C"))
    CPE.required.append(engine.read_course("COP3503C"))
    CPE.required.append(engine.read_course("COP3530"))
    CPE.required.append(engine.read_course("COT3100"))
    CPE.required.append(engine.read_course("EEL3701C"))
    CPE.required.append(engine.read_course("EEL4744C"))
    CPE.required.append(engine.read_course("ENC3246"))

    # Critical Tracking
    CPE.critical_tracking.append(engine.read_course("MAC2311"))
    CPE.critical_tracking.append(engine.read_course("MAC2312"))
    CPE.critical_tracking.append(engine.read_course("MAC2313"))
    CPE.critical_tracking.append(engine.read_course("MAP2302"))
    CPE.critical_tracking.append(engine.read_course("PHY2048"))
    CPE.critical_tracking.append(engine.read_course("PHY2049"))

    # CPE Design Courses
    CPE.groups.append(
        RequiredGroup(
            name="CpE Design 1",
            credits=3,
            courses=[engine.read_course("CEN3907C"), engine.read_course("EGN4951")],
        )
    )
    CPE.groups.append(
        RequiredGroup(
            name="CpE Design 2",
            credits=3,
            courses=[engine.read_course("CEN4908C"), engine.read_course("EGN4952")],
        )
    )

    # Technical Electives
    CPE_TECH_ELECTIVES = RequiredGroup(name="Technical Electives", credits=18)

    engine.add_to_group(
        CPE_TECH_ELECTIVES,
        "^(?!.*(CIS4940|CIS4949|EEL4837|EEL4948|EEL4949|CIS4914|EEL4924C|CDA3101|CEN3031|COP3502C|COP3503C|COP3530|COT3100|EEL3701C|EEL4744C|ENC3246|MAC2311|MAC2312|MAC2313|MAP2302|PHY2048|PHY2049)).*^(EEL4|COP4|MHF4|MAC4|STA4|PHY3|PHY4|PHZ3|PHZ4|EEE3308C|EEE3396|EEE3773|EEL3112|EEL3211C|EEL3402|EEL3472|EEL3850|CAP3020|CAP3027)",
    )

    CPE_ENRICHMENT_ELECTIVES = RequiredGroup(name="Enrichment Electives", credits=7)

    engine.add_to_group(
        CPE_ENRICHMENT_ELECTIVES,
        "^(?!.*(CIS|COP|MHF|MAC|STA|PHY)).*^(\w{3}4|\w{3}3)",
    )

    CPE.groups.append(CPE_TECH_ELECTIVES)
    CPE.groups.append(CPE_ENRICHMENT_ELECTIVES)

    engine.write(CPE)
    print("Done!")


if __name__ == "__main__":
    sqlite_file_name = (
        pathlib.Path(__file__).parent.resolve().joinpath("../database.db")
    )
    e = DB_Engine(sqlite_file_name)
    populate(e)
