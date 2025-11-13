# תחביר חדש (Pydantic v2)
from pydantic import BaseModel, ConfigDict

class TodoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int | None = None
    title: str
    description: str | None = None
    completed: bool = False