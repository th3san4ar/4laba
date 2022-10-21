from . import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

course_has_student_table = Table(
    'course_has_student',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id'), primary_key = True), 
    Column('course_id', Integer, ForeignKey('course.id'), primary_key = True)
)