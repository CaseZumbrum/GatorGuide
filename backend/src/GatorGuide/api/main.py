from fastapi import FastAPI
from GatorGuide.api.routes import courses, majors, users

app = FastAPI(title="GatorGuide API", version="1.0")

app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(majors.router, prefix="/majors", tags=["Majors"])
app.include_router(users.router, prefix="/users", tags=["Users"])

# Root endpoint (for testing purposes)
@app.get("/")
def root():
    return {"message": "Welcome to GatorGuide API"}
