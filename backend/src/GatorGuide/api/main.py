from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import pathlib
from GatorGuide.api.routes import courses, majors, users

app = FastAPI(title="GatorGuide API", version="1.0")

app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(majors.router, prefix="/majors", tags=["Majors"])
app.include_router(users.router, prefix="/users", tags=["Users"])


# mount frontend
app.mount(
    "/",
    StaticFiles(
        directory=pathlib.Path(__file__)
        .parent.resolve()
        .joinpath("../../../../frontend/dist"),
        html=True,
    ),
    name="site",
)
