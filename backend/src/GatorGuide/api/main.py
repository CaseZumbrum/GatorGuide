from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import pathlib
from GatorGuide.api.routes import courses, majors, users
from fastapi.openapi.utils import get_openapi

app = FastAPI(title="GatorGuide API", version="1.0")

app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(majors.router, prefix="/majors", tags=["Majors"])
app.include_router(users.router, prefix="/users", tags=["Users"])

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    app.openapi_schema = get_openapi(
        title="GatorGuide API",
        version="1.0",
        description="API for managing majors",
        routes=app.routes,
    )
    return app.openapi_schema

app.openapi = custom_openapi

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
