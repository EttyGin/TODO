from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import todos

# Import models so they are registered in SQLAlchemy metadata
from app.models import todo  # noqa: F401

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")

app.include_router(todos.router, prefix="/todos", tags=["todos"])


@app.get("/")
def root():
    return {"message": "Todo API. Use /todos"}
