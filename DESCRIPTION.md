Project summary and brief explanations

Backend (backend/app)

- core/database.py: SQLAlchemy engine, session and Base.
- models/todo.py: ORM model `Todo` with id, title, completed.
- schemas/todo.py: Pydantic schemas `TodoCreate` and `TodoRead` used for validation/serialization.
- repositories/todo_repo.py: Database operations: get_all, create, delete. Single responsibility: direct DB access.
- services/todo_service.py: Business logic layer. Calls repository functions; here it's thin but exists to separate concerns.
- api/dependencies.py: `get_db` dependency that yields a DB session for routes.
- api/routes/todos.py: FastAPI router exposing three endpoints: GET /todos, POST /todos, DELETE /todos/{id}.
- main.py: FastAPI app instance, registers router, ensures tables are created on startup.

Frontend (frontend)

- package.json / tsconfig.json: Vite + TypeScript setup. Run `npm install` then `npm run dev`.
- index.html: app root and Vite entry.
- src/main.tsx: React entry point, renders `<App/>`.
- src/App.tsx: Top-level layout.
- src/pages/TodosPage.tsx: Page to list, add and delete todos. Uses `useTodos` hook.
- src/components/TodoItem.tsx: Presentational component for a todo item and delete button.
- src/services/api.ts: Axios wrapper calling `http://localhost:8000/todos` for fetch/create/delete.
- src/hooks/useTodos.ts: Custom hook that loads todos, exposes add/delete/refetch.
- src/types.ts: TypeScript types for Todo DTOs.
- src/style.css: Minimal styling.

Run instructions

- Backend: cd backend; python -m venv .venv; .venv\Scripts\Activate (PowerShell: .\.venv\Scripts\Activate.ps1); pip install -r requirements.txt; uvicorn app.main:app --reload --port 8000
- Frontend: cd frontend; npm install; npm run dev (runs at http://localhost:5173)

Notes

- Backend uses sync SQLAlchemy and a simple SQLite file `todos.db` in the backend folder.
- API base URL: http://localhost:8000/todos
- Frontend expects backend to be running. CORS: for local development you may enable CORS in FastAPI if needed (not included here for brevity). To enable CORS, install `fastapi[all]` or `starlette` and add middleware.

Next steps (optional):

- Add CORS middleware in backend if calling from browser causes CORS errors.
- Add validation, edit/complete endpoints, and basic tests.
