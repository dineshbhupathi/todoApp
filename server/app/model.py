from .database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func, ForeignKey, Table, MetaData, PickleType


class Todo(Base):
    __tablename__ = "Todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250), nullable=True)
    description = Column(Text, nullable=True)
