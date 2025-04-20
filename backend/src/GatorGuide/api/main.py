from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import pathlib
from GatorGuide.api.routes import courses, majors, users
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
import logging
from GatorGuide.config import ORIGINS


# do not log user password data
class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("/users/") == -1


app = FastAPI(title="GatorGuide API", version="1.0")

# mount sub-routes
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


app.openapi_schema = custom_openapi()

# Add CORS handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
