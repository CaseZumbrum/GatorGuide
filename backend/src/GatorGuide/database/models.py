from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

    

class MajorCriticalTrackingLink(SQLModel, table=True):
    course_id: int | None = Field(default=None, foreign_key="course.id", primary_key=True)
    major_id: int | None = Field(default=None, foreign_key="major.id", primary_key=True)

class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(index=True)
    name: str
    description: str
    # critical_tracking_for: list["Major"] = Relationship(back_populates="critical_tracking", link_model=MajorCriticalTrackingLink)


class Major(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    critical_tracking: list[Course] = Relationship(link_model=MajorCriticalTrackingLink)
    

