"""
Repository layer for Todo model.
Handles database operations (CRUD) for Todo items.
"""

from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import TodoSchema


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        """Return all todos."""
        return self.db.query(Todo).all()

    def get_by_id(self, todo_id: int):
        """Return a single todo by ID."""
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def create(self, todo_data: TodoSchema):
        """Create a new todo."""
        todo = Todo(**todo_data.model_dump(exclude_unset=True))
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def update(self, todo_id: int, todo_data: TodoSchema):
        """Update an existing todo."""
        todo = self.get_by_id(todo_id)
        if not todo:
            return None

        for key, value in todo_data.model_dump(exclude_unset=True).items():
            setattr(todo, key, value)

        self.db.commit()
        self.db.refresh(todo)
        return todo

    def delete(self, todo_id: int):
        """Delete a todo by ID."""
        todo = self.get_by_id(todo_id)
        if not todo:
            return None
        self.db.delete(todo)
        self.db.commit()
        return todo
