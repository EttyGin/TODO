from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import get_db
from app.schemas.todo import TodoCreate, TodoRead
from app.services import todo_service

router = APIRouter()

@router.get("/", response_model=List[TodoRead])
def read_todos(db: Session = Depends(get_db)):
    """Get all todos"""
    return todo_service.list_todos(db)

@router.post("/", response_model=TodoRead, status_code=201)
def create_todo(payload: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo"""
    return todo_service.add_todo(db, payload.title)

@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo by id"""
    success = todo_service.remove_todo(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
