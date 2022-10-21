from models import student
from . import Base
from .course_has_student import course_has_student_table
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key = True)
    name = Column(String(45), unique = True, nullable = False)
    credits = Column(Integer, nullable = False)
    url = Column(String(45))
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable = False)
    join_requests = relationship('JoinRequest', backref = 'course')
    students = relationship('Student', secondary = course_has_student_table, back_populates = "courses")