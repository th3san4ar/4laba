from flask import *
from marshmallow import *
import app.models as models
from werkzeug.security import generate_password_hash
from ..db import session_factory
from ..models import Student, update,Course
from ..validation_models import StudentSchema

student_bp = Blueprint('student', __name__, url_prefix='/Students')



@student_bp.get('/')
def get_students():
    with session_factory() as session:
        student = session.query(Student).all()
    return StudentSchema(many=True).dumps(student)


@student_bp.get('/<int:id>')
def get_student(id):
    with session_factory() as session:
        student = session.query(Student).filter_by(id = id).first()
    if student == None:
        abort(Response('Student not found', 404))
    return StudentSchema().dumps(student), 200

# @student_bp.get('/<int:course_id>')
# def get_student(course_id):
#     with session_factory() as session:
#         student = session.query(Student).filter_by(id = id).first()
#     if student == None:
#         abort(Response('Student not found', 404))
#     return StudentSchema().dumps(student), 200


@student_bp.post('/')
def create_student():
    try:
        student = StudentSchema().load(request.get_json())
    except:
        abort(Response('Invalid input', 400))
    student.password = generate_password_hash(student.password)
    with session_factory() as session:
        if session.query(Student).filter_by(email = student.email).first() is not None:
            abort(Response('Invalid input', 400))
        session.add(student)
        session.commit()
        id = student.id
    return {'id': id}, 201


@student_bp.delete('/<int:id>')
def delete_student(id):
    with session_factory() as session:
        student = session.query(Student).filter_by(id = id).first()
        if student is None:
            abort(Response('User not found', 404))
        session.delete(student)
        session.commit()
    return Response('Student deleted', 200)

@student_bp.put('/<int:id>')
def update_student(id):
    try:
        updated = StudentSchema().load(request.get_json())
    except:
        abort(Response('Invalid input', 400))
    #updated.password = generate_password_hash(updated.password)
    with session_factory() as session:
        student = session.query(Student).filter_by(id = id).first()
        if student is None:
            abort(Response('Student not found', 404))
    #check if updated email is unique
        if session.query(Student).filter_by(email = updated.email).first() is not None:
            abort(Response('This email already exists', 400))
        student.first_name = updated.first_name
        student.last_name = updated.last_name
        student.email = updated.email
        student.password = updated.password
        student.password = generate_password_hash(student.password)
        student.create_time = updated.create_time

        session.commit()
    return Response('Student updated', 200)



# {
#     "first_name" : "Tony",
#     "second_name" : "Montana",
#     "email" : "tony@gmail.com",
#     "password" : "1234",
#     "create_time": "2004-05-23T14:25:10"
# }

