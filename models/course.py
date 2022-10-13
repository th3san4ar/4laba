from . import Base
from .course_has_user import course_has_user
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key = True)
    name = Column(String(45), unique = True, nullable = False)
    credits = Column(Integer, nullable = False)
    url = Column(String(45))
    join_requests = relationship('JoinRequest', backref = 'course')
    users = relationship('User', secondary = course_has_user, back_populates = "courses")