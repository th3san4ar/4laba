from . import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func

class JoinRequest(Base):
    __tablename__ = 'join_request'
    id = Column(Integer, primary_key = True)
    status = Column(Enum('accepted', 'denied', 'unprocessed'), nullable = False)
    create_time = Column(DateTime, default = func.now(), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    course_id = Column(Integer, ForeignKey('course.id'))