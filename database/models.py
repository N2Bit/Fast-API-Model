from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from .db import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False, index=True)
    description = Column(String(100))





