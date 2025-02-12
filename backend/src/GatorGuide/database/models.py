from sqlmodel import Field, Relationship, SQLModel


class MajorCriticalTrackingLink(SQLModel, table=True):
    """Link table between majors and their critical tracking courses"""

    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    major_id: int | None = Field(default=None, foreign_key="major.id", primary_key=True)


class PrerequisiteGroupCourseLink(SQLModel, table=True):
    """Link table between PrerequisiteGroup and their Courses"""

    prereq_group_id: int | None = Field(
        default=None, foreign_key="prequisitegroup.id", primary_key=True
    )
    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )


class CoursePrerequisiteGroupLink(SQLModel, table=True):
    """Link table between Courses and their PrerequisiteGroups"""

    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    prereq_group_id: int | None = Field(
        default=None, foreign_key="prequisitegroup.id", primary_key=True
    )


class MajorRequiredLink(SQLModel, table=True):
    """Link table between Majors and their Required Courses"""

    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    major_id: int | None = Field(default=None, foreign_key="major.id", primary_key=True)


class RequirementGroupsCourseLink(SQLModel, table=True):
    """Link table between RequirementGroups and their Courses"""

    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    group_id: int | None = Field(
        default=None, foreign_key="requiredgroup.id", primary_key=True
    )


class MajorRequiredGroupLink(SQLModel, table=True):
    """Link table between Majors and their RequirementGroups"""

    Major_id: int | None = Field(default=None, foreign_key="major.id", primary_key=True)
    group_id: int | None = Field(
        default=None, foreign_key="requiredgroup.id", primary_key=True
    )


class Course(SQLModel, table=True):
    """Object representing a single course

    Args:
        id (int, optional): Primary key of the table, do NOT pass this parameter in unless you are aware of the affect it will have. Defaults to None.
        code (str): Course code, should follow the UF course code format (ex: CEN3031)
        name (str): Course name, allows spaces and special characters
        description (str): Course description
        credits (int): number of credits the course is worth, if a course can be worth different amounts of credits, create several courses for it
        prerequisits (list[PrerequisitGroup]): prerequisits for the course
    """

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(index=True)
    name: str
    description: str
    credits: int
    prerequisites: list["PrequisiteGroup"] = Relationship(
        link_model=CoursePrerequisiteGroupLink
    )


class PrequisiteGroup(SQLModel, table=True):
    """Group used to store prerequisits for courses

    Args:
        id (int, optional): Primary key of the table, do NOT pass this parameter in unless you are aware of the affect it will have. Defaults to None.
        Courses (list[Course]): courses within the prerequisite group
    """

    id: int | None = Field(default=None, primary_key=True)
    courses: list[Course] = Relationship(link_model=PrerequisiteGroupCourseLink)


class Major(SQLModel, table=True):
    """Object representing a single major

    Args:
        id (int, optional): Primary key of the table, do NOT pass this parameter in unless you are aware of the affect it will have. Defaults to None.
        name (str): Major name, allows spaces and special characters
        critical_tracking (list[Course]): list of all critical tracking courses
        required (list[Course]): list of all required (non-critical tracking) courses
        groups (list[RequiredGroup]): list of all groups of requirements (ex: tech electives)
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str
    critical_tracking: list[Course] = Relationship(link_model=MajorCriticalTrackingLink)
    required: list[Course] = Relationship(link_model=MajorRequiredLink)
    groups: list["RequiredGroup"] = Relationship(link_model=MajorRequiredGroupLink)

    def print(self):
        """print data on the major"""
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
    """Object representing a group of required courses

    Args:
        id (int, optional): Primary key of the table, do NOT pass this parameter in unless you are aware of the affect it will have. Defaults to None.
        name (str): Group name, allows spaces and special characters (ex: tech electives)
        credits (int): number of credits this group requires
        courses (list[courses]): courses included in this group
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str
    credits: int
    courses: list[Course] = Relationship(link_model=RequirementGroupsCourseLink)
