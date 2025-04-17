from pydantic import BaseModel


class PrerequisiteGroupResponse(BaseModel):
    id: int | None = None
    courses: list["CourseResponseNoPrereqs"]

    class Config:
        from_attributes = True


class CorequisiteGroupResponse(BaseModel):
    id: int | None = None
    courses: list["CourseResponseNoPrereqs"]

    class Config:
        from_attributes = True


class CourseResponse(BaseModel):
    id: int | None = None
    code: str
    name: str
    description: str
    credits: int
    prerequisites: list["PrerequisiteGroupResponse"]
    corequisites: list[CorequisiteGroupResponse]

    class Config:
        from_attributes = True


class CourseResponseNoPrereqs(BaseModel):
    id: int | None = None
    code: str
    name: str
    description: str
    credits: int

    class Config:
        from_attributes = True


class RequiredGroupResponse(BaseModel):
    id: int | None = None
    name: str
    credits: int
    courses: list[CourseResponseNoPrereqs]

    class Config:
        from_attributes = True


class MajorResponseNoRequired(BaseModel):
    id: int | None = None
    name: str

    class Config:
        from_attributes = True


class MajorResponse(BaseModel):
    id: int | None = None
    name: str
    critical_tracking: list[CourseResponseNoPrereqs]
    required: list[CourseResponseNoPrereqs]
    groups: list[RequiredGroupResponse]

    class Config:
        from_attributes = True


class SemesterResponse(BaseModel):
    id: int | None = None
    courses: list[CourseResponseNoPrereqs]

    class Config:
        from_attributes = True


class FourYearPlanResponse(BaseModel):
    id: int | None = None
    name: str
    major: MajorResponseNoRequired
    semesters: list[SemesterResponse]

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int | None = None
    name: str
    email: str
    plans: list[FourYearPlanResponse]

    class Config:
        from_attributes = True
