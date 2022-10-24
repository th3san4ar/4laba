from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

course_has_student_table = Table(
    'course_has_student',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id'), primary_key = True), 
    Column('course_id', Integer, ForeignKey('course.id'), primary_key = True)
)

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

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(16), nullable = False)
    second_name = Column(String(45), nullable = False)
    email = Column(String(255), nullable = False, unique = True)
    password = Column(String(32), nullable = False)
    create_time = Column(DateTime, default = func.now(), nullable = False)
    course = relationship('Course', backref = 'teacher')

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key = True)
    name = Column(String(45), unique = True, nullable = False)
    credits = Column(Integer, nullable = False)
    url = Column(String(45))
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable = False)
    join_requests = relationship('JoinRequest', backref = 'course')
    students = relationship('Student', secondary = course_has_student_table, back_populates = "courses")

class JoinRequest(Base):
    __tablename__ = 'join_request'
    id = Column(Integer, primary_key = True)
    status = Column(Enum('accepted', 'denied', 'unprocessed'), nullable = False)
    create_time = Column(DateTime, default = func.now(), nullable = False)
    student_id = Column(Integer, ForeignKey('student.id'), nullable = False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable = False)
