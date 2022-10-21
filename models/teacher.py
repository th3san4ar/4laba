from . import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(16), nullable = False)
    second_name = Column(String(45), nullable = False)
    email = Column(String(255), nullable = False, unique = True)
    password = Column(String(32), nullable = False)
    create_time = Column(DateTime, default = func.now(), nullable = False)
    course = relationship('Course', backref = 'teacher')