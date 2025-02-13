# GatorGuide

## Build

- Backend
  - ```
      cd backend
      python -m venv .venv
      ./.venv/Scipts/Activate
      pip install -e .
    ```
- Frontend
  - ```
      cd frontend
      npm install .
    ```

## Build the docs
  - Be in the python virtual environment created during build
  - ```
      cd backend
      pip install -r requirements.dev.txt
      ./docs/make.bat html
    ```
  - Open (or serve) docs/build/index.html
