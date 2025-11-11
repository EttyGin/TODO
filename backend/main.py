from fastapi import FastAPI
from routers import todo_router

app = FastAPI(title="Todo API")

app.include_router(todo_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)