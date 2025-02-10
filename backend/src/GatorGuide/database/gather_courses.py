import requests
from pydantic.json import pydantic_encoder
from GatorGuide.database.models import Course

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import GatorGuide.database.models as models
import pathlib
from GatorGuide.database.parse_prereqs import parse

sqlite_file_name = pathlib.Path(__file__).parent.resolve().joinpath("./database.db")
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


last_num = 0  # used by the one.uf api to get the next page of courses

courses: list[Course] = []
course_json = []
count = 0  # used to keep track of how many courses have been registered
with Session(engine) as session:
    while True:
        URL = f"https://one.uf.edu/apix/soc/schedule?ai=false&auf=false&category=CWSP&class-num=&course-code=&course-title=&cred-srch=&credits=&day-f=&day-m=&day-r=&day-s=&day-t=&day-w=&dept=&eep=&fitsSchedule=false&ge=&ge-b=&ge-c=&ge-d=&ge-h=&ge-m=&ge-n=&ge-p=&ge-s=&instructor=&last-control-number={last_num}&level-max=&level-min=&no-open-seats=false&online-a=&online-c=&online-h=&online-p=&period-b=&period-e=&prog-level=&qst-1=&qst-2=&qst-3=&quest=false&term=2251&wr-2000=&wr-4000=&wr-6000=&writing=false&var-cred=&hons=false"

        r = requests.get(url=URL)

        data = r.json()

        # if we have gotten to all of the courses
        if data[0]["RETRIEVEDROWS"] == 0:
            break

        # iterate through course JSONs
        for c in data[0]["COURSES"]:
            # graduate level courses
            if c["sections"][0]["credits"] == "VAR" or int(c["code"][3]) >= 5:
                continue

            count += len(c["sections"])  # increment course counter

            # create new Course object, add to the database
            course_json.append(c)
            courses.append(
                Course(
                    code=c["code"],
                    name=c["name"],
                    description=c["description"],
                    credits=c["sections"][0]["credits"],
                )
            )

        last_num = data[0]["LASTCONTROLNUMBER"]
        print(f"COUNT: {count}")

    for c in course_json:
        prereqs: list[models.PrequisiteGroup] = []

        if c["prerequisites"] != "":
            p = parse(c["prerequisites"])
            for group in p:
                prereqs.append(models.PrequisiteGroup(courses=[]))
                for code in group:
                    course: models.Course | None = next(
                        (x for x in courses if x.code == code), None
                    )
                    if course is not None:
                        prereqs[-1].courses.append(course)
        if(c["code"] == "COP3503")
        session.add(
            Course(
                code=c["code"],
                name=c["name"],
                description=c["description"],
                credits=c["sections"][0]["credits"],
                prerequisites=prereqs,
            )
        )

    session.commit()
# with open("courses.json", "w") as f:
#     json.dump(courses, f, default=pydantic_encoder)
#     print(f"TOTAL COUNT: {count}")
