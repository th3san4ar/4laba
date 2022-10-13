from . import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

course_has_user = Table(
    'course_has_user',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key = True), 
    Column('course_id', Integer, ForeignKey('course.id'), primary_key = True)
)