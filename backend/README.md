# Backend (FastAPI)

Run backend (from the `backend` folder):

1. Create a virtual environment (recommended) and activate it.

2. Install dependencies:

   pip install -r requirements.txt

3. Start the server:

   uvicorn app.main:app --reload --port 8000

The API base is `http://localhost:8000/todos`.

Structure:

- app/core: database setup
  This is intentionally small and clear for educational purposes.

````markdown
# Backend (FastAPI)

Run backend (from the `backend` folder). The instructions below are tailored for Windows PowerShell.

1. Create a virtual environment and install dependencies

```powershell
cd C:\Users\1\TODOLIST\backend
python -m venv .venv
# Activate the venv in PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
````

2. Start the server (dev)

```powershell
# from the same activated shell
uvicorn app.main:app --reload --port 8000
```

API base URL: `http://localhost:8000/todos`

Structure (short):

- `app/core`: database setup
- `app/models`: SQLAlchemy ORM models
- `app/schemas`: Pydantic schemas for request/response
- `app/repositories`: DB operations (single responsibility)
- `app/services`: business logic
- `app/api`: FastAPI routes and dependencies
- `app/main.py`: application instance and DB table creation

Notes

- When you run the backend for the first time `todos.db` (SQLite) will be created in the `backend` folder.
- If you need browser access from `http://localhost:5173` (frontend) you may need to enable CORS. Add this snippet to `app/main.py` near the FastAPI instantiation if needed:

```py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:5173"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)
```

This backend uses synchronous SQLAlchemy and is intentionally simple for learning.

```

```
