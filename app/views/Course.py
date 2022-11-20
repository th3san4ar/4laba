from flask import *
from marshmallow import *
import app.models as models
from werkzeug.security import generate_password_hash
from ..db import session_factory
from ..models import Course, update,Teacher,Student,course_has_student_table
from ..validation_models import CourseSchema,StudentSchema,JoinRequest

course_bp = Blueprint('course', __name__, url_prefix='/Courses')


@course_bp.get('/')
def get_courses():
    with session_factory() as session:
        course = session.query(Course).all()
    return CourseSchema(many=True).dumps(course)


# @course_bp.post('/')
# def create_course():
#     try:
#         course = CourseSchema().load(request.get_json())
#     except:
#         abort(Response('Invalid input', 400))
#     with session_factory() as session:
#         if session.query(Course).filter_by(name=course.name).first() is not None:
#             abort(Response('Invalid input', 400))
#         session.add(course)
#         session.commit()
#         id = course.id
#     return {'id': id}, 201

@course_bp.post('/')
def create_course():
    try:
        course = CourseSchema().load(request.get_json())
    except:
        abort(Response('Invalid input', 400))
    with session_factory() as session:
        if session.query(Course).filter_by(url = course.url).first() is not None:
            abort(Response('This url is already taken', 400))

        if session.query(Teacher).filter_by(id = course.teacher_id).first()is None:
            abort(Response('There is no teacher with this teacher_id', 400))

        if session.query(Course).filter_by(teacher_id = course.teacher_id).first() is not None:
            abort(Response('This teacher has course already', 400))
        session.add(course)
        session.commit()
        id = course.id
    return {'id': id}, 201


@course_bp.get('/<int:id>')
def get_course(id):
    with session_factory() as session:
        course = session.query(Course).filter_by(id = id).first()
    if course == None:
        abort(Response('Course not found', 404))
    return CourseSchema().dumps(course), 200

@course_bp.put('/<int:id>')
def update_course(id):
    try:
        updated = CourseSchema().load(request.get_json())
    except:
        abort(Response('1Invalid input', 400))
    with session_factory() as session:
        course = session.query(Course).filter_by(id = id).first()
        if course is None:
            abort(Response('Course not found', 404))
        if session.query(Course).filter_by(url = updated.url).first() is not None:
            abort(Response('Wrong email', 400))
        if session.query(Teacher).filter_by(id = updated.teacher_id).first() is None:
            abort(Response('There is no teacher with this teacher_id', 400))
        if session.query(Course).filter_by(teacher_id = updated.teacher_id).first() is not None:
            abort(Response('This teacher has course already', 400))
        #check if course name is unique
        if session.query(Course).filter_by(name = updated.name).first() is not None:
            abort(Response('Course name is not unique', 400))
        course.name = updated.name
        course.credits = updated.credits
        course.url = updated.url
        course.teacher_id = updated.teacher_id
        session.commit()
    return Response('Course updated', 200)

@course_bp.delete('/<int:id>')
def delete_course(id):
    with session_factory() as session:
        course = session.query(Course).filter_by(id = id).first()
        if course is None:
            abort(Response('Course not found', 404))
        session.delete(course)
        session.commit()
    return Response('Course deleted', 200)

#http://127.0.0.1:5000/Courses/add_student/1?student_id=4
# @course_bp.post('/add_student/<int:id>')
# def add_student_to_course(id):
#     with session_factory() as session:
#         course = session.query(Course).filter_by(id=id).first()
#         student=session.query(Student).filter_by(id=request.args.get('student_id')).first()
#         course.students.append(student)
#         session.commit()
#     return Response('Student added', 201)

@course_bp.post('/add_student/<int:id>')
def add_student_to_course(id):
    with session_factory() as session:
        course = session.query(Course).filter_by(id=id).first()
        student=session.query(Student).filter_by(id=request.args.get('student_id')).first()
        count = session.query(course_has_student_table).filter_by(course_id = id).count()
        if count > 5:
            abort(Response('Course has 5 students already', 400))
        if course is None:
            abort(Response('Course not found', 404))
        if student is None:
            abort(Response('Student not found', 404))
        course.students.append(student)
        session.commit()
    return Response('Student added', 201)

#Переробити і перевірити
@course_bp.post('/join/<int:id>')
def send_request(id):
    try:
        course = JoinRequest().load(request.get_json())
    except:
        abort(Response('Invalid input', 400))
    with session_factory() as session:
        course = session.query(Course).filter_by(id = id).first()
        if course is None:
            abort(Response('Course not found', 404))
        student = session.query(Student).filter_by(id = course.student_id).first()
        if student is None:
            abort(Response('Student not found', 404))
        session.add(course)
        session.commit()
        id = course.id
    return {'id': id}, 201


# @course_bp.get('/studentsincourse/<int:id>')
# def get_students_in_course(id):
#     with session_factory() as session:
#         student= session.query(course_has_student_table).filter_by(course_id=id).all()
#     if student == None:
#         abort(Response('Students not found', 404))
#     return {'id': id}, 201

@course_bp.get('/studentsincourse/<int:id>/')
def get_course_students(id):
    with session_factory() as session:
        ids = session.query(course_has_student_table).filter_by(course_id = id).all()
        if ids is None:
            abort(Response('Course has no students', 404))
        students = []
        for i in ids:
            students.append(session.query(Student).filter_by(id = i.student_id).first())

        if students is None:
            abort(Response('Course has no students', 404))
    return StudentSchema(many=True).dumps(students), 200

# {
#     "name" : "Math",
#     "credits" : 13,
#     "url" : "math.com",
#     "teacher_id": 1
# }

