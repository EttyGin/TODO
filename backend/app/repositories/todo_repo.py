from sqlalchemy.orm import Session
from app.models.todo import Todo


def get_all(db: Session):
    return db.query(Todo).order_by(Todo.id.desc()).all()


def create(db: Session, title: str):
    todo = Todo(title=title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def delete(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False
