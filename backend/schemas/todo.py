from pydantic import BaseModel

class TodoSchema(BaseModel):
    id: int | None = None
    title: str
    description: str | None = None
    completed: bool = False

    class Config:
        from_attributes = True