"""
Todo API routes.
Defines all endpoints related to Todo management.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import get_db
from schemas import TodoSchema
from services import TodoService

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/")
def get_todos(db: Session = Depends(get_db)):
    """Get all todos."""
    return TodoService(db).get_all_todos()


@router.get("/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a todo by its ID."""
    try:
        return TodoService(db).get_todo_by_id(todo_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/")
def create_todo(todo: TodoSchema, db: Session = Depends(get_db)):
    """Create a new todo."""
    return TodoService(db).create_todo(todo)


@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: TodoSchema, db: Session = Depends(get_db)):
    """Update an existing todo."""
    updated = TodoService(db).update_todo(todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo by its ID."""
    deleted = TodoService(db).delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"ok": True}
