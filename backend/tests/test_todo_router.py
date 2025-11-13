"""Unit tests for Todo router"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from fastapi import FastAPI
from sqlalchemy.orm import Session

from routers.todo_router import router
from services.todo_service import TodoService
from schemas.todo import TodoSchema

# יצירת app לטסטים
app = FastAPI()
app.include_router(router)
client = TestClient(app)


@pytest.fixture
def mock_db():
    """Mock של database session"""
    return MagicMock(spec=Session)


@pytest.fixture
def mock_todo_service():
    """Mock של TodoService"""
    return MagicMock(spec=TodoService)


@pytest.fixture
def sample_todos():
    """דוגמאות של todos"""
    return [
        TodoSchema(id=1, title="Learn FastAPI", description="Study FastAPI", completed=False),
        TodoSchema(id=2, title="Write tests", description="Unit tests", completed=True),
    ]


def test_get_todos(mock_db, mock_todo_service, sample_todos):
    """Test GET /todos/"""
    # הגדרת התנהגות ה-mock
    mock_todo_service.get_all_todos.return_value = sample_todos
    
    # Override של get_db ו-TodoService
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.get("/todos/")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert data[0]["title"] == "Learn FastAPI"
        assert data[1]["completed"] is True
        
        # ווידוא שהשירות נקרא
        mock_todo_service.get_all_todos.assert_called_once()


def test_get_todo_by_id_success(mock_db, mock_todo_service):
    """Test GET /todos/{todo_id} - success"""
    expected_todo = TodoSchema(id=1, title="Test Todo", description="Test", completed=False)
    mock_todo_service.get_todo_by_id.return_value = expected_todo
    
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.get("/todos/1")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["title"] == "Test Todo"
        
        mock_todo_service.get_todo_by_id.assert_called_once_with(1)


def test_get_todo_by_id_not_found(mock_db, mock_todo_service):
    """Test GET /todos/{todo_id} - not found"""
    mock_todo_service.get_todo_by_id.side_effect = ValueError("Todo not found")
    
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.get("/todos/999")
        
        assert response.status_code == 404
        assert "Todo not found" in response.json()["detail"]


def test_create_todo(mock_db, mock_todo_service):
    """Test POST /todos/"""
    new_todo = {"title": "New Todo", "description": "Description", "completed": False}
    created_todo = TodoSchema(id=1, **new_todo)
    
    mock_todo_service.create_todo.return_value = created_todo
    
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.post("/todos/", json=new_todo)
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "New Todo"
        assert data["id"] == 1
        
        # ווידוא שהשירות נקרא עם הפרמטרים הנכונים
        mock_todo_service.create_todo.assert_called_once()


def test_update_todo_success(mock_db, mock_todo_service):
    """Test PUT /todos/{todo_id} - success"""
    updated_data = {"title": "Updated", "description": "Updated desc", "completed": True}
    updated_todo = TodoSchema(id=1, **updated_data)
    
    mock_todo_service.update_todo.return_value = updated_todo
    
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.put("/todos/1", json=updated_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated"
        assert data["completed"] is True
        
        # ווידוא שהמתודה נקראה פעם אחת
        mock_todo_service.update_todo.assert_called_once()
        
        # בדיקה שהפרמטרים נכונים
        call_args = mock_todo_service.update_todo.call_args
        assert call_args[0][0] == 1  # todo_id
        
        # הפרמטר השני הוא TodoSchema object
        todo_arg = call_args[0][1]
        assert isinstance(todo_arg, TodoSchema)
        assert todo_arg.title == "Updated"
        assert todo_arg.description == "Updated desc"
        assert todo_arg.completed is True
def test_update_todo_not_found(mock_db, mock_todo_service):
    """Test PUT /todos/{todo_id} - not found"""
    updated_data = {"title": "Updated", "description": "Updated desc", "completed": True}
    mock_todo_service.update_todo.return_value = None
    
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.put("/todos/999", json=updated_data)
        
        assert response.status_code == 404
        assert "Todo not found" in response.json()["detail"]


def test_delete_todo_success(mock_db, mock_todo_service):
    """Test DELETE /todos/{todo_id} - success"""
    mock_todo_service.delete_todo.return_value = True
    
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.delete("/todos/1")
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}
        
        mock_todo_service.delete_todo.assert_called_once_with(1)


def test_delete_todo_not_found(mock_db, mock_todo_service):
    """Test DELETE /todos/{todo_id} - not found"""
    mock_todo_service.delete_todo.return_value = False
    
    with patch("routers.todo_router.get_db", return_value=mock_db), \
         patch("routers.todo_router.TodoService", return_value=mock_todo_service):
        
        response = client.delete("/todos/999")
        
        assert response.status_code == 404
        assert "Todo not found" in response.json()["detail"]