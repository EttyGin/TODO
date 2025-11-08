from sqlalchemy.orm import Session
from app.repositories import todo_repo


def list_todos(db: Session):
    return todo_repo.get_all(db)


def add_todo(db: Session, title: str):
    return todo_repo.create(db, title)


def remove_todo(db: Session, todo_id: int):
    return todo_repo.delete(db, todo_id)
