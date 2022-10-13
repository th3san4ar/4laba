from . import Base
from .course_has_user import course_has_user
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(16), nullable = False)
    second_name = Column(String(45), nullable = False)
    email = Column(String(255), nullable = False, unique = True)
    password = Column(String(32), nullable = False)
    create_time = Column(DateTime, default = func.now(), nullable = False)
    role_id = Column(Integer, ForeignKey('role.id'))
    join_requests = relationship('JoinRequest', backref = 'user')
    courses = relationship('Course', secondary = course_has_user, back_populates = "users")