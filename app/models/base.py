from . import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

class BaseTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String(120), nullable=False, index=True)
    text = Column('text', String(1000), nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.datetime.utcnow)