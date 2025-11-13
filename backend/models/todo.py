"""
Todo model definition.
Defines the SQLAlchemy ORM mapping for the Todo table.
"""
from sqlalchemy import Column, Integer, String, Boolean
from core.db import Base  # ← ייבא את ה-Base מ-core/db.py!

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)