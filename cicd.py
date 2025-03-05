from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
import pathlib
import os
import subprocess
import atexit
from GatorGuide import config

app = FastAPI()

origins = ["*"]

SERVER_PATH = str(
    pathlib.Path(__file__)
    .parent.resolve()
    .joinpath("./backend/src/GatorGuide/api/main.py")
)

BUILD_PATH = str(pathlib.Path(__file__).parent.resolve().joinpath("./frontend"))

# create log folder if it does not exist

if not os.path.isdir(pathlib.Path(__file__).parent.resolve().joinpath("./logs")):
    os.mkdir(pathlib.Path(__file__).parent.resolve().joinpath("./logs"))

API_LOG = open("./logs/api.log", "a")
NPM_BUILD_LOG = open("./logs/build.log", "a")
GIT_LOG = open("./logs/git.log", "a")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

session = subprocess.Popen('exec echo "starting server"', stdout=API_LOG, shell=True)


def close_logs():
    API_LOG.close()
    NPM_BUILD_LOG.close()
    GIT_LOG.close()


def build_and_host():
    global session
    print("--------------")
    print("Killing existing server...")
    session.kill()

    print("--------------")
    print("Pulling most recent files...")
    subprocess.call(
        "git pull",
        stdout=GIT_LOG,
        stderr=GIT_LOG,
        shell=True,
    )

    print("--------------")
    print("Building react...")
    subprocess.call(
        f"cd {BUILD_PATH}; npm run build",
        stdout=NPM_BUILD_LOG,
        stderr=NPM_BUILD_LOG,
        shell=True,
    )

    print("--------------")
    print("Starting FastApi server...")
    session = subprocess.Popen(
        f"exec fastapi run --port {config.PORT} {str(SERVER_PATH)}",
        stdout=API_LOG,
        stderr=API_LOG,
        shell=True,
    )


build_and_host()
atexit.register(close_logs)


@app.get("/")
async def get_build(passkey: str, response: Response):
    if passkey == config.CICD_PASSKEY:
        build_and_host()
        response.status_code = status.HTTP_200_OK
        return {"Build": "Succeeded"}
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"Build": "Failed due to faulty passkey"}
