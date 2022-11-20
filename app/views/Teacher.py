from flask import *
from marshmallow import *
import app.models as models
from werkzeug.security import generate_password_hash
from ..db import session_factory
from ..models import Course, update,Teacher
from ..validation_models import TeacherSchema

teacher_bp = Blueprint('teacher', __name__, url_prefix='/Teachers')

@teacher_bp.post('/')
def create_teacher():
    try:
        teacher = TeacherSchema().load(request.get_json())
    except:
        abort(Response('A Invalid input', 400))
    with session_factory() as session:
        if session.query(Teacher).filter_by(email=teacher.email).first() is not None:
            abort(Response('This email is already taken', 400))
        session.add(teacher)
        session.commit()
        id = teacher.id
    return {'id': id}, 201


@teacher_bp.get('/')
def get_teachers():
    with session_factory() as session:
        teacher = session.query(Teacher).all()
    return TeacherSchema(many=True).dumps(teacher)