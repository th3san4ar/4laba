from . import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique = True, nullable = False)
    users = relationship('User', backref = "role")