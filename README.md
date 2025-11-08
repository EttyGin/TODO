# Fullstack To-Do List (FastAPI + React + TypeScript)

This workspace contains a small educational fullstack To-Do application.

- Backend: FastAPI + SQLAlchemy + SQLite (runs on port 8000)
- Frontend: React + TypeScript (Vite) + Axios (runs on port 5173)

This README explains exactly how to set up and run the project from scratch on Windows PowerShell, and how to run both backend and frontend together.

Prerequisites

- Python 3.10+ (or any supported version)
- Node.js & npm
- Git (optional)

Quick outline

1. Install backend Python deps and create a virtual environment
2. Install frontend npm deps
3. Run backend (uvicorn)
4. Run frontend (vite dev server)
5. Or run both together using the provided PowerShell script `run-all.ps1`

Detailed steps (PowerShell)

1. Backend: create venv, install deps, run server

```powershell
cd C:\Users\1\TODOLIST\backend
python -m venv .venv
# If using PowerShell (default), run:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# Start backend on port 8000
uvicorn app.main:app --reload --port 8000
```

When the backend first starts it will create the SQLite database file `todos.db` inside the `backend` folder.

2. Frontend: install and run Vite dev server

```powershell
cd C:\Users\1\TODOLIST\frontend
npm install
npm run dev
```

This will start the frontend at `http://localhost:5173` and it will call the API at `http://localhost:8000/todos`.

3. Run both together (single command)

There is a helper PowerShell script at the repository root: `run-all.ps1` which opens two new PowerShell windows — one for the backend and one for the frontend — and runs the dev servers there. Use this after you created the Python venv and installed frontend deps at least once.

```powershell
cd C:\Users\1\TODOLIST
# Make sure you've already created the venv and installed pip & npm deps once
.\run-all.ps1
```

If you prefer to run both together on Mac/Linux, there is also a bash script named `start-all.sh` in the project root that attempts to open new terminal windows on macOS and Linux and run the backend and frontend. Example usage:

```bash
cd /path/to/TODOLIST
./start-all.sh
```

Note: The script tries to use `Terminal.app` on macOS and several common terminals on Linux (gnome-terminal, konsole, x-terminal-emulator). If no suitable terminal is found, it will run the processes in the background in the same terminal.

Notes & troubleshooting

- If you get CORS errors in the browser, enable CORS in the backend (see `backend/README.md` for a small snippet).
- If `uvicorn` is not found after activating the venv, ensure `pip install -r requirements.txt` completed without errors and that the virtual environment is activated.
- The `run-all.ps1` script assumes the venv folder is `.venv` under `backend`.

See `backend/README.md` and `frontend/README.md` for the platform-specific step-by-step instructions and examples.

---

הוראות בעברית — איך להריץ מהתחלה (PowerShell ב-Windows)

1. דרישות מוקדמות

- התקן Python 3.10+
- התקן Node.js + npm

2. קונפיגורציה והרצה של ה-backend

```powershell
cd C:\Users\1\TODOLIST\backend
python -m venv .venv
# הפעלת ה-venv ב-PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

3. קונפיגורציה והרצה של ה-frontend

```powershell
cd C:\Users\1\TODOLIST\frontend
npm install
npm run dev
```

4. להריץ את שניהם ביחד

סקריפט עוזר בשם `run-all.ps1` נמצא בתיקיית השורש. לאחר שביצעת פעם אחת את יצירת ה-venv והתקנת התלויות, פשוט הרץ:

```powershell
cd C:\Users\1\TODOLIST
.\run-all.ps1
```

הסקריפט יפתח שתי חלונות PowerShell נפרדים: אחד ל-backend (uvicorn) ואחד ל-frontend (vite).

אם תרצה שאוסיף גם קובץ `start-all` אחר (ל-Mac/Linux) או אוטומציה אחרת, תגיד לי ואוסיף.
