from . import Base
from .course_has_student import course_has_student_table
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from models import course_has_student

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(16), nullable = False)
    second_name = Column(String(45), nullable = False)
    email = Column(String(255), nullable = False, unique = True)
    password = Column(String(32), nullable = False)
    create_time = Column(DateTime, default = func.now(), nullable = False)
    join_requests = relationship('JoinRequest', backref = 'student')
    courses = relationship('Course', secondary = course_has_student_table, back_populates = "students")