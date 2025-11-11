"""
Business logic layer for Todo operations.
Handles validation, repository calls, and error handling.
"""

from sqlalchemy.orm import Session
from repositories.todo_repository import TodoRepository
from schemas.todo import TodoSchema


class TodoService:
    def __init__(self, db: Session):
        self.repo = TodoRepository(db)

    def get_all_todos(self):
        """Return all todos."""
        return self.repo.get_all()

    def get_todo_by_id(self, todo_id: int):
        """Return a todo by ID or raise error if missing."""
        todo = self.repo.get_by_id(todo_id)
        if not todo:
            raise ValueError(f"Todo with id {todo_id} not found")
        return todo

    def create_todo(self, todo_in: TodoSchema):
        """Create a new todo."""
        return self.repo.create(todo_in)

    def update_todo(self, todo_id: int, todo_in: TodoSchema):
        """Update an existing todo."""
        return self.repo.update(todo_id, todo_in)

    def delete_todo(self, todo_id: int):
        """Delete a todo."""
        return self.repo.delete(todo_id)
