"""
Integration Tests for Todo API
"""


def test_get_empty_todos(client):
    """בדיקה שרשימת todos ריקה בהתחלה"""
    response = client.get("/todos/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo(client):
    """בדיקת יצירת todo בסיסי"""
    response = client.post("/todos/", json={
        "title": "Buy groceries",
        "description": "Milk, bread, eggs",
        "completed": False
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy groceries"
    assert "id" in data


def test_get_todo_by_id(client):
    """בדיקת קריאת todo לפי ID"""
    create_response = client.post("/todos/", json={
        "title": "Test Todo",
        "completed": False
    })
    todo_id = create_response.json()["id"]
    
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id


def test_get_todo_not_found(client):
    """בדיקה שקריאת todo שלא קיים מחזירה 404"""
    response = client.get("/todos/999")
    assert response.status_code == 404


def test_update_todo(client):
    """בדיקת עדכון todo"""
    create_response = client.post("/todos/", json={
        "title": "Original",
        "completed": False
    })
    todo_id = create_response.json()["id"]
    
    response = client.put(f"/todos/{todo_id}", json={
        "title": "Updated",
        "completed": True
    })
    
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


def test_delete_todo(client):
    """בדיקת מחיקת todo"""
    create_response = client.post("/todos/", json={
        "title": "To delete",
        "completed": False
    })
    todo_id = create_response.json()["id"]
    
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200