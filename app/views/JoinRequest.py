from flask import *
from marshmallow import *
import app.models as models
from werkzeug.security import generate_password_hash
from ..db import session_factory
from ..models import Course, update,Teacher,Student,JoinRequest
from ..validation_models import CourseSchema,StudentSchema,JoinRequest


join_request_bp = Blueprint('join_request', __name__, url_prefix='/JoinRequest')

#Переробити і перевірити
@join_request_bp.get('/accept/<int:id>')
def get_courses():
    with session_factory() as session:
        request = session.query(Request).filter_by(id=id).first()
        request.status='accepted'
        request.course.students.append(request.student)
        session.commit()
    return Response('Request accepted', 201)



