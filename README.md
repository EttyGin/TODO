https://chatgpt.com/share/6913bcb6-998c-8011-a626-cb9755317c42 fs
https://chatgpt.com/share/6913c082-8e78-8011-be29-d955e50f9b34 ib 

# 🧠 Project Structure Overview – Backend (FastAPI)

פרויקט זה הוא שרת Backend מבוסס **FastAPI**, הבנוי בארכיטקטורה מודולרית לפי עקרונות הפרדה ברורה בין שכבות:
- **Routers** – ניהול הנתיבים (Endpoints)
- **Services** – לוגיקה עסקית
- **Repositories** – גישה ל־Database
- **Schemas / Models** – מבני נתונים
- **Core** – הגדרות מערכת ומיגרציות
- **Main** – נקודת הכניסה לאפליקציה

---

## 📂 תיקיות וקבצים

### `main.py`
נקודת הכניסה הראשית של היישום.  
מכיל את יצירת מופע FastAPI, חיבור ל־DB, טעינת ה־Routers ורישום middlewares במידת הצורך.

---

### `core/`
מכיל את הרכיבים הבסיסיים של האפליקציה.

- **`config.py`** – קריאת משתני סביבה והגדרות כלליות (כגון URI של ה־DB).  
- **`db.py`** – יצירת חיבור למסד הנתונים (SQLAlchemy Engine, Session).  
- **`migrations/`** – ספריית Alembic לניהול מיגרציות DB:
  - `env.py` – קובץ תצורה של Alembic.
  - `script.py.mako` – תבנית ליצירת מיגרציות חדשות.
  - `versions/` – קבצים אוטומטיים עם שינויים בסכמת הנתונים.
  - `README` – קובץ ברירת מחדל שנוצר ע"י Alembic.

---

### `models/`
מכיל את מודלי הנתונים שמייצגים טבלאות במסד הנתונים (ORM Models).

- **`todo.py`** – הגדרה של טבלת Todos עם שדות (`id`, `title`, `description`, `completed` וכו').  
- כל מודל יורש מ־`Base` של SQLAlchemy ומקושר ל־DB דרך `core/db.py`.

---

### `schemas/`
מכיל את ה־Pydantic Schemas – מבני הנתונים המוחזרים או מתקבלים מה־API.

- **`todo.py`** – מגדיר את המודלים הלוגיים לתקשורת JSON בין השרת ללקוח (`TodoCreate`, `TodoUpdate`, `TodoResponse`).

---

### `repositories/`
שכבת הגישה למסד הנתונים.  
אחראית על כל אינטראקציה עם ה־DB (CRUD Operations).

- **`todo_repository.py`** – כולל פונקציות כמו `get_todos`, `create_todo`, `delete_todo` וכו’.  
  **שכבה זו אינה יודעת דבר על ה־API או הלוגיקה העסקית** – רק על הנתונים עצמם.

---

### `services/`
השכבה העסקית (Business Logic).  
מקשרת בין ה־Routers ל־Repositories, ומבצעת ולידציות, טרנספורמציות או תנאים לוגיים.

- **`todo_service.py`** – עוטף את הקריאות ל־Repository ומנהל את התהליך העסקי (למשל: אימות נתונים, החזרת תוצאות או חריגות).

---

### `routers/`
מכיל את הגדרת ה־Endpoints של ה־API.  
בכל קובץ Router יש קריאות HTTP (GET, POST, PUT, DELETE) שמתקשרות עם השירותים (`services`).

- **`todo_router.py`** – מגדיר את נקודות הקצה לעבודה עם Todos (לדוגמה: `/todos`, `/todos/{id}`).

---

### `db/`
תיקייה נפרדת המכילה תצורות למסד הנתונים.

---

### `alembic.ini`
קובץ ההגדרות הראשי של Alembic.  
מגדיר את מיקום התצורה (`core/migrations`) ואת URI של מסד הנתונים בזמן הרצת מיגרציות.

---
🧩 מיגרציות עם Alembic
יצירת מיגרציה חדשה
alembic revision --autogenerate -m "create todos table"

החלת מיגרציות על בסיס הנתונים
alembic upgrade head

בדיקת מצב המיגרציות