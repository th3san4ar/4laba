from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .teacher import Teacher
from .student import Student
from .join_request import JoinRequest
from .course import Course