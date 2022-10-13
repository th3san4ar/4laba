from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .user import User
from .join_request import JoinRequest
from .course import Course
from .role import Role
from .course_has_user import course_has_user