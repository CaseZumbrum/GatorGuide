import requests
from GatorGuide.database.models import Course, CorequisiteGroup

import GatorGuide.database.models as models
import pathlib
from GatorGuide.database.db_engine import DB_Engine

from sqlalchemy.exc import IntegrityError


def parse(pre: str) -> list[list[str]]:
    """parse a prerequisite string from the One.UF API

    Args:
        pre (str): string to be parsed

    Returns:
        list[list[str]]: prerequisites from the string. Those that are grouped together are "or".
        EX: [["COP3502", "COP3504"], ["COT3100"]] is equivalent to (COP3502 or COP3504) and COT3100
    """

    # remove parentheses, slashed, and periods
    pre = pre.replace("(", "").replace(")", "").replace(".", "").replace("/", " ")
    # split words into a list
    words = pre.split()
    prereq_group: list[list[str]] = []

    i = 0
    # iterate through all words
    while i < len(words) - 1:
        # if a word matches the code format
        if (
            words[i].isupper()
            and len(words[i]) == 3
            and len(words[i + 1]) == 4
            and words[i + 1].isnumeric()
        ):
            prereq_group.append([])
            prereq_group[-1].append(words[i] + words[i + 1])
            # attempt to find ORs in the string
            try:
                # while there is an or
                while words[i + 2] == "or":
                    # if the or is followed by a valid course code
                    if (
                        words[i + 3].isupper()
                        and len(words[i + 3]) == 3
                        and len(words[i + 4]) == 4
                        and words[i + 4].isnumeric()
                    ):
                        # add to the group
                        prereq_group[-1].append(words[i + 3] + words[i + 4])
                    i += 3

            except IndexError:
                pass
        i += 1
    return prereq_group

def parse_coreqs(pre: str) -> list[list[str]]:
    """Parse corequisite string from the One.UF API (same structure as parse())

    Args:
        pre (str): string to be parsed (contains prereqs and coreqs)

    Returns:
        list[list[str]]: corequisites grouped by 'or' conditions
    """

    # Normalize punctuation
    pre = pre.replace("(", "").replace(")", "").replace(".", "").replace("/", " ")
    pre = pre.replace(":", "").replace(";", "")

    words = pre.split()
    coreq_group: list[list[str]] = []

    i = 0
    reading_coreqs = False

    while i < len(words) - 1:
        # Start parsing after 'Coreq' or 'Corequisite'
        if words[i].lower() in ["coreq", "corequisite"]:
            reading_coreqs = True
            i += 1
            continue

        if reading_coreqs:
            if (
                words[i].isalpha()
                and len(words[i]) == 3
                and len(words[i + 1]) == 4
                and words[i + 1].isnumeric()
            ):
                coreq_group.append([])
                coreq_group[-1].append(words[i] + words[i + 1])
                try:
                    while words[i + 2].lower() == "or":
                        if (
                            words[i + 3].isalpha()
                            and len(words[i + 3]) == 3
                            and len(words[i + 4]) == 4
                            and words[i + 4].isnumeric()
                        ):
                            coreq_group[-1].append(words[i + 3] + words[i + 4])
                        i += 3
                except IndexError:
                    pass
        i += 1

    return coreq_group




def populate(engine: DB_Engine):
    """Populate the DB with One.UF API data

    Args:
        engine (DB_Engine): Database API
    """

    print("-----------------------")
    print("Deleting current Courses...")
    # wipe the database of all courses!
    courses_to_delete: list[Course] = engine.read_all_courses()
    for d in courses_to_delete:
        engine.delete(d)

    print("Done!")

    courses: list[Course] = []  # list of course objects
    course_json = []  # list of courses as dictionary, used for prequisite matching
    count = 0  # used to keep track of how many courses have been registered

    codes: set[str] = set()

    print("-----------------------")
    print("Finding courses...")
    terms = ["2248", "2251"]
    for term in terms:
        last_num = 0  # used by the one.uf api to get the next page of courses
        while True:
            # pull data from one.uf
            URL = f"https://one.uf.edu/apix/soc/schedule?ai=false&auf=false&category=CWSP&class-num=&course-code=&course-title=&cred-srch=&credits=&day-f=&day-m=&day-r=&day-s=&day-t=&day-w=&dept=&eep=&fitsSchedule=false&ge=&ge-b=&ge-c=&ge-d=&ge-h=&ge-m=&ge-n=&ge-p=&ge-s=&instructor=&last-control-number={last_num}&level-max=&level-min=&no-open-seats=false&online-a=&online-c=&online-h=&online-p=&period-b=&period-e=&prog-level=&qst-1=&qst-2=&qst-3=&quest=false&term={term}&wr-2000=&wr-4000=&wr-6000=&writing=false&var-cred=&hons=false"
            r = requests.get(url=URL)
            data = r.json()

            # if we have gotten to all of the courses
            if data[0]["RETRIEVEDROWS"] == 0:
                break

            # iterate through course JSONs
            for c in data[0]["COURSES"]:
                # filter out graduate level courses
                if c["sections"][0]["credits"] == "VAR" or int(c["code"][3]) >= 5:
                    continue
                elif c["code"] in codes:
                    continue
                else:
                    # create new Course object, add to the list
                    course_json.append(c)
                    courses.append(
                        Course(
                            code=c["code"],
                            name=c["name"],
                            description=c["description"],
                            credits=c["sections"][0]["credits"],
                        )
                    )
                    codes.add(c["code"])

            last_num = data[0]["LASTCONTROLNUMBER"]

    print("Adding prerequisites...")
    # add prerequisits to each course
    for i in range(len(course_json)):
        prereqs: list[models.PrequisiteGroup] = []

        # if a course has prequisits
        if course_json[i]["prerequisites"] != "":
            # get the codes for each prereq
            p = parse(course_json[i]["prerequisites"])
            # for each group of prereqs
            for group in p:
                # create a new PrerequisiteGroup object
                prereqs.append(models.PrequisiteGroup(courses=[]))
                # for each code in the group
                for code in group:
                    # find the corresponding course
                    course: models.Course | None = next(
                        (x for x in courses if x.code == code), None
                    )
                    # if the course is found, add it to the PrerequisiteGroup object
                    if course is not None:
                        prereqs[-1].courses.append(course)
        coreq_groups = parse_coreqs(course_json[i]["prerequisites"])
        if course_json[i]["code"] == "COT3100":
            print("RAW:", course_json[i]["prerequisites"])
            print("PARSED COREQS:", coreq_groups)
        coreqs: list[models.CorequisiteGroup] = []

        coreqs: list[models.CorequisiteGroup] = []
        for group in coreq_groups:
            coreq_group = models.CorequisiteGroup(courses=[])
            for code in group:
                course = next((x for x in courses if x.code == code), None)
                if course:
                    coreq_group.courses.append(course)
            if coreq_group.courses:
                coreqs.append(coreq_group)

        courses[i].prerequisites = prereqs
        courses[i].corequisites = coreqs
    # add the course + prereqs to the DB
    print("Writing to Database...")
    from sqlmodel import Session
    with Session(engine.engine) as s:
        s.add_all(courses)
        s.commit()
    for c in courses:
        count += 1
        # except IntegrityError as e:
        #     if c.code == "EEL4744C":
        #         print(e)
    print(f"Courses added: {count}")
    print("Done!")


if __name__ == "__main__":
    sqlite_file_name = (
        pathlib.Path(__file__).parent.resolve().joinpath("../database.db")
    )

    e = DB_Engine(sqlite_file_name)
    populate(e)