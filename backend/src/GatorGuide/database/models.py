from sqlmodel import Field, Relationship, SQLModel


class MajorCriticalTrackingLink(SQLModel, table=True):
    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    major_id: int | None = Field(default=None, foreign_key="major.id", primary_key=True)


class PrerequisiteGroupCourseLink(SQLModel, table=True):
    prereq_group_id: int | None = Field(
        default=None, foreign_key="prequisitegroup.id", primary_key=True
    )
    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )


class CoursePrerequisiteGroupLink(SQLModel, table=True):
    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    prereq_group_id: int | None = Field(
        default=None, foreign_key="prequisitegroup.id", primary_key=True
    )


class MajorRequiredLink(SQLModel, table=True):
    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    major_id: int | None = Field(default=None, foreign_key="major.id", primary_key=True)


class RequirementGroupsCourseLink(SQLModel, table=True):
    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    group_id: int | None = Field(
        default=None, foreign_key="requiredgroup.id", primary_key=True
    )


class MajorRequiredGroupLink(SQLModel, table=True):
    Major_id: int | None = Field(default=None, foreign_key="major.id", primary_key=True)
    group_id: int | None = Field(
        default=None, foreign_key="requiredgroup.id", primary_key=True
    )


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(index=True)
    name: str
    description: str
    credits: int
    prerequisites: list["PrequisiteGroup"] = Relationship(
        link_model=CoursePrerequisiteGroupLink
    )


class PrequisiteGroup(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    courses: list[Course] = Relationship(link_model=PrerequisiteGroupCourseLink)


class Major(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    critical_tracking: list[Course] = Relationship(link_model=MajorCriticalTrackingLink)
    required: list[Course] = Relationship(link_model=MajorRequiredLink)
    groups: list["RequiredGroup"] = Relationship(link_model=MajorRequiredGroupLink)

    def print(self):
        print("-------------------")
        print(f"Name: {self.name}")
        print("-------------------")
        print("Critical Tracking")
        for c in self.critical_tracking:
            print(f"\t{c.name}")
        print("-------------------")
        print("Required")
        for c in self.required:
            print(f"\t{c.name}")
        print("-------------------")
        print("Groups")
        for g in self.groups:
            print(f"\t{g.name} : {g.credits}")
            for c in g.courses:
                print(f"\t\t{c.name}")


class RequiredGroup(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    credits: int
    courses: list[Course] = Relationship(link_model=RequirementGroupsCourseLink)
