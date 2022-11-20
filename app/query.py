from sqlalchemy import create_engine
from sqlalchemy.orm import session
from app.models import *
engine = create_engine("mysql+pymysql://root:21805Sasha_@localhost/school", echo = True)
Session = session(bind=engine)
session = Session()

teacher1 = Teacher(
    first_name = "Joe",
    second_name = "Doe",
    email = 'joedoe@example.com',
    password = '1234'
)

teacher2 = Teacher(
    first_name = "Rack",
    second_name = "Back",
    email = 'rackback@example.com',
    password = '1234'
)

student1 = Student(
    first_name = "Jack",
    second_name = "Rack",
    email = 'jackrack@example.com',
    password = '1234'
)

student2 = Student(
    first_name = "Jim",
    second_name = "Tall",
    email = 'jimtall@example.com',
    password = '1234'
)

course1 = Course(
    name = 'Programming',
    credits = 10,
    teacher = teacher1,
    students = [student1, student2]
)

course2 = Course(
    name = 'Math',
    credits = 15,
    teacher = teacher2,
    students = [student1, student2]
)

join_request1 = JoinRequest(
    status = "denied",
    student = student1,
    course = course1
)

join_request2 = JoinRequest(
    status = "unprocessed",
    student = student2,
    course = course2
)

session.add_all(
    [
        join_request1,
        join_request2
    ]
)
session.commit()